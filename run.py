from app import create_app

# Create the Flask app
# This is the same as app = Flask(__name__)
app = create_app()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
