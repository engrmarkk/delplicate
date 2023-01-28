from extensions import blp
from flask import render_template


# This is the route for the index page
@blp.route('/')
def index():
    # Render the index.html template
    return render_template("index.html")
