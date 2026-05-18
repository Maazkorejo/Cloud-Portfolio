# Final Project — Multi-Cloud Portfolio Platform
## Muhammad Maaz | Cloud Computing Final Project | PRD v1.0

---

## Current Folder Structure

```
FinalProject/
│
├── index.html              ← Main portfolio page (FR-01 to FR-10 complete)
├── README.md               ← This file
│
├── static/
│   ├── css/
│   │   └── style.css       ← Full stylesheet (dark/light mode, responsive)
│   ├── js/
│   │   └── main.js         ← Interactions, form, theme, scroll animations
│   └── images/             ← Add your profile photo or project screenshots here
│
└── [NEXT STEPS — coming soon]
    ├── app.py              ← Flask backend (Phase 2)
    ├── requirements.txt    ← Python dependencies (Phase 2)
    ├── .env                ← Environment variables — DO NOT commit (Phase 2)
    └── .github/
        └── workflows/
            └── deploy.yml  ← GitHub Actions CI/CD (Phase 3)
```

---

## Phase 1: Frontend (DONE ✓)
- Home/Hero section with name, title, CTA buttons
- About section with bio, meta info, availability status
- Skills section (6 skill cards covering all technologies)
- Projects section (3 projects, featured card for the main project)
- Certifications section
- Contact section with form
- Dark/Light mode toggle
- Responsive design (mobile + desktop)
- Smooth scroll + scroll reveal animations

## Phase 2: Flask Backend (NEXT)
- app.py with Flask routes
- /contact POST endpoint saving to PostgreSQL
- Neon.tech database integration
- .env configuration
- Gunicorn setup
- systemd service file

## Phase 3: CI/CD & Deployment (NEXT)
- GitHub Actions deploy.yml
- Oracle Cloud VM setup guide
- Nginx config file
- SSL/HTTPS with Certbot

---

*To preview the frontend locally: just open index.html in your browser.*
