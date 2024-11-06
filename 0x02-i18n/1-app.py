from flask import Flask, render_template
from flask_babel import Babel  # Use Flask-Babel, not Flask-BabelEx

app = Flask(__name__)

class Config:
    """Configuration for Flask app and Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Set up the app config
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@app.route('/')
def index():
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
