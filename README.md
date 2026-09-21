# 📧 Smart Email Assistant - Complete Setup & User Guide

An AI-powered email assistant built with Python, Flask, and Docker. Automatically generates intelligent email replies using OpenAI, integrates with Gmail, and provides a beautiful web interface.

## ✨ Features

- 📬 **Gmail Integration** - Read emails directly from your Gmail account
- 🤖 **AI Reply Generation** - Generate smart replies in multiple tones
- 📤 **Send Emails** - Compose and send emails directly from the app
- 🎨 **Beautiful UI** - Modern, responsive web interface
- 🐳 **Docker Ready** - Run anywhere with one command
- ⚡ **Lightning Fast** - Optimized for performance
- 🔐 **Secure** - OAuth 2.0 authentication with Gmail

## 📦 What's Included

```
smart-email-assistant/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Docker Compose setup
├── .dockerignore           # Docker ignore patterns
├── Makefile               # Convenient commands
├── SETUP_GUIDE.md         # Detailed setup instructions
├── QUICK_START.md         # Quick reference
├── templates/
│   └── index.html         # Web interface
└── static/
    ├── style.css          # Styling
    └── script.js          # Frontend logic
```

## 🚀 Quick Start (Experienced Users)

```bash
# 1. Clone/download this project
cd smart-email-assistant

# 2. Create and fill .env file
cp .env.example .env
# Edit .env with your OpenAI API key

# 3. Add credentials.json from Google Cloud

# 4. Run with Docker
docker compose up

# 5. Open http://localhost:5000
```

## 📋 Prerequisites

✅ **Docker Desktop** - https://www.docker.com/products/docker-desktop
✅ **OpenAI API Key** - https://platform.openai.com/api-keys
✅ **Gmail Account** - Any Google account
✅ **Google Cloud Project** - Free tier available

## 🔧 Complete Setup (Step-by-Step)

### Step 1: Install Docker Desktop

**macOS:**
1. Visit https://www.docker.com/products/docker-desktop
2. Download "Docker.dmg" for Apple Silicon (M1/M2) or Intel
3. Open the DMG and drag Docker to Applications
4. Launch Docker from Applications folder

**Verify installation:**
```bash
docker --version
docker run hello-world
```

### Step 2: Get OpenAI API Key

1. Visit https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "+ Create new secret key"
4. Copy and save the key safely

### Step 3: Set Up Gmail Credentials

**Detailed instructions in SETUP_GUIDE.md - Section 3**

Quick summary:
1. Go to https://console.cloud.google.com/
2. Create new project "Email Assistant"
3. Enable Gmail API
4. Create OAuth 2.0 Desktop credentials
5. Download JSON file → rename to `credentials.json`
6. Place in project root folder

### Step 4: Configure Environment

```bash
# Copy example to actual file
cp .env.example .env

# Edit .env file with your keys
nano .env  # or use your preferred editor
```

Add your values:
```
FLASK_ENV=development
FLASK_SECRET_KEY=any-random-string-for-session
OPENAI_API_KEY=sk-your-actual-openai-key
GMAIL_USER=your-email@gmail.com
```

### Step 5: Run the Application

**Option A: Using Make (easiest on Mac)**
```bash
make up
```

**Option B: Using Docker Compose**
```bash
docker compose up
```

**Option C: Using Docker directly**
```bash
docker build -t email-assistant .
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=sk-your-key \
  -v $(pwd):/app \
  email-assistant
```

### Step 6: Access the App

Open your browser to: **http://localhost:5000**

## 📱 How to Use

### First Time: Gmail Authentication

1. Click "📬 Inbox" tab
2. Click "Refresh Emails"
3. Browser opens → Click "Allow" for Gmail access
4. Authorization complete!

### Reading Emails

1. Go to "📬 Inbox" tab
2. Your recent emails appear
3. Click any email to read full content
4. Click "Use for Reply" to start generating response

### Generating AI Replies

1. Go to "🤖 Generate Reply" tab
2. **Option A:** Paste email text directly
3. **Option B:** Click email in Inbox → "Use for Reply"
4. Choose tone:
   - **Professional** - Formal business tone
   - **Friendly** - Warm, conversational tone
   - **Brief** - Short, concise response
   - **Grateful** - Appreciative tone
