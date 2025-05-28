from flask import Flask, render_template, request, jsonify
from bot import LanguageBot

app = Flask(__name__)
lang_bot = LanguageBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = lang_bot.handle_message(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)