import os
from flask import Flask
from app.routes import home_bp
import secrets
print(secrets.token_hex(16))  # Generates a secure random 32-character string


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key')

# Initialize the Flask app
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Register the blueprint
app.register_blueprint(home_bp, url_prefix='/')  # Register with '/' as the base URL

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode
