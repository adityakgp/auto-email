# Email Scheduler

Email Scheduler is a script designed to automate email reminders and review requests for customers with appointments. It utilizes cron jobs to send reminders and review requests at scheduled intervals.

## Features

- Sends reminders to customers with appointments scheduled in the next 3 days.
- Sends review requests to customers after the end of their sessions.
- Integrates with Google Sheets to manage appointment schedules.

## Usage

### Cron Jobs

This project runs two cron jobs:

1. **Daily Reminder:**
   - Sends reminders to customers with appointments scheduled in the next 3 days.
   - Schedule: Runs once per day.
   
2. **Hourly Review Request:**
   - Checks if a customer's session has ended and sends them an email requesting a review (when cron running at time t it checks customers who had their appointments scheduled between t-2 and t-1, assuming a session to be 1 hour long).
   - Schedule: Runs every hour.

### Google Sheets Integration

- **Booking Form Link:** https://docs.google.com/forms/d/e/1FAIpQLSeCMq920gHdgKCMVJbvr1Nwmjpq4Tj6oZE8BPWmC0OTb6-iDA/viewform
- **Appointment Sheet:** https://docs.google.com/spreadsheets/d/19opmWWe1XWSJoOo6MYEp5WsrtOo2nusPO3VW_65lMCQ/edit?usp=sharing

### Running Cron Jobs

To run the cron jobs, uncomment the schedule lines from the dailyemail.yml file used by GitHub Actions.

## Setup

1. Clone this repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure the Email credentials.
4. Uncomment the schedule lines in the YAML file to activate the cron jobs.
