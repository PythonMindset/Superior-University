from flask import Flask,render_template
import requests

app=Flask(__name__)
URL1="https://uselessfacts.jsph.pl/api/v2/facts/random"

@app.route("/", methods=["GET"])
def index():
    response=requests.get(URL1)
    data=response.json()
    required_text=data["text"]
    return render_template('index.html',data=required_text)



if __name__ == "__main__":
    app.run(debug=True)