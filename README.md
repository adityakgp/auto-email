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
   - Checks if a customer's session has ended and sends them an email requesting a review.
   - Schedule: Runs every hour.

### Google Sheets Integration

- **Booking Form Link:** [Link to the form to book appointments]
- **Appointment Sheet:** [Link to the Google Sheet containing the appointments]

### Running Cron Jobs

To run the cron jobs, uncomment the schedule lines from the dailyemail.yml file used by GitHub Actions.

## Setup

1. Clone this repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure the Email credentials.
4. Uncomment the schedule lines in the YAML file to activate the cron jobs.
