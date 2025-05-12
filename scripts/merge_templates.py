
import json

def save_template(model_paths, weights, out_path="merge_template.json"):
    data = {"models": model_paths, "weights": weights}
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)

def load_template(template_path):
    with open(template_path, 'r') as f:
        data = json.load(f)
    return data["models"], data["weights"]
