from datetime import datetime, timedelta
import pandas as pd
from script import send_email_hourly

SHEET_ID='19opmWWe1XWSJoOo6MYEp5WsrtOo2nusPO3VW_65lMCQ'
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?gid=913445633&format=csv"

def load_df(url):
    parse_dates = ["Preferred_Date", "Preferred_Time"]
    df = pd.read_csv(url, parse_dates=parse_dates, dayfirst=True)
    return df

def query_data_and_send_emails_daily(df):
    present = datetime.now()
    t1=present-timedelta(hours=1)
    t2=present-timedelta(hours=2)
    email_counter = 0
    for _, row in df.iterrows():
        if (t2<row["Preferred_Time"]<t1):
            send_email_hourly(
                subject=f'Rate us',
                receiver_email=row["Email_Address"],
                Name=row["Name"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL)
result = query_data_and_send_emails_daily(df)
print(result)