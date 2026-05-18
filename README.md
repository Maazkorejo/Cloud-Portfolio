# Muhammad Maaz — Cloud Portfolio
### Cloud Computing Final Project | PRD v1.0 | May 2026

> A fully deployed personal portfolio platform built on a multi-cloud architecture — Flask backend, Neon PostgreSQL database, and Railway hosting — all at **$0 cost**.

---

## 🌐 Live Demo

cloud-portfolio-production-f02c.up.railway.app

---

## ✅ Project Status

| Phase | Task | Status |
|-------|------|--------|
| Phase 1 | Frontend — HTML/CSS/JS portfolio | ✅ Complete |
| Phase 2 | Flask backend + Neon PostgreSQL | ✅ Complete |
| Phase 3 | Railway deployment + auto-deploy | ✅ Complete |

---

## 📁 Folder Structure

```
Cloud-Portfolio/
│
├── index.html              ← Main portfolio page (FR-01 to FR-10)
├── app.py                  ← Flask backend — routes, contact form, DB
├── requirements.txt        ← Python dependencies
├── schema.sql              ← PostgreSQL table schema (run once on Neon)
├── README.md               ← This file
├── .env                    ← Environment variables (NOT committed)
├── .gitignore              ← Excludes .env and cache files
│
└── static/
    ├── css/
    │   └── style.css       ← Full stylesheet (dark/light mode, responsive)
    └── js/
        └── main.js         ← Scroll animations, theme toggle, contact form
```

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | HTML5, CSS3, JavaScript | Portfolio UI |
| Backend | Python Flask + Gunicorn | API routes, contact form |
| Database | Neon PostgreSQL (Free Tier) | Contact form submissions |
| Hosting | Railway (Free Tier) | Cloud deployment |
| Version Control | GitHub | Source code + auto-deploy trigger |

---

## ⚙️ Features

- **FR-01** — Hero section with name, title, CTA buttons
- **FR-02** — About section with bio, skills, meta info
- **FR-03** — Projects section (4 projects with GitHub links)
- **FR-04** — Contact form (name, email, message)
- **FR-05** — Contact form saves to PostgreSQL database
- **FR-06** — Fully responsive (mobile + desktop)
- **FR-07** — CV download button
- **FR-08** — GitHub + LinkedIn social links
- **FR-09** — Certifications section (12 credentials)
- **FR-10** — Dark/Light mode toggle

---

## 🚀 Deployment

This project auto-deploys to Railway on every push to `main`.

### Run locally

```bash
# 1. Clone the repo
git clone https://github.com/Maazkorejo/Cloud-Portfolio.git
cd Cloud-Portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
# Add your DATABASE_URL and ADMIN_KEY

# 4. Run Flask
python app.py
```

Open `http://localhost:5000` in your browser.

### Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | Neon PostgreSQL connection string |
| `ADMIN_KEY` | Secret key to access `/contacts` endpoint |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the portfolio page |
| POST | `/contact` | Saves contact form to database |
| GET | `/contacts?key=ADMIN_KEY` | View all submissions (admin) |
| GET | `/health` | Health check endpoint |

---

## 👨‍💻 Author

**Muhammad Maaz**
- Email: maazkorejo00@gmail.com
- GitHub: [github.com/Maazkorejo](https://github.com/Maazkorejo)
- LinkedIn: [linkedin.com/in/maazkorejo](https://linkedin.com/in/maazkorejo)
- Portfolio: [my-portfolio-gray-tau-42.vercel.app](https://my-portfolio-gray-tau-42.vercel.app)

---

*Cloud Computing Final Project | University of Sindh | Instructor: Abdullah Amin*
