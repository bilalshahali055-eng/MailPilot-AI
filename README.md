
# MailPilot AI 📧

### AI-Powered Email Management Assistant

MailPilot AI is a Python-based web application that
makes email management easier using artificial intelligence.

I developed this project as part of my learning journey
with Stanford Code in Place.

## 🚀 Features

- Gmail Integration: Connect to Gmail and view recent emails.
- AI Email Summarization: Summarize recent emails using Gemini AI.
- AI Reply Generator: Generate professional email reply drafts.
- AI Chat Assistant: Ask questions and get AI-powered responses.
- Editable Replies: Edit and copy generated replies.
- Hybrid Dashboard: Modern and user-friendly interface.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Gmail API
- Google Gemini API
- Google OAuth 2.0

## 📁 Project Structure

MailPilot-AI/
│
├── app.py
├── gmail_service.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/bilalshahali055-eng/MailPilot-AI.git

### 2. Open the project folder

cd MailPilot-AI

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the virtual environment (Windows)

.venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Configure API credentials

Create a .env file in the project folder.

Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

Set up Gmail API OAuth credentials in Google Cloud
and save the downloaded OAuth client configuration
as credentials.json in the project folder.

Never upload your API keys, credentials.json,
or token.json to GitHub.

### 7. Run the application

python app.py

### 8. Open the dashboard

Visit:

http://127.0.0.1:5000

## 🔒 Security

- Gmail access uses OAuth 2.0.
- Gmail integration is read-only.
- AI-generated replies are drafts and are not sent automatically.
- API keys and authentication files are kept private.
- Email previews are sent to Gemini when using AI email features.

## 🎯 Project Goal

My goal was to build a practical Python application
that solves a real-world problem.

Managing multiple emails can be time-consuming.
MailPilot AI helps users understand their emails
and prepare replies more efficiently.

## 📚 What I Learned

While developing this project, I learned:

- How to build web applications using Python and Flask.
- How to integrate external APIs.
- How Gmail OAuth authentication works.
- How to use Gemini AI in a Python application.
- How to connect Python with HTML, CSS, and JavaScript.
- How to debug errors and improve application functionality.

## 👨‍💻 Developer

Bilal Shah

Software Engineering Student

Stanford Code in Place X — Final Project

## 🔗 GitHub Repository

https://github.com/bilalshahali055-eng/MailPilot-AI
