
import os
import json

def save_chat(history, path="chat_memory.json"):
    with open(path, 'w') as f:
        json.dump(history, f)

def load_chat(path="chat_memory.json"):
    if not os.path.exists(path): return []
    with open(path, 'r') as f:
        return json.load(f)
