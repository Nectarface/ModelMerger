
import torch

def compose_loras(lora_paths, weights, output_path):
    assert len(lora_paths) == len(weights), "Mismatch between LoRA files and weights"
    combined = torch.load(lora_paths[0], map_location='cpu')
    for key in combined:
        combined[key] *= weights[0]

    for path, weight in zip(lora_paths[1:], weights[1:]):
        lora = torch.load(path, map_location='cpu')
        for key in lora:
            if key in combined:
                combined[key] += lora[key] * weight
            else:
                combined[key] = lora[key] * weight

    torch.save(combined, output_path)
    return output_path
