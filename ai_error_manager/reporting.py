
import requests
import os
from datetime import datetime

WEBHOOK_URL = "http://localhost:4000/webhook"  # Replace with actual webhook if needed
LOG_PATH = "fix_history.log"

def log_fix(action, result):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now()}] ACTION: {action} -> RESULT: {result}\n")

def send_report(error_log, fix_result):
    try:
        payload = {
            "error": error_log,
            "fix_result": fix_result,
            "timestamp": str(datetime.now())
        }
        response = requests.post(WEBHOOK_URL, json=payload)
        return "✅ Report sent" if response.ok else f"❌ Webhook failed: {response.status_code}"
    except Exception as e:
        return f"❌ Webhook exception: {str(e)}"
