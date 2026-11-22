
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

# Gmail read-only permission
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


# Connect to Gmail
def connect_gmail():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    return service


# Get recent inbox emails
def get_recent_emails(max_results=10):
    service = connect_gmail()

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results,
        labelIds=["INBOX"]
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for message in messages:
        email = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()

        headers = email.get("payload", {}).get("headers", [])

        details = {
            header["name"].lower(): header["value"]
            for header in headers
        }

        emails.append({
            "id": message["id"],
            "from": details.get("from", "Unknown"),
            "subject": details.get("subject", "No Subject"),
            "date": details.get("date", ""),
            "snippet": email.get("snippet", "")
        })

    return emails


# Test Gmail connection
if __name__ == "__main__":
    gmail = connect_gmail()

    profile = gmail.users().getProfile(
        userId="me"
    ).execute()

    print("Gmail connected successfully!")
    print("Email:", profile["emailAddress"])