5. Add optional context for better results
6. Click "Generate Reply"
7. Review generated text
8. Click "Copy" or "Use in Compose"

### Sending Emails

1. Go to "✉️ Compose" tab
2. Enter recipient email address
3. Add subject
4. Write or paste message body
5. Click "Send Email"

## 🎯 Use Cases

✅ Quick email responses during busy days
✅ Maintain professional tone automatically
✅ Generate replies in multiple languages (via custom context)
✅ Batch process similar emails
✅ Learn writing styles from AI suggestions
✅ Reduce email response time

## 🛠️ Troubleshooting

### Docker issues?
```bash
# Restart Docker
docker restart

# View logs
docker compose logs -f

# Rebuild fresh
docker compose build --no-cache
```

### Gmail not connecting?
- Delete `token.pickle` file
- Restart application
- Re-authenticate through browser

### API key errors?
- Check `.env` file syntax
- Verify no spaces around `=`
- Restart: `docker compose restart`

### Port 5000 in use?
```bash
# See what's using it
lsof -i :5000

# Stop all containers
docker compose down
```

### More issues?
See **SETUP_GUIDE.md** for detailed troubleshooting!

## 🐳 Docker Cheat Sheet

```bash
# Build image
docker compose build

# Start (foreground)
docker compose up

# Start (background)
docker compose up -d

# Stop
docker compose down

# View logs
docker compose logs -f

# Execute command in container
docker compose exec email-assistant bash

# List containers
docker ps -a

# Remove everything
docker system prune -a
```

## 📊 Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `FLASK_ENV` | Dev/production mode | `development` |
| `FLASK_SECRET_KEY` | Session encryption | `anything-secret` |
| `OPENAI_API_KEY` | OpenAI authentication | `sk-...` |
| `GMAIL_USER` | Email address | `you@gmail.com` |

## 🔐 Security

⚠️ **Never commit these files:**
- `.env` - Contains API keys
- `credentials.json` - Gmail credentials
- `token.pickle` - Access tokens

✅ **Already in .gitignore** - Safe to use

💡 **Production tips:**
- Use strong `FLASK_SECRET_KEY`
- Store API keys in secrets manager
- Enable HTTPS
- Use environment-specific configs

## 📚 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with routes and logic |
| `requirements.txt` | Python package dependencies |
| `Dockerfile` | Docker container definition |
| `docker-compose.yml` | Multi-container orchestration |
| `templates/index.html` | Web interface HTML |
| `static/style.css` | User interface styling |
| `static/script.js` | Frontend interactivity |
| `Makefile` | Convenient command shortcuts |

## 🚀 Advanced Features

### Custom Tones

Add new response tones by editing `EMAIL_TEMPLATES` in `app.py`:

```python
EMAIL_TEMPLATES = {
    'your-tone': 'Your custom prompt here...',
    ...
}
```

### Multiple Accounts

Modify `app.py` to support multiple Gmail accounts:
1. Store multiple tokens
2. Add account selector to UI
3. Switch service based on selection

### Scheduling

Add background tasks:
```bash
pip install celery redis
```

## 📈 Next Steps

1. **Customize prompts** - Edit `EMAIL_TEMPLATES` for your needs
2. **Deploy** - Use Docker on cloud (AWS, GCP, Azure)
3. **Database** - Add email history storage
4. **Analytics** - Track response times and types
5. **Integrations** - Connect to Slack, Teams, etc.

## 🆘 Getting Help

1. **Read SETUP_GUIDE.md** - Comprehensive setup guide
2. **Check logs** - `docker compose logs -f`
3. **Verify files** - Ensure credentials and .env exist
4. **Test API** - Visit http://localhost:5000/health
5. **Forum/Issues** - GitHub discussions

## 📞 Support Resources

- **Flask Docs:** https://flask.palletsprojects.com/
- **Docker Docs:** https://docs.docker.com/
- **OpenAI API:** https://platform.openai.com/docs/
- **Gmail API:** https://developers.google.com/gmail/api

## 📜 License

MIT License - Feel free to use and modify!

## 🎉 You're Ready!

Follow the Quick Start or complete setup above and you'll be generating intelligent email replies in minutes!

**Questions?** Check SETUP_GUIDE.md or QUICK_START.md

---

**Happy emailing! 📧✨**

Built with ❤️ using Python, Flask, OpenAI, and Docker
