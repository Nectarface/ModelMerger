
import torch
import safetensors.torch
import os

def merge_models(models, weights, output_path):
    assert len(models) == len(weights), "Mismatch between model list and weights"
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    base_state = torch.load(models[0], map_location='cpu')
    merged_state = {}

    for key in base_state:
        merged_state[key] = sum(
            torch.load(m, map_location='cpu')[key] * w for m, w in zip(models, normalized_weights)
        )

    torch.save(merged_state, output_path)
    return output_path
