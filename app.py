from flask import Flask, jsonify, request
import socket, datetime, random

app = Flask(__name__)

logs_data = []

def add_log(msg):
    t = datetime.datetime.now().strftime("%H:%M:%S")
    logs_data.insert(0, f"[{t}] {msg}")

# ✅ LOGIN ROUTE
@app.route("/login_inline", methods=["POST"])
def login_inline():
    username = request.form.get("username")
    password = request.form.get("password")

    role = "guest"

    if username == "admin" and password == "admin":
        role = "admin"
    elif username == "user" and password == "user":
        role = "user"

    return jsonify({"role": role})

@app.route("/restart_service")
def restart():
    add_log("Service restarted ✅")
    return jsonify({"status": "ok"})

@app.route("/scale_service")
def scale():
    add_log("Scaling triggered 🚀")
    return jsonify({"status": "ok"})

@app.route("/security_alert")
def alert():
    add_log("Security alert ⚠️")
    return jsonify({"status": "ok"})

@app.route("/logs")
def logs():
    return jsonify({"logs": logs_data})

@app.route("/")
def home():
    host = socket.gethostname()
    time = datetime.datetime.now()

    return f"""
<html>
<head>
<title>Roosevelt Emac Operations Console</title>

<style>

/* 🌌 BACKGROUND */
body {{
font-family:Segoe UI;
margin:0;
background:
 radial-gradient(circle at 20% 20%, #1e3a8a, transparent 50%),
 radial-gradient(circle at 80% 80%, #0ea5e9, transparent 50%),
 linear-gradient(135deg, #020617, #0f172a);
color:white;
}}

/* NAV BAR (TOP) */
.nav {{
display:flex;
justify-content:space-between;
align-items:center;
padding:12px 20px;
background:rgba(2,6,23,0.85);
backdrop-filter: blur(10px);
border-bottom:1px solid rgba(255,255,255,0.1);
}}

.brand {{
display:flex;
align-items:center;
font-weight:bold;
font-size:18px;
gap:10px;
}}

.logo {{
width:32px;
height:32px;
background:#38bdf8;
border-radius:8px;
display:flex;
align-items:center;
justify-content:center;
font-weight:bold;
color:black;
}}

.nav-links a {{
margin:10px;
cursor:pointer;
color:#38bdf8;
font-weight:bold;
}}

.user {{
display:flex;
align-items:center;
gap:10px;
}}

.avatar {{
width:30px;
height:30px;
border-radius:50%;
background:#38bdf8;
display:flex;
align-items:center;
justify-content:center;
color:black;
font-weight:bold;
}}

.container {{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:20px;
padding:20px;
}}

.card {{
background: rgba(255,255,255,0.05);
backdrop-filter: blur(15px);
padding:20px;
border-radius:15px;
transition:0.3s;
box-shadow:0 4px 15px rgba(0,0,0,0.3);
}}

.card:hover {{
transform:scale(1.05);
}}

button {{
padding:10px;
margin:5px;
border:none;
border-radius:10px;
background:#38bdf8;
cursor:pointer;
}}

button:hover {{
background:#0284c7;
}}

.status-green {{
color:#22c55e;
font-weight:bold;
animation:blink 1s infinite;
}}

.status-red {{
color:#ef4444;
font-weight:bold;
animation:blink 1s infinite;
}}

@keyframes blink {{
0%{{opacity:1}}
50%{{opacity:0.4}}
100%{{opacity:1}}
}}

h2 {{
text-align:center;
}}

.service {{
background:#1e293b;
padding:10px;
margin:10px 0;
border-radius:10px;
cursor:pointer;
}}

</style>
</head>

<body>

<!-- NAVBAR -->
<div class="nav">

<div class="brand">
<div class="logo">R</div>
Roosevelt Emac
</div>

<div class="nav-links">
<a onclick="show('dashboard')">Dashboard</a>
<a onclick="show('services')">Services</a>
<a onclick="show('monitor')">Monitoring</a>
<a onclick="show('settings')">Settings</a>
</div>

<div class="user">
<div>Welcome, Guest</div>
<div class="avatar">G</div>
<button onclick="toggle()">🌗</button>
</div>

</div>

<h2>🚀 Roosevelt Emac Operations Console</h2>

<div id="dashboard">

<div class="container">

<!-- LOGIN CARD -->
<div class="card">
<h3>🔐 Quick Login</h3>

<input id="user" placeholder="username"><br><br>
<input id="pass" type="password" placeholder="password"><br><br>

<button onclick="login()">Login</button>
</div>

<div class="card">
<h3>📊 System</h3>
<p>{host}</p>
<p>{time}</p>
<p>CPU: {random.randint(20,90)}%</p>
</div>

<div class="card">
<h3>🎮 Gaming</h3>
<p class="status-green">ACTIVE</p>
</div>

<div class="card">
<h3>🏦 Banking</h3>
<p class="status-green">SECURE</p>
</div>

<div class="card">
<h3>🎬 Streaming</h3>
<p class="status-green">RUNNING</p>
</div>

<div class="card">
<h3>⚙️ Control</h3>
<button onclick="run('/restart_service',this)">Restart</button>
<button onclick="run('/scale_service',this)">Scale</button>
<button onclick="run('/security_alert',this)">Alert</button>
</div>

<div class="card">
<h3>📜 Logs</h3>
<ul id="logs"></ul>
</div>

</div>

</div>

<!-- SERVICES -->
<div id="services" style="display:none;padding:20px">
<h2>🧩 Services</h2>
<div id="servicesContent"></div>
</div>

<!-- MONITOR -->
<div id="monitor" style="display:none;padding:20px">
<h2>📊 Monitoring</h2>
</div>

<!-- SETTINGS -->
<div id="settings" style="display:none;padding:20px">
<h2>⚙️ Settings</h2>
</div>

<script>

function show(v) {{
let logged = localStorage.getItem("user")

if(!logged){{
alert("🔐 Please login to access this section")
}}

['dashboard','services','monitor','settings']
.forEach(x => document.getElementById(x).style.display='none')

document.getElementById(v).style.display='block'

if(v === "services"){{ loadServices() }}
}}

function login(){{
fetch('/login_inline',{{
method:'POST',
headers:{{'Content-Type':'application/x-www-form-urlencoded'}},
body:"username="+document.getElementById('user').value+
"&password="+document.getElementById('pass').value
}})
.then(r=>r.json())
.then(d=>{{
localStorage.setItem("user",d.role)
location.reload()
}})
}}

function run(endpoint,btn) {{
btn.innerText="Processing..."
fetch(endpoint).then(() => {{
btn.innerText="Done ✅"
loadLogs()
setTimeout(() => {{ btn.innerText="Ready"; }},1500)
}})
}}

function loadLogs() {{
fetch('/logs').then(r => r.json()).then(d => {{
let l=document.getElementById('logs')
l.innerHTML=""
d.logs.forEach(x => {{
let li=document.createElement('li')
li.innerText=x
l.appendChild(li)
}})
}})
}}

function loadServices(){{
let logged = localStorage.getItem("user")
let d = document.getElementById("servicesContent")

if(!logged){{
d.innerHTML = "<p>🔐 Login to view services</p>"
}}else{{
d.innerHTML = `
<div class='service'>🏦 Banking System</div>
<div class='service'>🎮 Gaming Engine</div>
<div class='service'>🎬 Streaming Platform</div>
`
}}
}}

function toggle(){{
document.body.classList.toggle('light')
}}

setInterval(loadLogs,2000)

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
