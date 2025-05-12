
import torch

def merge_lora(base_model_path, lora_paths, output_path):
    base = torch.load(base_model_path, map_location='cpu')
    for lora_path in lora_paths:
        lora = torch.load(lora_path, map_location='cpu')
        for key in lora:
            if key in base:
                base[key] += lora[key]
    torch.save(base, output_path)
    return output_path
