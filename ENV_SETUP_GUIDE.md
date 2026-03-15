# .env File Setup Guide

## What is .env?

The `.env` file is a special file that stores sensitive information like API keys. It:
- ✅ Keeps your API key secure
- ✅ Prevents accidental sharing of keys
- ✅ Makes the app easier to use
- ✅ Is automatically ignored by git

## Setup Steps

### 1. Get Your Gemini API Key

1. Go to: **https://makersuite.google.com/app/apikey**
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated key (it starts with `AIza...`)

### 2. Edit the .env File

The `.env` file is already created in your project directory.

**Option A: Using VS Code (Recommended)**
1. Open VS Code
2. Find and click on `.env` file in the explorer
3. Replace `your_api_key_here` with your actual API key
4. Save the file (Ctrl+S)

**Option B: Using Notepad**
1. Right-click on `.env` file
2. Open With → Notepad
3. Replace `your_api_key_here` with your actual API key
4. Save (Ctrl+S)

### 3. Example

**Before:**
```
GEMINI_API_KEY=your_api_key_here
```

**After:**
```
GEMINI_API_KEY=AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## How the App Uses It

When you run the app:
1. ✓ Automatically reads your `.env` file
2. ✓ Loads the API key
3. ✓ Shows "API Key loaded from .env file" in sidebar
4. ✓ You don't need to enter it manually!

## File Descriptions

### `.env` (Only on Your Computer ⚠️)
- Contains your actual API key
- **NEVER** commit this to git
- Already in `.gitignore`
- Change this file

### `.env.example` (Safe to Share ✓)
- Template showing the format
- Does NOT contain real API key
- Safe to share/upload to git
- Don't change unless updating template

### `.gitignore`
- Tells git to ignore `.env` file
- Prevents accidental committing of secrets
- Automatically ignores sensitive files

## Important Security Notes

⚠️ **DO NOT:**
- Share your `.env` file
- Upload `.env` to GitHub
- Post your API key online
- Give `.env` to anyone

✅ **DO:**
- Keep `.env` file locally only
- Regenerate key if accidentally shared
- Use `.env.example` as template
- Follow the `.gitignore` rules

## Troubleshooting

### "API Key not loading"
1. Check `.env` file exists in project directory
2. Verify format: `GEMINI_API_KEY=your_key`
3. No extra spaces around `=`
4. Restart the app

### "Still asking for API key"
- `.env` might have wrong format
- Check for typos in `GEMINI_API_KEY`
- Make sure key is copied correctly
- Restart terminal and try again

### "Module not found: dotenv"
- Run: `pip install python-dotenv`
- Already installed if you ran latest setup

## Optional: Override in App

You can also manually enter a different API key in the app:
1. Click "Use different API key?" checkbox in sidebar
2. Enter a different API key
3. This overrides the .env file for that session only

## Example Project Structure

```
capstone_project_eq_solver/
├── .env                  ← Your API key (KEEP SECRET!)
├── .env.example          ← Template (safe to share)
├── .gitignore           ← Security rules
├── app.py               ← Main app
└── other files...
```

## Next Steps

1. ✅ Get your API key from makersuite.google.com/app/apikey
2. ✅ Edit the `.env` file and paste your key
3. ✅ Run the app: `streamlit run app.py` or double-click `run_app.bat`
4. ✅ Enjoy! The app will auto-load your key

## Tips

💡 **Pro Tips:**
- Keep `.env` backed up securely
- Regenerate key monthly for security
- Use different keys for development/production
- Never commit `.env` to version control
- For team projects, share `.env.example` only

---

That's it! Your API key is now secure and ready to use. 🔐✨
