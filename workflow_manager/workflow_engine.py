
import os
import json

WORKFLOW_DIR = "workflows"

def init_workflows():
    os.makedirs(WORKFLOW_DIR, exist_ok=True)
    for i in range(10):
        wf_path = os.path.join(WORKFLOW_DIR, f"workflow_{i+1}.json")
        if not os.path.exists(wf_path):
            with open(wf_path, 'w') as f:
                json.dump({"name": f"Workflow {i+1}", "settings": {}}, f)

def save_workflow(index, settings):
    path = os.path.join(WORKFLOW_DIR, f"workflow_{index+1}.json")
    with open(path, 'w') as f:
        json.dump(settings, f, indent=2)
    return f"✅ Saved workflow_{index+1}.json"

def load_workflow(index):
    path = os.path.join(WORKFLOW_DIR, f"workflow_{index+1}.json")
    if not os.path.exists(path):
        return {"name": f"Workflow {index+1}", "settings": {}}
    with open(path, 'r') as f:
        return json.load(f)
