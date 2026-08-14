<h1 align="center">🚀 AdSync AI</h1>

<p align="center">
  <b>AI-powered landing page personalization — turn ad creatives into high-converting pages, automatically.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-Django-darkgreen?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/AI-OpenAI%20API-black?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/Database-Supabase%20%2F%20PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

<p align="center">
  <a href="#-demo">Demo</a> •
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 🎥 Demo

https://github.com/user-attachments/assets/1845875f-4b4a-40e2-b616-4819122903dd

---

## 📌 Overview

**AdSync AI** is an AI-powered landing page personalization platform. Feed it an ad creative, marketing copy, and a target URL — it analyzes the ad and existing web content, then generates an optimized, custom landing page designed to convert.

Instead of manually rebuilding landing pages for every campaign, AdSync AI applies AI and **Conversion Rate Optimization (CRO)** principles automatically, so each page matches the intent and messaging of the ad that drives traffic to it — a technique known to significantly lift conversion rates over generic, one-size-fits-all pages.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **AI-Generated Landing Pages** | Auto-builds custom pages from ad creatives and marketing text |
| 📢 **Ad Creative Analysis** | Extracts intent, tone, and key messaging from ad content |
| 🌐 **Website Content Extraction** | Pulls existing site content to keep pages on-brand and consistent |
| 🧠 **Smart Personalization Engine** | Matches page content and layout to what the ad actually promises |
| 📈 **Conversion-Focused Optimization** | Applies CRO principles to maximize landing page performance |
| 🤖 **AI Chatbot Integration** | Adds an on-page assistant to engage visitors in real time |
| 📊 **Analytics Dashboard** | Tracks page performance and visitor behavior |
| 📰 **Blog Management System** | Built-in content publishing for ongoing marketing needs |

---

## 🖥 Screenshots

### Homepage
<p align="center">
  <img width="500" alt="AdSync AI Homepage" src="https://github.com/user-attachments/assets/d29a9ace-857b-4710-b3c9-17af9cb418b9" />
</p>

### Generated Landing Page
<p align="center">
  <img width="900" alt="AI-Generated Landing Page" src="https://github.com/user-attachments/assets/347db2d6-ec55-48e4-a168-b95bc6d9369a" />
</p>

---

## 🛠 Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="50"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="50"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="50"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="50"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="50"/>
</p>

| Layer | Technology |
|---|---|
| **Backend** | Python, Django |
| **Frontend** | HTML, CSS, JavaScript |
| **AI Engine** | OpenAI API |
| **Database** | Supabase, PostgreSQL |

---

## ⚙️ How It Works

1. **Input** — Provide an ad creative, marketing copy, and a target URL.
2. **Analysis** — AdSync AI analyzes the ad's messaging, tone, and intent, and extracts relevant content from the target site.
3. **Generation** — The AI engine generates a custom landing page aligned with the ad's promise, applying CRO best practices.
4. **Deploy & Track** — The page goes live, and performance is tracked on the analytics dashboard for ongoing optimization.

---

## 🔧 Installation

### Prerequisites
- Python 3.10+
- pip
- An OpenAI API key
- A Supabase project (or PostgreSQL instance)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/shauryasjadaunnn12345/AdSync-AI.git
cd AdSync-AI

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
OPENAI_API_KEY=your-openai-api-key
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
DATABASE_URL=postgres://user:password@localhost:5432/adsyncai
```

---

## 📂 Project Structure

```
AdSync-AI/
│
├── core/                  # Landing page generation logic
├── ads/                   # Ad creative analysis
├── analytics/             # Dashboard & tracking
├── blog/                  # Blog management system
├── chatbot/               # AI chatbot integration
├── static/                # CSS, JS, assets
├── templates/              # HTML templates
├── requirements.txt
└── manage.py
```

> Adjust this tree to match your actual repo layout.

---

## 🗺 Roadmap

- [ ] A/B testing between generated page variants
- [ ] Multi-language landing page generation
- [ ] Direct ad-platform integrations (Meta Ads, Google Ads)
- [ ] Template library for faster generation
- [ ] Team collaboration & workspace support
- [ ] Advanced CRO scoring per generated page

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Support

Found a bug or have a feature request? [Open an issue](https://github.com/shauryasjadaunnn12345/AdSync-AI/issues).

<p align="center">Made with ❤️ by <a href="https://github.com/shauryasjadaunnn12345">Shaurya</a></p>
