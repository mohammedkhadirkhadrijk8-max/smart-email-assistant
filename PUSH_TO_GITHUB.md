# 🚀 How to Push to GitHub

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Sign in to your GitHub account (create one if needed)
3. Fill in:
   - **Repository name:** `smart-email-assistant`
   - **Description:** `AI-powered email assistant with Gmail integration and OpenAI`
   - **Visibility:** Choose "Public" or "Private"
   - **Initialize with README:** Leave unchecked (we have one)
4. Click **"Create repository"**

---

## Step 2: Copy Your Repository URL

After creating, GitHub shows you commands. Look for the URL that looks like:
```
https://github.com/YOUR_USERNAME/smart-email-assistant.git
```

Or if using SSH:
```
git@github.com:YOUR_USERNAME/smart-email-assistant.git
```

---

## Step 3: Push Your Code (Choose One Method)

### Method A: Using HTTPS (Easier for First Time)

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/smart-email-assistant.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

### Method B: Using SSH (More Secure)

```bash
# Add remote repository
git remote add origin git@github.com:YOUR_USERNAME/smart-email-assistant.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Step 4: Enter Your GitHub Credentials

### If Using HTTPS:
- GitHub will ask for username and password
- For password, use a **Personal Access Token** (not your password):
  1. Go to https://github.com/settings/tokens
  2. Click "Generate new token"
  3. Select `repo` scope
  4. Copy the token and paste when asked

### If Using SSH:
- Make sure SSH keys are set up:
  ```bash
  ssh-keygen -t ed25519 -C "your-email@example.com"
  # Follow prompts, press Enter for defaults
  ```
- Add public key to GitHub:
  1. Go to https://github.com/settings/keys
  2. Click "New SSH key"
  3. Paste your public key

---

## Step 5: Verify Push Succeeded

```bash
git remote -v
# Should show:
# origin  https://github.com/YOUR_USERNAME/smart-email-assistant.git (fetch)
# origin  https://github.com/YOUR_USERNAME/smart-email-assistant.git (push)
```

Visit your repository on GitHub:
```
https://github.com/YOUR_USERNAME/smart-email-assistant
```

---

## Commands Ready to Copy-Paste

### For HTTPS (Just Replace YOUR_USERNAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/smart-email-assistant.git
git branch -M main
git push -u origin main
```

### For SSH (Just Replace YOUR_USERNAME):

```bash
git remote add origin git@github.com:YOUR_USERNAME/smart-email-assistant.git
git branch -M main
git push -u origin main
```

---

## What Gets Pushed

✅ All application code
✅ All configuration files
✅ All documentation
✅ .gitignore (protects .env, credentials.json, token.pickle)

❌ NOT pushed (protected by .gitignore):
- `.env` file (has your API keys)
- `credentials.json` (has Gmail credentials)
- `token.pickle` (has Gmail tokens)
- `__pycache__` directories
- Virtual environment

---

## Troubleshooting

### "fatal: remote origin already exists"
```bash
git remote remove origin
# Then try the git remote add command again
```

### "Permission denied (publickey)"
- SSH keys not set up correctly
- Use HTTPS method instead
- Or set up SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### "401 Unauthorized"
- GitHub password/token incorrect
- Make sure you're using Personal Access Token, not password

---

## After Pushing

### Next Steps:
1. GitHub page shows your code
2. Share the URL with others
3. Future pushes: `git push origin main`
4. Pull changes: `git pull origin main`

### Add This to Your README
```markdown
## Quick Links
- **GitHub Repository:** https://github.com/YOUR_USERNAME/smart-email-assistant
- **Live App:** Will be running on http://localhost:5000
```

---

## Common Git Commands After Push

```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View history
git log
```

---

Need help? The repository is already initialized and committed locally. Just follow Step 1-4 above!
