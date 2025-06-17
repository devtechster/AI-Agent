from flask import Flask, render_template, request, redirect, flash
from email_utils import send_welcome_email
from articles import ARTICLES
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

DB_FILE = "subscribers.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS subscribers (email TEXT UNIQUE)")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            with sqlite3.connect(DB_FILE) as conn:
                try:
                    conn.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
                    send_welcome_email(email)
                    flash("Subscribed successfully! Check your inbox.")
                except sqlite3.IntegrityError:
                    flash("You're already subscribed.")
    return render_template('index.html', articles=ARTICLES)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
