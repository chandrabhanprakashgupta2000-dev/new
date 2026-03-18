from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Success hai!</h1><p>naya wala Azure Free! is running via GitHub Actions.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
