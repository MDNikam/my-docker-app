
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My First Docker App 🚀</h1>
    <p>Hello! My application is running inside Docker via Webhook.</p>
    <p>Deployed successfully by a DevOps Engineer!</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
