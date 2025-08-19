from flask import Flask, request, jsonify
from app.reviewer import analyze_code
from app.github_integration import process_github_event

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"message": "AI Code Reviewer API is running 🚀"}

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Input: { "code": "def add(a,b): return a+b" }
    Output: JSON with issues and AI suggestions
    """
    data = request.get_json()
    code = data.get("code", "")
    result = analyze_code(code)
    return jsonify(result)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    """
    GitHub webhook for pull requests.
    """
    event = request.get_json()
    response = process_github_event(event)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
