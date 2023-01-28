from routes import blp
from extensions import app


# This function creates the Flask app and registers the Blueprint
def create_app():
    # Register the Blueprint
    app.register_blueprint(blp)
    # Return the app
    return app
