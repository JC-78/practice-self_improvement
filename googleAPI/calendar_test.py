import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google Calendar API Scope (Modify scope if you need more permissions)
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_credentials():
    """Authenticate and get credentials for Google Calendar API."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds

def create_event(service, summary, location, description, start_time, end_time):
    """Creates an event and adds it to Google Calendar."""
    event = {
        "summary": summary,
        "location": location,
        "description": description,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "America/New_York",
        },
        "reminders": {
            "useDefault": True,
        },
    }

    try:
        event_result = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created successfully! Event ID: {event_result['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

def main():
    """Main function to authenticate and create an event."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    # Get event details from user
    summary = input("Enter event title: ")
    location = input("Enter event location: ")
    description = input("Enter event description: ")

    # Get start and end time
    start_str = input("Enter event start time (YYYY-MM-DD HH:MM): ")
    end_str = input("Enter event end time (YYYY-MM-DD HH:MM): ")

    start_time = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    end_time = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")

    # Create the event
    create_event(service, summary, location, description, start_time, end_time)

if __name__ == "__main__":
    main()
