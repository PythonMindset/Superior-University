from flask import Flask,render_template,request
from bot import chatbot

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat_route():
    user_input=request.json.get("message")
    response=chatbot.respond(user_input)
    if not response:
        response="I'm not sure how to respond to that. Try asking for a study plan, motivation, or focus tips."
    return response

if __name__ == "__main__":
    app.run(debug=True)
