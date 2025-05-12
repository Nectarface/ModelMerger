
from datetime import datetime

def log_message(message, log_path="merge_log.txt"):
    time_stamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full = f"{time_stamp} {message}\n"
    with open(log_path, 'a') as f:
        f.write(full)
    return full
