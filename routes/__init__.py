from extensions import blp
from flask import render_template, redirect, request, url_for, flash
import os
import random


# This is the route for the index page
@blp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "fileInput" in request.files:
            random_num = random.randint(0000, 9999)
            image = request.files["fileInput"]
            if image.filename != '':
                image.save(os.path.join("static\\images", image.filename))
                return redirect(url_for("routes.display", img=image.filename,
                                        num=random_num))
            flash("Nothing to upload", "danger")
    # Render the index.html template
    return render_template("index.html")


@blp.route("/display/<img>/<num>")
def display(img, num):
    return render_template("display.html", img=img)
