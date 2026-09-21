#!/usr/bin/env python3
"""
Smart Email Assistant - AI-powered email reply generator
"""

import os
import json
import pickle
import base64
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request, jsonify
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.cloud import storage as gcs
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import openai
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-change-in-production')

# Gmail API setup
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.send']
GMAIL_CREDENTIALS_FILE = 'credentials.json'
GMAIL_TOKEN_FILE = 'token.pickle'

# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')

# Email templates for different scenarios
EMAIL_TEMPLATES = {
    'professional': "Generate a professional email reply to the following email. Keep it concise and formal.\n\nOriginal email:\n{email_content}",
    'friendly': "Generate a friendly and warm email reply to the following email. Keep it conversational.\n\nOriginal email:\n{email_content}",
    'brief': "Generate a brief one-paragraph email reply to the following email.\n\nOriginal email:\n{email_content}",
    'grateful': "Generate a grateful and appreciative email reply to the following email.\n\nOriginal email:\n{email_content}",
}


class GmailHandler:
    """Handles Gmail API operations"""
    
    def __init__(self):
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Authenticate with Gmail API"""
        creds = None
        
        # Load existing token
        if os.path.exists(GMAIL_TOKEN_FILE):
            with open(GMAIL_TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        
        # If no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(GMAIL_CREDENTIALS_FILE):
                    logger.error(f"Please download {GMAIL_CREDENTIALS_FILE} from Google Cloud Console")
                    return False
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    GMAIL_CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for future use
            with open(GMAIL_TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
        
        self.service = build('gmail', 'v1', credentials=creds)
        return True
    
    def get_emails(self, max_results=10, query=''):
        """Fetch emails from Gmail"""
        try:
            results = self.service.users().messages().list(
                userId='me', 
                q=query, 
                maxResults=max_results
            ).execute()
            
            messages = results.get('messages', [])
            emails = []
            
            for message in messages:
                msg = self.service.users().messages().get(
                    userId='me', 
                    id=message['id'], 
                    format='full'
                ).execute()
                
                headers = msg['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                
                # Extract body
                body = self._get_email_body(msg['payload'])
                
                emails.append({
                    'id': message['id'],
                    'subject': subject,
                    'sender': sender,
                    'body': body,
                    'snippet': msg['snippet']
                })
            
            return emails
        except HttpError as error:
            logger.error(f'An error occurred: {error}')
            return []
    
    def _get_email_body(self, payload):
        """Extract email body from payload"""
        if 'parts' in payload:
            return ''.join([self._get_email_body(part) for part in payload['parts']])
        else:
            data = payload['body'].get('data', '')
            if data:
                return base64.urlsafe_b64decode(data).decode('utf-8')
        return ''
    
    def send_email(self, to_email, subject, message_body):
        """Send an email"""
        try:
            message = {
                'raw': base64.urlsafe_b64encode(
                    f'To: {to_email}\nSubject: {subject}\n\n{message_body}'.encode()
                ).decode()
            }
            
            self.service.users().messages().send(
                userId='me', 
                body=message
            ).execute()
            
            return True
        except HttpError as error:
            logger.error(f'An error occurred: {error}')
            return False


class EmailReplyGenerator:
    """Generates AI-powered email replies"""
    
    @staticmethod
    def generate_reply(email_content, tone='professional', custom_context=''):
        """Generate an email reply using OpenAI"""
        try:
            template = EMAIL_TEMPLATES.get(tone, EMAIL_TEMPLATES['professional'])
            
            prompt = template.format(email_content=email_content)
            if custom_context:
                prompt += f"\n\nAdditional context: {custom_context}"
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional email assistant. Generate concise, clear, and appropriate email replies."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message['content'].strip()
        except Exception as error:
            logger.error(f'Error generating reply: {error}')
            return None


# Initialize Gmail handler
gmail_handler = GmailHandler()


# ============ ROUTES ============

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/emails', methods=['GET'])
def get_emails_api():
    """API endpoint to fetch emails"""
    try:
        max_results = request.args.get('max_results', 10, type=int)
        query = request.args.get('query', '')
        
        emails = gmail_handler.get_emails(max_results=max_results, query=query)
        
        return jsonify({
            'success': True,
            'emails': emails
        })
    except Exception as error:
        logger.error(f'Error fetching emails: {error}')
        return jsonify({
            'success': False,
            'error': str(error)
        }), 500


@app.route('/api/generate-reply', methods=['POST'])
def generate_reply_api():
    """API endpoint to generate an email reply"""
    try:
        data = request.json
        email_content = data.get('email_content', '')
        tone = data.get('tone', 'professional')
        custom_context = data.get('custom_context', '')
        
        if not email_content:
            return jsonify({
                'success': False,
                'error': 'Email content is required'
            }), 400
        
        reply = EmailReplyGenerator.generate_reply(
            email_content, 
            tone=tone, 
            custom_context=custom_context
        )
        
        if reply:
            return jsonify({
                'success': True,
                'reply': reply
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to generate reply'
            }), 500
    except Exception as error:
        logger.error(f'Error generating reply: {error}')
        return jsonify({
            'success': False,
            'error': str(error)
        }), 500


@app.route('/api/send-email', methods=['POST'])
def send_email_api():
    """API endpoint to send an email"""
    try:
        data = request.json
        to_email = data.get('to_email', '')
        subject = data.get('subject', '')
        message_body = data.get('message_body', '')
        
        if not all([to_email, subject, message_body]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400
        
        success = gmail_handler.send_email(to_email, subject, message_body)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Email sent successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to send email'
            }), 500
    except Exception as error:
        logger.error(f'Error sending email: {error}')
        return jsonify({
            'success': False,
            'error': str(error)
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
