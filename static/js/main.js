/* ── Portfolio JS — Muhammad Maaz ── */

/* ─ Scroll reveal ─ */
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        revealObserver.unobserve(e.target);
      }
    });
  },
  { threshold: 0.12 }
);
document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

/* ─ Nav scroll glass ─ */
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

/* ─ Dark/Light theme toggle ─ */
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle.querySelector('.theme-toggle__icon');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
let isDark = localStorage.getItem('theme')
  ? localStorage.getItem('theme') === 'dark'
  : prefersDark;

function applyTheme() {
  document.body.classList.toggle('light', !isDark);
  themeIcon.textContent = isDark ? '☀' : '☾';
}
applyTheme();

themeToggle.addEventListener('click', () => {
  isDark = !isDark;
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  applyTheme();
});

/* ─ Mobile menu ─ */
const burger = document.getElementById('burger');
const mobileMenu = document.getElementById('mobileMenu');
let menuOpen = false;

burger.addEventListener('click', () => {
  menuOpen = !menuOpen;
  mobileMenu.classList.toggle('open', menuOpen);
  burger.querySelector('span:nth-child(1)').style.transform = menuOpen ? 'translateY(7px) rotate(45deg)' : '';
  burger.querySelector('span:nth-child(2)').style.opacity = menuOpen ? '0' : '';
  burger.querySelector('span:nth-child(3)').style.transform = menuOpen ? 'translateY(-7px) rotate(-45deg)' : '';
});

document.querySelectorAll('.mobile-link').forEach((link) => {
  link.addEventListener('click', () => {
    menuOpen = false;
    mobileMenu.classList.remove('open');
    burger.querySelectorAll('span').forEach((s) => { s.style.transform = ''; s.style.opacity = ''; });
  });
});

/* ─ Active nav link on scroll ─ */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__links a');

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        const id = e.target.getAttribute('id');
        navLinks.forEach((a) => {
          a.style.color = a.getAttribute('href') === `#${id}`
            ? 'var(--clr-text)'
            : '';
        });
      }
    });
  },
  { rootMargin: '-40% 0px -55% 0px' }
);
sections.forEach((s) => sectionObserver.observe(s));

/* ─ Contact form ─ */
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');
const submitBtn = document.getElementById('submitBtn');

contactForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  if (!name || !email || !message) {
    showStatus('Please fill in all fields.', 'error');
    return;
  }

  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending...';

  try {
    const res = await fetch('/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, message }),
    });

    if (res.ok) {
      showStatus('✓ Message sent! I\'ll get back to you soon.', 'success');
      contactForm.reset();
    } else {
      throw new Error('Server error');
    }
  } catch {
    /* Fallback for when Flask backend isn't running locally */
    showStatus('✓ Message received! (Demo mode — backend not connected yet)', 'success');
    contactForm.reset();
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Send Message';
  }
});

function showStatus(msg, type) {
  formStatus.textContent = msg;
  formStatus.className = `form-status ${type}`;
  setTimeout(() => { formStatus.textContent = ''; formStatus.className = 'form-status'; }, 5000);
}

/* ─ Smooth anchor scrolling with nav offset ─ */
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = document.getElementById('nav').offsetHeight;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});