from routes import blp
from extensions import app


# This function creates the Flask app and registers the Blueprint
def create_app():
    app.config["SECRET_KEY"] = "4f557e8e5eb51bfb7c42"
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # Register the Blueprint
    app.register_blueprint(blp)
    # Return the app
    return app
