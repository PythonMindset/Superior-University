from flask import Flask, render_template, request, url_for
import os
from color_detector import extract

app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    colors=None
    image_path=None
    if request.method=="POST":
        if 'image' in request.files:
            file=request.files['image']
            if file.filename!="":
                image_path=os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(image_path)
                colors=extract(image_path)
                image_path=url_for('static', filename='uploads/' + file.filename)
    return render_template("index.html", colors=colors, image=image_path)

if __name__ == "__main__":
    app.run(debug=True)
