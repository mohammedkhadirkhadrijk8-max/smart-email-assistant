# 🎯 EXECUTION CHECKLIST - Step by Step for Mac Users

## 📋 Before You Start

You need to have on your Mac:
- ✅ Docker Desktop (will download)
- ✅ OpenAI Account (will get key)
- ✅ Gmail Account
- ✅ This entire project folder

---

## 🎬 PART 1: Install Docker (5 minutes)

### Step 1.1: Download Docker Desktop

1. Open your browser
2. Go to: https://www.docker.com/products/docker-desktop
3. Look for "Download for Mac"
4. Choose based on your Mac chip:
   - **Apple Silicon (M1/M2/M3)** → Click "Apple Silicon"
   - **Intel Mac** → Click "Intel Chip"
5. Wait for download to complete

### Step 1.2: Install Docker

1. Open your **Downloads** folder
2. Find `Docker.dmg` file
3. Double-click to open it
4. Drag the **Docker** icon to the **Applications** folder
5. Wait for copy to complete
6. Eject the disk image

### Step 1.3: Launch Docker

1. Open **Applications** folder
2. Find **Docker**
3. Double-click to launch
4. Enter your Mac password if prompted
5. Wait for Docker menu bar icon to appear (≈ 2-3 minutes)
6. You'll see Docker icon in top-right menu bar

### Step 1.4: Verify Docker Installation

Open **Terminal** and run:

```bash
docker --version
```

You should see something like: `Docker version 24.0.0, build abcdef`

✅ **Docker is ready!**

---

## 🔑 PART 2: Get Your API Keys (5 minutes)

### Step 2.1: Get OpenAI API Key

1. Open browser → https://platform.openai.com/api-keys
2. Sign in with OpenAI account (create if needed)
3. Click **"+ Create new secret key"**
4. A popup shows your key starting with `sk-`
5. Click **Copy** button
6. **Important:** Save it somewhere safe (Notepad, 1Password, etc.)
7. You won't see it again!

✅ **Save your key** - You'll need it in Part 4

### Step 2.2: Get Gmail Credentials

**This is the longest part - takes about 10 minutes**

#### Substep A: Create Google Cloud Project

1. Open browser → https://console.cloud.google.com/
2. Sign in with your Gmail account
3. Near the top, find "Select a Project" dropdown
4. Click **"NEW PROJECT"**
5. Enter name: `Email Assistant`
6. Click **"CREATE"**
7. Wait for project to be created (≈ 1-2 minutes)

#### Substep B: Enable Gmail API

1. In left sidebar, click **"APIs & Services"**
2. Click **"Library"**
3. Search box appears - type: `Gmail API`
4. Click the "Gmail API" result
5. Click blue **"ENABLE"** button
6. Wait for it to enable (≈ 30 seconds)

#### Substep C: Create OAuth Credentials

1. In left sidebar, click **"APIs & Services"** → **"Credentials"**
2. Click blue **"+ CREATE CREDENTIALS"** button
3. Choose **"OAuth client ID"**
4. It asks "OAuth consent screen" - click **"CONFIGURE CONSENT SCREEN"**
5. Choose **"External"** and click **"CREATE"**
6. Fill the form:
   - **App name:** `Email Assistant`
   - **User support email:** Your email
   - **Developer contact:** Your email
7. Click **"SAVE AND CONTINUE"**
8. Next page → Click **"SAVE AND CONTINUE"** (no need to fill)
9. Next page → Click **"SAVE AND CONTINUE"** (same)
10. Click **"BACK TO DASHBOARD"**

#### Substep D: Download Credentials JSON

1. Go to **"Credentials"** (left sidebar)
2. Under "OAuth 2.0 Client IDs", find your app
3. Click the download icon (⬇️)
4. A JSON file downloads
5. **Rename it to exactly:** `credentials.json`
6. Move to your project folder

✅ **Gmail credentials ready!**

---

## 📁 PART 3: Set Up Project Folder (2 minutes)

### Step 3.1: Check Project Files

In your project folder, you should have:

```
smart-email-assistant/
├── app.py ✅
├── requirements.txt ✅
├── Dockerfile ✅
├── docker-compose.yml ✅
├── .dockerignore ✅
├── .env.example ✅
├── credentials.json ✅ (you just added)
├── templates/
│   └── index.html ✅
├── static/
│   ├── style.css ✅
│   └── script.js ✅
├── Makefile ✅
├── README.md ✅
├── SETUP_GUIDE.md ✅
└── QUICK_START.md ✅
```

All files should be there!

### Step 3.2: Create .env File

