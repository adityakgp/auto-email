from datetime import date, timedelta
import pandas as pd
from script import send_email

SHEET_ID='19opmWWe1XWSJoOo6MYEp5WsrtOo2nusPO3VW_65lMCQ'
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?gid=913445633&format=csv"

def load_df(url):
    parse_dates = ["Preferred_Date", "Preferred_Time"]
    df = pd.read_csv(url, parse_dates=parse_dates, dayfirst=True)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present+timedelta(days=3) == row["Preferred_Date"].date()):
            send_email(
                subject=f'Reminder for your appointment',
                receiver_email=row["Email_Address"],
                Name=row["Name"],
                Preferred_Date=row["Preferred_Date"].strftime("%d, %b %Y"),
                Preferred_Time=row["Preferred_Time"].strftime("%I %p"),
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)
# @app.lib.cron()
# def cron_job(event):
#     df = load_df(URL)
#     result = query_data_and_send_emails(df)
#     return result