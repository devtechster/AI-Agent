import os
import sendgrid
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

def send_welcome_email(to):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    content = "Thanks for subscribing to Tech Digest! You'll receive daily updates starting tomorrow at 9AM."
    message = Mail(from_email=FROM_EMAIL, to_emails=to, subject="Welcome to Tech Digest!", plain_text_content=content)
    sg.send(message)

def send_daily_email(to):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    message = Mail(from_email=FROM_EMAIL, to_emails=to, subject="Hi", plain_text_content="Hi")
    sg.send(message)