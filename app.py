from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Success!</h1><p>Your Azure Free Tier App is running via GitHub Actions.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
