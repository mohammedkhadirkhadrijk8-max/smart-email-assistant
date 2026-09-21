# Smart Email Assistant - Quick Start Checklist

## ✅ Quick Setup (5 minutes)

- [ ] Install Docker Desktop from https://www.docker.com/products/docker-desktop
- [ ] Get OpenAI API key from https://platform.openai.com/api-keys
- [ ] Get Gmail credentials from https://console.cloud.google.com/
- [ ] Create `.env` file with your API keys (see below)
- [ ] Place `credentials.json` in project root
- [ ] Run `docker compose up`
- [ ] Open http://localhost:5000

## 📝 Create .env File

Copy this into your `.env` file and fill in your keys:

```
FLASK_ENV=development
FLASK_SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=sk-your-openai-api-key-here
GMAIL_USER=your-email@gmail.com
```

## 🚀 Run Commands

```bash
# Build and start (first time)
docker compose up --build

# Start (if already built)
docker compose up

# Stop
docker compose down

# View logs
docker compose logs -f

# View running containers
docker ps
```

## 🌐 Access

- **Web Interface**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 in use | `docker compose down` first |
| credentials.json missing | Download from Google Cloud Console (Step 3 in SETUP_GUIDE.md) |
| API key error | Check `.env` file has correct OPENAI_API_KEY |
| Gmail auth fails | Delete `token.pickle` and try again |
| Docker not found | Install Docker Desktop and restart terminal |

## 📚 Features

✅ Read emails from Gmail
✅ AI-powered reply generation (professional, friendly, brief, grateful)
✅ Send emails directly
✅ Multiple tone options
✅ Beautiful web interface
✅ Real-time notifications

## 🆘 Need Full Guide?

See `SETUP_GUIDE.md` for detailed step-by-step instructions!

---

**Happy emailing! 📧🚀**
