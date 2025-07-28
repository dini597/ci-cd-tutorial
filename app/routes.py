from flask import json, jsonify
from app import app
from app import db
from app.models import Menu
from datetime import datetime  # ✅ Add this at the top

@app.route('/')
def home():
	return jsonify({ "status": "ok" })

@app.route('/menu')
def menu():
    current_time = datetime.utcnow().isoformat() + "Z"  # ✅ Add timestamp

    today = Menu.query.first()
    if today:
        body = {
            "today_special": today.name,
            "timestamp": current_time
        }
        status = 200
    else:
        body = {
            "error": "Sorry, the service is not available today.",
            "timestamp": current_time
        }
        status = 404
    return jsonify(body), status

    


 

    