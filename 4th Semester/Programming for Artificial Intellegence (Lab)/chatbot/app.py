from flask import Flask, render_template, request
from model import get_similar_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results=None
    query=""
    message=""
    if request.method=="POST":
        query=request.form.get("query")
        if query:
            results=get_similar_news(query)
            if not results:
                message="No news found for your query. Please try different keywords."
    return render_template("index.html",results=results,query=query,message=message)

if __name__ == "__main__":
    app.run(debug=True)