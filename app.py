# Step 1: Secrets Injection for Lab 2

import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Read secret values from environment variables
app_secret = os.getenv("APP_SECRET_KEY")
app_mode = os.getenv("APP_MODE", "production")

# Save secret in Flask config
app.config["SECRET_KEY"] = app_secret


@app.route("/health", methods=["GET"])
def health():
    # Simple endpoint to check if the app is running
    return jsonify({
        "status": "running",
        "mode": app_mode
    })


@app.route("/check-secret", methods=["GET"])
def check_secret():
    # Check whether the secret was loaded correctly
    if app_secret:
        return jsonify({
            "message": "Secret loaded successfully",
            "secret_loaded": True
        })
    else:
        return jsonify({
            "message": "Secret not found",
            "secret_loaded": False
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)