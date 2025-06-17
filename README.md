# 📬 Tech Digest AI Email Agent

A Flask-powered email subscription system that delivers curated tech news to your inbox. Users can sign up through a beautiful landing page and receive:

* 📥 An instant welcome email
* 📧 Daily “Hi” emails sent automatically at 9AM

Deployed with **Vercel (frontend)** and **GitHub Actions or Render (cron agent)**.

---

## 📁 Project Structure

```
project-root/
├── app/
│   ├── templates/
│   │   └── index.html             # Main HTML template with article display and form
│   ├── static/
│   │   ├── style.css              # CSS styling for the webpage
│   ├── articles.py                # 15 hardcoded tech articles with images and links
│   ├── email_utils.py             # Logic to send welcome and daily emails via SendGrid
│   ├── main.py                    # Flask app with form logic and database insert
│   ├── schedule_task.py           # Script to send daily emails to subscribers
│   ├── subscribers.db             # SQLite DB storing user emails (auto-generated)
│   ├── requirements.txt           # Python dependencies
│   └── .env                       # Environment variables (SENDGRID_API_KEY, etc.)
├── .github/
│   └── workflows/
│       └── daily-email.yml        # GitHub Action to send daily emails
└── README.md                      # This file
```

---

## 🚀 How to Run Locally

### 1. ✅ Clone and Navigate

```bash
git clone https://github.com/devtechster/AI-Agent.git
cd tech-digest
```

### 2. ✅ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: .\venv\Scripts\activate
```

### 3. ✅ Install Dependencies

```bash
pip install -r app/requirements.txt
```

### 4. ✅ Setup Environment Variables

Create `app/.env`:

```
SENDGRID_API_KEY=your-sendgrid-key
FROM_EMAIL=your-verified-sender@email.com
```

### 5. ✅ Run the Flask App

```bash
cd app
python main.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## ⏰ Schedule Daily Email (via GitHub Actions)

1. The `app/schedule_task.py` script sends “Hi” emails to all subscribers
2. GitHub Actions runs it daily using `.github/workflows/daily-email.yml`
3. After pushing to GitHub, go to:

   * **Settings → Secrets → Actions**
   * Add:

     * `SENDGRID_API_KEY`
     * `FROM_EMAIL`

---

## 🌐 Deployment Recommendations

| Component | Platform                    | Notes                                                           |
| --------- | --------------------------- | --------------------------------------------------------------- |
| Frontend  | Vercel                      | Upload `/app/templates/index.html` and `/static` as static site |
| Cron Job  | Render.com / GitHub Actions | Run `schedule_task.py` daily at 9AM                             |

---

## 📄 License (MIT)

```
MIT License

Copyright (c) 2025 Tech Digest Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💡 Author Notes

* You can easily extend this to pull live tech articles from APIs (e.g., NewsAPI)
* SQLite can be swapped for Supabase or Postgres for multi-user cloud deployment
* Want to add unsubscribe links, rich HTML emails, or user preferences? Open an issue or fork it!