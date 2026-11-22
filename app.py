
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

# Load Gemini API key
load_dotenv(override=True)

app = Flask(__name__)

# Connect to Gemini
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask_agent():
    user_message = (request.json or {}).get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    if client is None:
        return jsonify({"reply": "Gemini API key is missing."})

    try:
        response = client.models.generate_content(
         model="gemini-3.5-flash-lite",
         contents=user_message
        )
        

        return jsonify({
            "reply": response.text or "No response generated."
        })

    except Exception as e:
        print("Gemini Error:", e)
        return jsonify({
            "reply": "Error! Check the terminal."
        })


if __name__ == "__main__":
    app.run(debug=True)
