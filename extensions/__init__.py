from flask import Flask, Blueprint

# Create the Flask app
app = Flask(__name__, static_folder='../static', template_folder='../templates')
# Create the Blueprint
blp = Blueprint("routes", __name__)
