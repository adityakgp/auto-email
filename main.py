from datetime import date, timedelta, datetime
import pandas as pd
from script import send_email
import pytz

ist = pytz.timezone('Asia/Kolkata')
SHEET_ID='19opmWWe1XWSJoOo6MYEp5WsrtOo2nusPO3VW_65lMCQ'
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?gid=913445633&format=csv"

def load_df(url):
    parse_dates = ["Preferred_Date", "Preferred_Time"]
    df = pd.read_csv(url, parse_dates=parse_dates, dayfirst=True)
    return df

def query_data_and_send_emails_daily(df):
    curr = date.today()
    present_utc = datetime.combine(curr, datetime.min.time()).replace(tzinfo=pytz.utc)
    present_ist = present_utc.astimezone(ist)
    present=present_ist.date()
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
    # return present
            

df = load_df(URL)
result = query_data_and_send_emails_daily(df)
print(result)