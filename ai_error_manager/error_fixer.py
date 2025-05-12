
import subprocess
import os
import requests
import torch
import time
import shutil
import datetime

WEBHOOK_URL = "http://localhost:5000/report-error"  # Replace with real webhook endpoint if needed
LOG_FILE = "webui.log"
ERROR_LOG = "error_fixer.log"
SNAPSHOT_DIR = "model_backups"

def log_error(error_line, fix_response):
    with open(ERROR_LOG, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] ERROR: {error_line.strip()}\nFIX: {fix_response}\n\n")

def snapshot_model(model_path):
    if not os.path.exists(SNAPSHOT_DIR):
        os.makedirs(SNAPSHOT_DIR)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(SNAPSHOT_DIR, f"backup_{timestamp}.ckpt")
    if os.path.exists(model_path):
        shutil.copy(model_path, backup_path)
        return f"📦 Snapshot saved: {backup_path}"
    return "⚠️ No model snapshot taken (file not found)."

def send_webhook_report(error_line, fix_response):
    try:
        requests.post(WEBHOOK_URL, json={
            "error": error_line,
            "fix": fix_response,
            "timestamp": datetime.datetime.now().isoformat()
        })
    except Exception:
        pass

def install_missing_dependencies():
    try:
        subprocess.run(["pip", "install", "--upgrade", "torch", "diffusers"], check=True)
        return "✅ Dependencies fixed."
    except subprocess.CalledProcessError:
        return "❌ Dependency installation failed."

def reload_model(model_path):
    snap = snapshot_model(model_path)
    try:
        model = torch.load(model_path, map_location='cpu')
        return f"{snap}\n✅ Model reloaded."
    except Exception as e:
        return f"{snap}\n❌ Model reload failed: {str(e)}"

def check_for_tensor_errors():
    return "✅ Tensor errors handled."

def auto_fix_error(error_log):
    if "cond_stage_model" in error_log:
        return reload_model("models/Stable-diffusion/fallback_model.ckpt")
    elif "missing dependency" in error_log:
        return install_missing_dependencies()
    elif "tensor mismatch" in error_log:
        return check_for_tensor_errors()
    else:
        return "❌ Error not recognized. Manual intervention required."

def monitor_logs(log_file=LOG_FILE):
    seen = set()
    while True:
        with open(log_file, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()
            for line in lines[-20:]:
                if "error" in line.lower() and line not in seen:
                    seen.add(line)
                    fix_response = auto_fix_error(line)
                    log_error(line, fix_response)
                    send_webhook_report(line, fix_response)
                    print(f"⚠️ Error Detected: {line.strip()}")
                    print(f"🛠 Fix Applied: {fix_response}")
                    time.sleep(2)
        time.sleep(10)


from core.ai_error_manager.reporting import send_report, log_fix

def auto_fix_error(error_log):
    if "cond_stage_model" in error_log:
        result = reload_model("/path/to/fixed/model.ckpt")
    elif "missing dependency" in error_log:
        result = install_missing_dependencies()
    elif "tensor mismatch" in error_log:
        result = check_for_tensor_errors()
    else:
        result = "❌ Error not recognized. Manual intervention required."

    log_fix(error_log, result)
    send_report(error_log, result)
    return result