1. Open Terminal
2. Navigate to your project:
```bash
cd /path/to/smart-email-assistant
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Open the `.env` file in a text editor:
```bash
nano .env
```

5. You'll see:
```
FLASK_ENV=development
FLASK_SECRET_KEY=your-secret-key-change-in-production
OPENAI_API_KEY=your-openai-api-key-here
GMAIL_USER=your-email@gmail.com
```

6. Replace:
   - `your-openai-api-key-here` → **Paste your OpenAI key** (from Part 2)
   - `your-email@gmail.com` → **Your Gmail address**
   - Leave `FLASK_SECRET_KEY` as is

7. Save and exit: Press `Ctrl+X`, then `Y`, then `Enter`

✅ **.env file is ready!**

---

## 🐳 PART 4: Build and Run with Docker (5 minutes)

### Step 4.1: Navigate to Project

Open Terminal and go to your project:

```bash
cd /path/to/smart-email-assistant
```

### Step 4.2: Build the Docker Image

Run this command (first time only, takes 2-3 minutes):

```bash
docker compose build
```

You'll see lots of text - that's normal. It's downloading and installing everything.

**Wait for it to finish** ✅

### Step 4.3: Start the Application

Run this command to start:

```bash
docker compose up
```

You'll see output like:
```
smart-email-assistant | * Running on http://0.0.0.0:5000
smart-email-assistant | * Debugger is active!
```

✅ **Application is running!**

---

## 💻 PART 5: First Time Using the App (3 minutes)

### Step 5.1: Open in Browser

1. Open your web browser (Chrome, Safari, Firefox, etc.)
2. Go to: **http://localhost:5000**
3. You should see a beautiful purple interface!

### Step 5.2: Gmail Authentication

1. Click the **"📬 Inbox"** tab
2. Click **"Refresh Emails"** button
3. A browser window opens asking for Gmail permission
4. Click **"Allow"**
5. You're done!

✅ **Ready to use!**

---

## 🎮 PART 6: How to Use

### Reading Emails
1. Click **"📬 Inbox"** tab
2. Your recent emails appear
3. Click on any email to see full content

### Generating Replies
1. Click **"🤖 Generate Reply"** tab
2. Paste an email or use one from inbox
3. Pick a tone: Professional, Friendly, Brief, or Grateful
4. Click **"Generate Reply"**
5. Copy or use the generated text

### Sending Emails
1. Click **"✉️ Compose"** tab
2. Fill in: To, Subject, Message
3. Click **"Send Email"**

---

## ⏹️ PART 7: Stop the App

When you're done, go back to Terminal and press:

```
Ctrl + C
```

The app stops. To start again next time:

```bash
cd /path/to/smart-email-assistant
docker compose up
```

---

## 🆘 Troubleshooting

### "docker: command not found"
→ Make sure Docker Desktop is fully launched
→ Wait 2-3 minutes after clicking Docker icon

### "Cannot find credentials.json"
→ Make sure file is named EXACTLY `credentials.json`
→ Place it in root project folder (same level as app.py)

### "Port 5000 already in use"
→ Run: `docker compose down` first
→ Then run: `docker compose up` again

### "OPENAI_API_KEY not set"
→ Check your `.env` file
→ Make sure you pasted the full key correctly
→ No spaces around the `=` sign
→ Restart app: `Ctrl+C`, then `docker compose up`

### "Gmail says permission denied"
→ Delete `token.pickle` file in your folder
→ Go through Gmail auth again

### "Nothing happens when I click buttons"
→ Check Terminal for error messages
→ Copy error text and search it

---

## ✅ Summary of Everything

```
✅ Docker Desktop installed
✅ OpenAI API key obtained
✅ Gmail credentials downloaded
✅ .env file created with your keys
✅ credentials.json in project folder
✅ Docker image built
✅ Application running at http://localhost:5000
✅ Gmail authenticated
✅ Ready to generate AI email replies!
```

---

## 📞 What You Need from Me

**Before you start, I need you to provide:**

1. **For OpenAI:**
   - OpenAI account (create at openai.com if needed)
   - Will get API key from platform.openai.com

2. **For Gmail:**
   - Gmail account (any Google account)
   - Google Cloud Project (will create free)

3. **For Your Mac:**
   - Download Docker Desktop
   - About 5GB free disk space
   - About 30 minutes of your time

**That's it!** Everything else is in the code.

---

## 🎉 You're All Set!

Follow these steps and you'll have a fully functional AI Email Assistant running on your Mac!

**Questions?** Check:
- `README.md` - Full overview
- `SETUP_GUIDE.md` - Detailed guide
- `QUICK_START.md` - Quick reference

**Good luck!** 🚀📧
