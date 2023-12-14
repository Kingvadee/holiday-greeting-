# holiday_greetings.py
from flask import Flask, render_template, request
from art import *
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_name = request.form.get("name")
    holiday_theme = get_random_holiday_theme()
    greeting_text = f"Happy {holiday_theme}, {user_name}!"
    greeting_art = text2art(greeting_text)
    return render_template("index.html", greeting=greeting_art)

def get_random_holiday_theme():
    holiday_themes = ["Christmas"]
    return random.choice(holiday_themes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

