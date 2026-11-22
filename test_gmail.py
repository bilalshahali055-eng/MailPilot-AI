
from gmail_service import get_recent_emails

emails = get_recent_emails()

for email in emails:
    print("From:", email["from"])
    print("Subject:", email["subject"])
    print("Date:", email["date"])
    print("-" * 40)

