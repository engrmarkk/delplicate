from flask import Flask, Blueprint

# Create the Flask app
app = Flask(__name__, template_folder="../templates")
# Create the Blueprint
blp = Blueprint("routes", __name__)
