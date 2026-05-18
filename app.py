# ─────────────────────────────────────────────────────────────
#  app.py — Muhammad Maaz Portfolio Flask Backend
#  Cloud Computing Final Project | PRD v1.0
#  Handles: static file serving, contact form, DB integration
# ─────────────────────────────────────────────────────────────

from flask import Flask, request, jsonify, render_template, send_from_directory
import psycopg2
import os
import re
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='.')

# ── Database connection helper ─────────────────────────────────
def get_db_connection():
    """Create and return a new database connection using DATABASE_URL from .env"""
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise Exception("DATABASE_URL not set in .env file")
    conn = psycopg2.connect(database_url)
    return conn


# ── Database initialisation ────────────────────────────────────
def init_db():
    """Create the contacts table if it doesn't exist yet."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id          SERIAL PRIMARY KEY,
                name        VARCHAR(100) NOT NULL,
                email       VARCHAR(150) NOT NULL,
                message     TEXT NOT NULL,
                submitted_at TIMESTAMP DEFAULT NOW()
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("✓ Database initialised — contacts table ready.")
    except Exception as e:
        print(f"✗ Database init failed: {e}")
        print("  → Running without DB. Contact form will log to console only.")


# ── Routes ─────────────────────────────────────────────────────

@app.route('/')
def index():
    """Serve the main portfolio page."""
    return send_from_directory('.', 'index.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS, images)."""
    return send_from_directory('static', filename)


@app.route('/contact', methods=['POST'])
def contact():
    """
    Handle contact form submissions.
    Expects JSON: { name, email, message }
    Saves to PostgreSQL contacts table.
    """
    try:
        data = request.get_json()

        # ── Validate input ─────────────────────────────────────
        if not data:
            return jsonify({'status': 'error', 'message': 'No data received'}), 400

        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

        if len(name) > 100:
            return jsonify({'status': 'error', 'message': 'Name too long (max 100 chars)'}), 400

        if len(message) > 5000:
            return jsonify({'status': 'error', 'message': 'Message too long (max 5000 chars)'}), 400

        # Basic email format check
        email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_pattern, email):
            return jsonify({'status': 'error', 'message': 'Invalid email address'}), 400

        # ── Save to database ───────────────────────────────────
        conn = get_db_connection()
        cur  = conn.cursor()
        cur.execute(
            'INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)',
            (name, email, message)
        )
        conn.commit()
        cur.close()
        conn.close()

        print(f"[{datetime.now()}] New contact: {name} <{email}>")
        return jsonify({'status': 'success', 'message': 'Message received!'}), 200

    except psycopg2.Error as db_err:
        # Database error — log it, still return a user-friendly response
        print(f"DB Error: {db_err}")
        return jsonify({'status': 'error', 'message': 'Database error. Please try again.'}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': 'Server error. Please try again.'}), 500


@app.route('/contacts', methods=['GET'])
def view_contacts():
    """
    View all contact form submissions.
    Protected by a simple secret key check.
    Usage: GET /contacts?key=YOUR_ADMIN_KEY
    """
    admin_key = os.getenv('ADMIN_KEY', '')
    provided_key = request.args.get('key', '')

    if not admin_key or provided_key != admin_key:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    try:
        conn = get_db_connection()
        cur  = conn.cursor()
        cur.execute('SELECT id, name, email, message, submitted_at FROM contacts ORDER BY submitted_at DESC')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        contacts = [
            {
                'id':           row[0],
                'name':         row[1],
                'email':        row[2],
                'message':      row[3],
                'submitted_at': str(row[4])
            }
            for row in rows
        ]
        return jsonify({'status': 'success', 'count': len(contacts), 'contacts': contacts}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': 'Could not fetch contacts'}), 500


@app.route('/health')
def health():
    """Health check endpoint — used by UptimeRobot monitoring."""
    return jsonify({'status': 'ok', 'app': 'Muhammad Maaz Portfolio'}), 200


# ── App startup ─────────────────────────────────────────────────
if __name__ == '__main__':
    init_db()  # Create table on first run
    app.run(host='0.0.0.0', port=5000, debug=False)