from flask import Flask, jsonify
import os
import socket
import datetime
import random

# ✅ Environment variables (AFTER import os)
VERSION = os.getenv("APP_VERSION", "v1")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    time = datetime.datetime.now()

    return f"""
    <html>
    <head>
        <title>DevOps Platform</title>
        <style>
            body {{
                background-color: #0f172a;
                color: #f1f5f9;
                font-family: Arial;
                text-align: center;
            }}
            h1 {{
                color: #38bdf8;
            }}
            .card {{
                background-color: #1e293b;
                padding: 20px;
                margin: 20px;
                border-radius: 10px;
                display: inline-block;
                width: 300px;
            }}
            button {{
                padding: 10px;
                margin-top: 10px;
                background-color: #38bdf8;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
        </style>
    </head>

    <body>

        <h1>🚀 DevOps Kubernetes Platform</h1>

        <div class="card">
            <h2>📊 System Info</h2>
            <p><b>Pod:</b> {hostname}</p>
            <p><b>Status:</b> Running</p>
            <p><b>Time:</b> {time}</p>
        </div>

        <div class="card">
            <h2>⚙️ Deployment Info</h2>
            <p><b>Version:</b> {VERSION}</p>
            <p><b>Environment:</b> {ENVIRONMENT}</p>
        </div>

        <div class="card">
            <h2>🎮 Gaming</h2>
            <p>Game servers active 🎯</p>
        </div>

        <div class="card">
            <h2>🏦 Banking</h2>
            <p>Secure payments running 💳</p>
        </div>

        <div class="card">
            <h2>📈 Metrics</h2>
            <p><b>CPU Usage:</b> {random.randint(10,90)}%</p>
            <p><b>Requests/sec:</b> {random.randint(100,1000)}</p>
        </div>

        <div class="card">
            <h2>⚠️ Testing</h2>
            <button onclick="fetch('/crash')">Simulate Failure</button>
        </div>

    </body>
    </html>
    """

# API endpoint (DevOps standard)
@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)

# Simulate failure endpoint
@app.route("/crash")
def crash():
    raise Exception("Simulated crash for testing")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
