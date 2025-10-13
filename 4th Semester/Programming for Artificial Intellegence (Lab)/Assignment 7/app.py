from flask import Flask,render_template
import requests

app=Flask(__name__)
URL="https://zenquotes.io/api/random"

@app.route("/", methods=["GET"])
def index():
    response=requests.get(URL)
    data=response.json()[0]
    quote=data['q']
    return render_template('index.html', quote=quote)


if __name__ == "__main__":
    app.run(debug=True)