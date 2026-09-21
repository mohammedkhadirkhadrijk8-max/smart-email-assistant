/* ==================== DOM Elements ==================== */
const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');
const toast = document.getElementById('toast');

/* ==================== Tab Navigation ==================== */
tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        const tabName = button.getAttribute('data-tab');
        
        // Remove active class from all buttons and contents
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to clicked button and corresponding content
        button.classList.add('active');
        document.getElementById(tabName).classList.add('active');
    });
});

/* ==================== Toast Notifications ==================== */
function showToast(message, type = 'success') {
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

/* ==================== Fetch Emails ==================== */
async function fetchEmails() {
    try {
        const response = await fetch('/api/emails?max_results=10');
        const data = await response.json();
        
        if (data.success) {
            displayEmails(data.emails);
            showToast('Emails loaded successfully!', 'success');
        } else {
            showToast(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showToast('Failed to fetch emails', 'error');
        console.error('Error:', error);
    }
}

function displayEmails(emails) {
    const emailsList = document.getElementById('emailsList');
    
    if (emails.length === 0) {
        emailsList.innerHTML = '<p class="loading">No emails found</p>';
        return;
    }
    
    emailsList.innerHTML = emails.map(email => `
        <div class="email-item" onclick="showEmailDetail('${escapeHtml(email.id)}', '${escapeHtml(email.subject)}', '${escapeHtml(email.sender)}', '${escapeHtml(email.body)}')">
            <div class="email-from">📧 ${escapeHtml(email.sender)}</div>
            <div class="email-subject">${escapeHtml(email.subject)}</div>
            <div class="email-snippet">${escapeHtml(email.snippet.substring(0, 100))}...</div>
        </div>
    `).join('');
}

function showEmailDetail(id, subject, sender, body) {
    const modalBody = document.getElementById('modalBody');
    const modal = document.getElementById('emailModal');
    
    modalBody.innerHTML = `
        <div>
            <h2>${escapeHtml(subject)}</h2>
            <p><strong>From:</strong> ${escapeHtml(sender)}</p>
            <hr style="margin: 15px 0;">
            <div style="background: #f9f9f9; padding: 15px; border-radius: 6px; max-height: 400px; overflow-y: auto;">
                ${escapeHtml(body).replace(/\n/g, '<br>')}
            </div>
            <div style="margin-top: 15px;">
                <button onclick="useEmailForReply(\`${escapeHtml(body)}\`)" class="btn btn-primary">Use for Reply</button>
            </div>
        </div>
    `;
    
    modal.classList.remove('hidden');
}

function closeModal() {
    document.getElementById('emailModal').classList.add('hidden');
}

function useEmailForReply(emailBody) {
    document.getElementById('emailContent').value = emailBody;
    closeModal();
    
    // Switch to generate tab
    document.querySelector('[data-tab="generate"]').click();
    showToast('Email loaded in reply generator!', 'success');
}

/* ==================== Generate Reply ==================== */
async function generateReply() {
    const emailContent = document.getElementById('emailContent').value;
    const tone = document.getElementById('tone').value;
    const customContext = document.getElementById('customContext').value;
    
    if (!emailContent) {
        showToast('Please enter an email to reply to', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/generate-reply', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email_content: emailContent,
                tone: tone,
                custom_context: customContext
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('replyText').value = data.reply;
            document.getElementById('generatedReply').classList.remove('hidden');
            showToast('Reply generated successfully!', 'success');
        } else {
            showToast(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showToast('Failed to generate reply', 'error');
        console.error('Error:', error);
    }
}

function regenerateReply() {
    generateReply();
}

function copyReply() {
    const replyText = document.getElementById('replyText');
    replyText.select();
    document.execCommand('copy');
    showToast('Reply copied to clipboard!', 'success');
}

function useReplyForCompose() {
    const replyText = document.getElementById('replyText').value;
    document.getElementById('composeBody').value = replyText;
    
    // Switch to compose tab
    document.querySelector('[data-tab="compose"]').click();
    showToast('Reply loaded in compose!', 'success');
}

/* ==================== Send Email ==================== */
async function sendEmail() {
    const toEmail = document.getElementById('toEmail').value;
    const subject = document.getElementById('composeSubject').value;
    const messageBody = document.getElementById('composeBody').value;
    
    if (!toEmail || !subject || !messageBody) {
        showToast('Please fill in all fields', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/send-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                to_email: toEmail,
                subject: subject,
                message_body: messageBody
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Clear form
            document.getElementById('toEmail').value = '';
            document.getElementById('composeSubject').value = '';
            document.getElementById('composeBody').value = '';
            
            showToast('Email sent successfully!', 'success');
        } else {
            showToast(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        showToast('Failed to send email', 'error');
        console.error('Error:', error);
    }
}

/* ==================== Utility Functions ==================== */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

/* ==================== Load Emails on Page Load ==================== */
document.addEventListener('DOMContentLoaded', () => {
    fetchEmails();
});

/* ==================== Close Modal on Outside Click ==================== */
window.addEventListener('click', (event) => {
    const modal = document.getElementById('emailModal');
    if (event.target === modal) {
        closeModal();
    }
});
