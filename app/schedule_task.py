import sqlite3
from email_utils import send_daily_email

DB_FILE = "subscribers.db"

def send_daily_to_all():
    with sqlite3.connect(DB_FILE) as conn:
        emails = conn.execute("SELECT email FROM subscribers").fetchall()
        for (email,) in emails:
            send_daily_email(email)

if __name__ == '__main__':
    send_daily_to_all()