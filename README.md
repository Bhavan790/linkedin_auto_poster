<div align="center">

# 📢 LinkedIn Auto Poster

### Automate your daily LinkedIn presence with Python

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-API-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com)
[![Automation](https://img.shields.io/badge/Automation-Daily%20Posts-brightgreen?style=flat)](https://github.com/Bhavan790/linkedin_auto_poster)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)

**Schedule and auto-publish LinkedIn posts daily — no manual effort, consistent presence, zero burnout.**

[Features](#-features) · [Quick Start](#-quick-start) · [Configuration](#️-configuration) · [How It Works](#-how-it-works) · [Roadmap](#️-roadmap)

</div>

---

## 💡 Why I Built This

Maintaining a consistent LinkedIn presence is tough for students and developers who are heads-down building things. This tool lets you write your posts in advance, schedule them, and have them go live automatically — so your profile stays active even when you're busy coding.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📅 **Scheduled Posting** | Set time and frequency — posts go live automatically |
| 📝 **Post Queue** | Write multiple posts in advance, runs through them in order |
| 🖼️ **Image Support** | Attach images to posts automatically |
| 🔐 **Secure Auth** | Credentials stored in `.env` — never hardcoded |
| 📋 **Post Logging** | Every post is logged with timestamp and status |
| 🔁 **Retry Logic** | Auto-retries on failure so no post gets skipped |

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/Bhavan790/linkedin_auto_poster.git
cd linkedin_auto_poster
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your credentials

```bash
cp .env.example .env
```

Edit `.env` with your LinkedIn credentials:

```env
LINKEDIN_EMAIL=your_email@gmail.com
LINKEDIN_PASSWORD=your_password_here
POST_TIME=09:00
```

### 4. Add your posts

Edit `posts.txt` — one post per block, separated by `---`:

```
Just shipped a new feature on my AI Privacy Shield project! 
Built using FastAPI + NVIDIA Llama-3.1. Check it out on GitHub 🚀
#buildinpublic #python #ai

---

450 LeetCode problems down. 
Daily consistency beats occasional bursts. Keep going. 💪
#leetcode #dsa #coding
```

### 5. Run it

```bash
python main.py
```

The script will post at your configured time every day. Run it in the background with:

```bash
nohup python main.py &
```

---

## ⚙️ Configuration

All config lives in `.env`:

| Variable | Description | Default |
|---|---|---|
| `LINKEDIN_EMAIL` | Your LinkedIn login email | — |
| `LINKEDIN_PASSWORD` | Your LinkedIn password | — |
| `POST_TIME` | Daily post time (24hr format) | `09:00` |
| `POST_INTERVAL_DAYS` | Days between posts | `1` |
| `LOG_FILE` | Path to log file | `logs/posts.log` |

---

## 📁 Project Structure

```
linkedin_auto_poster/
├── main.py              # Entry point — starts the scheduler
├── poster.py            # Core LinkedIn posting logic
├── scheduler.py         # Time-based job runner
├── posts.txt            # Your post queue (edit this!)
├── logs/
│   └── posts.log        # Auto-generated post history
├── .env.example         # Template for credentials
├── requirements.txt
└── README.md
```

---

## 🔄 How It Works

```
posts.txt (your content)
        │
        ▼
  scheduler.py  ──── checks time every minute
        │
        ▼ (when POST_TIME matches)
   poster.py
        │
        ├── Logs into LinkedIn
        ├── Reads next post from queue
        ├── Publishes the post
        └── Logs result to posts.log
```

---

## 📋 Requirements

```txt
selenium==4.x
schedule
python-dotenv
requests
```

Install all at once:
```bash
pip install -r requirements.txt
```

> **Note:** Selenium requires a browser driver. Install ChromeDriver matching your Chrome version from [chromedriver.chromium.org](https://chromedriver.chromium.org).

---

## 🔒 Security Notes

- **Never commit your `.env` file** — it's in `.gitignore` by default
- Use a dedicated LinkedIn account or App Password if possible
- LinkedIn may flag automation — use reasonable posting frequency (once/day max)

---

## 🗺️ Roadmap

- [x] Daily scheduled posting
- [x] Post queue from text file
- [x] Logging with timestamps
- [ ] Google Sheets integration (manage posts in a spreadsheet)
- [ ] Image/media attachment support
- [ ] LinkedIn Official API support (OAuth)
- [ ] Telegram bot to add posts on the go
- [ ] Analytics — track impressions per post

---

## ⚠️ Disclaimer

This tool uses browser automation (Selenium). Use responsibly and in accordance with [LinkedIn's User Agreement](https://www.linkedin.com/legal/user-agreement). Automating actions on LinkedIn may violate their ToS if abused — use for personal productivity only.

---

## 👨‍💻 Author

**Bhavan Kumar RT**
B.E. Electrical & Electronics · Rajalakshmi Engineering College

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bhavan%20Kumar%20RT-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/bhavan-kumar-rt)
[![GitHub](https://img.shields.io/badge/GitHub-Bhavan790-181717?style=flat&logo=github)](https://github.com/Bhavan790)
[![LeetCode](https://img.shields.io/badge/LeetCode-450%2B%20Solved-FFA116?style=flat&logo=leetcode&logoColor=white)](https://leetcode.com)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with ☕ and 🐍 by Bhavan Kumar RT · Star ⭐ if this saves you time!</sub>
</div>
