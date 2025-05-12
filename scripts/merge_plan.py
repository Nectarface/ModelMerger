
import json

def save_merge_plan(plan, path):
    with open(path, 'w') as f:
        json.dump(plan, f, indent=2)

def load_merge_plan(path):
    with open(path, 'r') as f:
        return json.load(f)
