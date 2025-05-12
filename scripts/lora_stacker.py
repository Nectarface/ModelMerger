
import torch

def stack_loras(lora_paths, output_path):
    if not lora_paths:
        raise ValueError("No LoRA paths provided.")
    combined = torch.load(lora_paths[0], map_location='cpu')
    for path in lora_paths[1:]:
        lora = torch.load(path, map_location='cpu')
        for key in lora:
            if key in combined:
                combined[key] += lora[key]
            else:
                combined[key] = lora[key]
    torch.save(combined, output_path)
    return output_path
