import os.path
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_credentials():
    """Get user credentials from token.json or authenticate."""
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

def send_email(service, to_email, subject, message_text):
    """Sends an email via Gmail API."""
    try:
        message = MIMEText(message_text)
        message["to"] = to_email
        message["subject"] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        message_body = {"raw": raw_message}

        sent_message = service.users().messages().send(userId="me", body=message_body).execute()
        print(f"Message sent successfully! Message Id: {sent_message['id']}")

    except HttpError as error:
        print(f"An error occurred: {error}")

def main():
    """Authenticates and sends an email."""
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    # Replace these with your desired email details
    to_email = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    message_text = input("Enter message: ")

    send_email(service, to_email, subject, message_text)

if __name__ == "__main__":
    main()
