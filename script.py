import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 465
EMAIL_SERVER = "smtp.gmail.com"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.environ.get("EMAIL")
password_email = os.environ.get("PASSWORD")

def send_email(subject, receiver_email, Name, Preferred_Date, Preferred_Time):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Gynoveda", f"{sender_email}"))
    msg["To"] = receiver_email

    msg.set_content(
        f"""\
        Hi {Name},
        I hope you are well.
        I just wanted to drop you a quick note to remind you that your appointment is scheduled for {Preferred_Date} at {Preferred_Time} with Gynoveda.
        If you are not available, you could change your appointment date and time here.
        Hope to have a great session with you.
        Best regards
        Aditya Das
        """
    )
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {Name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that your appointment is scheduled for <strong>{Preferred_Date}</strong> at <strong>{Preferred_Time}</strong> with Gynoveda.</p>
        <p>If you are not available, you could change your appointment date and time <a href="https://docs.google.com/forms/d/e/1FAIpQLSeCMq920gHdgKCMVJbvr1Nwmjpq4Tj6oZE8BPWmC0OTb6-iDA/viewform?usp=sf_link">here</a>.</p>
        <p>Hope to have a great session with you.</p>
        <p>Best regards</p>
        <p>Aditya Das</p>
      </body>
    </html>
    """,
        subtype="html",
    )
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL_SERVER, PORT, context=context) as smtp_server:
        smtp_server.login(sender_email, password_email)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())



def send_email_hourly(subject, receiver_email, Name):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Gynoveda", f"{sender_email}"))
    msg["To"] = receiver_email

    msg.set_content(
        f"""\
        Hi {Name},
        We hope you had a great session with us.
        Please do fill our survey and help us know about your experience with us so that we can improve, it would only take a minute.
        Thanks for choosing us.
        Best regards
        Aditya Das
        """
    )
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {Name},</p>
        <p>We hope you had a great session with us.</p>
        <p>Please do fill our <a href="https://docs.google.com/forms/d/e/1FAIpQLSeCMq920gHdgKCMVJbvr1Nwmjpq4Tj6oZE8BPWmC0OTb6-iDA/viewform?usp=sf_link">survey</a> and help us know about your experience with us so that we can improve, it would only take a minute.</p>
        <p>Thanks for choosing us.</p>
        <p>Best regards</p>
        <p>Aditya Das</p>
      </body>
    </html>
    """,
        subtype="html",
    )
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL_SERVER, PORT, context=context) as smtp_server:
        smtp_server.login(sender_email, password_email)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
