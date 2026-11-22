
# 📧 MailPilot AI
### AI-Powered Email Management Assistant

**Stanford Code in Place X — Final Project**

MailPilot AI is an AI-powered email management web application
developed using Python and Flask.

The application helps users manage their Gmail inbox more
efficiently using artificial intelligence.

It can summarize emails, generate professional email replies,
and provide assistance through Google Gemini AI.

---

## 👨‍💻 Developer Information

**Full Name:** Bilal Shah

**University:** HITEC University, Taxila, Pakistan

**Department:** Software Engineering

**Email:** bilalshahali055@gmail.com

**Project:** MailPilot AI

**Program:** Stanford Code in Place X

---

## 🎯 Project Objective

The main objective of MailPilot AI is to make email management
easier, faster, and more efficient.

Reading multiple emails and writing replies can take time.

MailPilot AI uses artificial intelligence to help users
understand their emails and prepare professional replies.

---

## 🚀 Main Features

### 1. Gmail Integration
- Connects to Gmail using Google OAuth 2.0.
- Retrieves recent inbox emails.
- Displays sender, subject, date, and email preview.

### 2. AI Email Summarization
- Uses Google Gemini AI.
- Summarizes recent emails.
- Highlights important information and possible actions.

### 3. AI Email Reply Generator
- Generates professional email reply drafts.
- Allows users to edit generated replies.
- Includes a Copy Reply button.
- Does not automatically send emails.

### 4. Gemini AI Assistant
- Allows users to ask questions.
- Helps draft professional emails.
- Provides AI-generated responses.

### 5. Hybrid Dashboard
- Modern dashboard interface.
- Dark sidebar with a light main content area.
- Responsive layout.
- Easy navigation between features.

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Google Gmail API
- Google Gemini API
- Google OAuth 2.0
- Git and GitHub
- Visual Studio Code

---

## 📁 Project Structure

    MailPilot-AI/
    |
    |-- app.py
    |-- gmail_service.py
    |-- requirements.txt
    |-- README.md
    |-- .gitignore
    |
    |-- templates/
    |   |-- index.html
    |
    |-- static/
        |-- style.css

Private configuration files such as .env, credentials.json,
and token.json are stored locally and excluded from GitHub.

---

## 🌐 Important: Website Access

**MailPilot AI is currently a locally hosted Flask application.**

It has not yet been deployed to a public hosting platform.

The dashboard is available at:

http://127.0.0.1:5000

This address only works on the computer where the Flask
application is running.

### Important Notes

- The Flask server must be running before opening the dashboard.
- The localhost address is not a public website.
- GitHub stores the project source code but does not host
  the running Flask application.
- Stanford reviewers cannot open my local dashboard
  directly from their own computers.
- Reviewers can download the source code and run it
  locally after configuring their own API credentials.

A public deployment may be added in the future.

---

## ⚙️ Installation and Setup

### Step 1: Clone the GitHub Repository

    git clone https://github.com/bilalshahali055-eng/MailPilot-AI.git

### Step 2: Open the Project Directory

    cd MailPilot-AI

### Step 3: Create a Virtual Environment

    python -m venv .venv

### Step 4: Activate the Virtual Environment

On Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

### Step 5: Install Required Libraries

    pip install -r requirements.txt

### Step 6: Configure Gemini API

Create a file named .env in the main project folder.

Add the following:

    GEMINI_API_KEY=your_own_gemini_api_key

Replace the placeholder with your own Gemini API key.

### Step 7: Configure Gmail API

1. Open Google Cloud Console.
2. Create or select a Google Cloud project.
3. Enable the Gmail API.
4. Configure the OAuth consent screen.
5. Create OAuth credentials for a desktop application.
6. Download the OAuth client credentials.
7. Rename the downloaded file to credentials.json.
8. Place credentials.json in the project folder.
9. Add your Google account as a test user if required.

The first Gmail connection may open a browser window
to request authorization.

### Step 8: Run the Flask Application

    python app.py

The terminal should display an address similar to:

    http://127.0.0.1:5000

### Step 9: Open the Dashboard

Open Google Chrome or another web browser.

Enter:

http://127.0.0.1:5000

The MailPilot AI dashboard should appear.

Keep the Flask terminal running while using the application.

To stop the server, press Ctrl+C in the terminal.

---

## 🔒 Security and Privacy

MailPilot AI uses Gmail OAuth 2.0 authentication.

The application currently requests read-only Gmail access.

It cannot automatically send emails.

The following files must never be uploaded publicly:

- .env
- credentials.json
- token.json
- .venv/

Email sender details, subjects, and previews are shared
with Gemini when the user requests AI email processing.

Users should review AI-generated replies before using them.

---

## 🧠 Challenges Faced

During development, I encountered several challenges:

1. Connecting Python with the Gmail API.
2. Configuring Google OAuth authentication.
3. Integrating Google Gemini AI with Flask.
4. Connecting JavaScript buttons to Flask backend routes.
5. Debugging the AI Email Reply Generator.
6. Designing and improving the dashboard interface.

I worked through these challenges by testing,
debugging, and improving my code step by step.

---

## 📚 What I Learned

Through this project, I learned:

- How to develop a web application using Python.
- How Flask handles web requests and routes.
- How to work with external APIs.
- How OAuth authentication works.
- How to integrate artificial intelligence into applications.
- How Python communicates with HTML and JavaScript.
- How to debug errors in a web application.
- How to organize and publish a project on GitHub.

---

## 🎓 Stanford Code in Place X

I developed MailPilot AI as part of my Python learning
journey and am presenting it as my Stanford Code in Place X
final project.

This project helped me apply programming concepts to
a practical, real-world application.

---

## 🔗 GitHub Repository

https://github.com/bilalshahali055-eng/MailPilot-AI

---

## 📬 Contact

**Bilal Shah**

Software Engineering Student

HITEC University, Taxila, Pakistan

Email: bilalshahali055@gmail.com

GitHub: https://github.com/bilalshahali055-eng

---

## 📌 Project Status

**Development Status:** Completed

**Main Features:** Working

**Hosting:** Local Flask Server

**Public Deployment:** Not yet available

**Final Project:** Stanford Code in Place X
