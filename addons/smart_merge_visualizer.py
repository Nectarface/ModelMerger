
def visualize_merge(models, weights):
    return {
        "nodes": [{"id": i, "label": f"Model {i+1}\n{weights[i]*100:.1f}%"} for i in range(len(models))],
        "edges": [{"from": i, "to": "merged"} for i in range(len(models))],
        "result": "merged_model.ckpt"
    }
