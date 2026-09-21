# Smart Email Assistant - Complete Setup Guide

## 📋 Prerequisites

Before starting, make sure you have the following installed on your Mac:

1. **Docker Desktop** - Download from https://www.docker.com/products/docker-desktop
2. **OpenAI API Key** - Get from https://platform.openai.com/api-keys
3. **Gmail Credentials** - You'll need to set up OAuth credentials (explained below)

---

## 🚀 Step-by-Step Setup Instructions

### STEP 1: Install Docker Desktop (If Not Already Installed)

```bash
# Download and install Docker Desktop for Mac
# Visit: https://www.docker.com/products/docker-desktop
# Open the DMG file and drag Docker to Applications folder
# Launch Docker from Applications
```

**Verify Docker is installed:**
```bash
docker --version
docker run hello-world
```

---

### STEP 2: Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in with your OpenAI account (create one if needed)
3. Click "Create new secret key"
4. Copy the key and save it safely (you'll need it in Step 4)

---

### STEP 3: Set Up Gmail OAuth Credentials

1. Go to https://console.cloud.google.com/
2. Create a new project:
   - Click "Select a Project" → "NEW PROJECT"
   - Name it "Email Assistant"
   - Click "CREATE"

3. Enable the Gmail API:
   - Go to APIs & Services → Library
   - Search for "Gmail API"
   - Click on it and press "ENABLE"

4. Create OAuth 2.0 Credentials:
   - Go to APIs & Services → Credentials
   - Click "CREATE CREDENTIALS" → "OAuth client ID"
   - Choose "Desktop application"
   - Click "CREATE"
   - Download the JSON file

5. Rename the downloaded file to `credentials.json` and place it in your project folder

---

### STEP 4: Set Up Environment Variables

1. In your project folder, create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

2. Edit the `.env` file and add your OpenAI API key:

```
FLASK_ENV=development
FLASK_SECRET_KEY=your-super-secret-key-12345
OPENAI_API_KEY=sk-your-openai-key-here
GMAIL_USER=your-email@gmail.com
```

Replace:
- `your-openai-key-here` with your actual OpenAI API key
- `your-email@gmail.com` with your Gmail address

---

### STEP 5: Project Structure

Make sure your project folder looks like this:

```
email-assistant/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── .env                          (create this)
├── credentials.json              (download this)
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

### STEP 6: Build and Run with Docker

#### Option A: Using Docker Compose (Recommended for Mac)

```bash
# Navigate to your project folder
cd /path/to/email-assistant

# Build the Docker image
docker compose build

# Start the application
docker compose up
```

#### Option B: Using Docker Commands

```bash
# Build the image
docker build -t smart-email-assistant .

# Run the container
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=your-api-key \
  -e FLASK_SECRET_KEY=your-secret \
  -v $(pwd):/app \
  smart-email-assistant
```

---

### STEP 7: Access the Application

1. Open your web browser
2. Go to: **http://localhost:5000**
3. You should see the Smart Email Assistant interface

---

## 📱 How to Use the Application

### 1️⃣ First Time Setup - Gmail Authentication

When you first try to fetch emails:
1. Click "📬 Inbox" tab
2. Click "Refresh Emails"
3. A browser window will open asking for Gmail permission
4. Click "Allow" to grant access
5. A `token.pickle` file will be created automatically

### 2️⃣ Fetching Emails

- Go to "📬 Inbox" tab
- Click "Refresh Emails" to load your recent emails
- Click on any email to read the full content
- Click "Use for Reply" to quickly generate a response

### 3️⃣ Generating AI Replies

- Go to "🤖 Generate Reply" tab
- Paste or select an email you want to reply to
- Choose the tone (Professional, Friendly, Brief, Grateful)
- Add optional context for better replies
- Click "Generate Reply"
- View the generated reply
- Use "Copy" to copy it, or "Use in Compose" to send it

### 4️⃣ Composing and Sending Emails

- Go to "✉️ Compose" tab
- Fill in recipient email, subject, and message
- Click "Send Email"
- Email will be sent from your Gmail account

---

## 🛠️ Common Issues & Solutions

### Issue 1: "credentials.json not found"
**Solution:** 
- Follow Step 3 again to download credentials
- Make sure file is named exactly `credentials.json`
- Place it in the root project folder

### Issue 2: "OPENAI_API_KEY not set"
**Solution:**
- Edit your `.env` file
- Add: `OPENAI_API_KEY=sk-your-actual-key`
- Restart the Docker container: `docker compose restart`

### Issue 3: Port 5000 already in use
**Solution:**
```bash
# Stop other containers using port 5000
docker ps
docker stop <container-id>

# Or use a different port
docker run -p 5001:5000 ...
```

### Issue 4: Gmail permission denied
**Solution:**
- Delete `token.pickle` file
- Restart the application
- Go through Gmail authentication again

### Issue 5: "docker: command not found"
**Solution:**
- Make sure Docker Desktop is installed and running
- Open Docker from Applications folder
- Wait for it to fully start

---

## 🐳 Docker Commands Cheat Sheet

```bash
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# Stop the application
docker compose down

# View logs
docker compose logs -f

# Rebuild after code changes
docker compose build --no-cache

# Start a fresh container
docker compose up --pull always

# Remove all stopped containers
docker system prune

# View container details
docker inspect <container-name>
```

---

## 📊 Environment Variables Explained

| Variable | Purpose | Example |
|----------|---------|---------|
| `FLASK_ENV` | Flask environment mode | `development` or `production` |
| `FLASK_SECRET_KEY` | Flask session secret | Any random string |
| `OPENAI_API_KEY` | OpenAI API authentication | `sk-...` |
| `GMAIL_USER` | Your Gmail address | `your-email@gmail.com` |

---

## 🔐 Security Notes

⚠️ **Important:**
- Never commit `.env` file to Git (it's in `.gitignore`)
- Never share your API keys publicly
- Keep `credentials.json` private
- Use strong `FLASK_SECRET_KEY` in production
- Regenerate keys if accidentally exposed

---

## 📈 Next Steps & Enhancements

1. **Add Database**: Store email conversation history
2. **Schedule Tasks**: Auto-reply to emails during specific times
3. **Custom Prompts**: Save your own AI prompts for different scenarios
4. **Email Templates**: Create templates for common reply types
5. **Multi-Account**: Support multiple Gmail accounts
6. **Advanced Filtering**: Filter emails by sender, date, keywords

---

## 🆘 Need Help?

1. Check Docker Desktop logs: Docker menu → Troubleshoot
2. View container logs: `docker compose logs -f`
3. Test API endpoint: Open http://localhost:5000/health
4. Verify credentials exist: `ls -la credentials.json`

---

## 📚 Useful Resources

- Docker Documentation: https://docs.docker.com/
- Flask Documentation: https://flask.palletsprojects.com/
- Gmail API: https://developers.google.com/gmail/api
- OpenAI API: https://platform.openai.com/docs/api-reference
- Docker on Mac: https://docs.docker.com/desktop/install/mac-install/

---

Good luck! 🚀 Let me know if you need any help!
