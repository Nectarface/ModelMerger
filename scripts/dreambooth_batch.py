
import os

def batch_train_dreambooth(models, dataset_path, output_dir):
    logs = []
    for model_path in models:
        model_name = os.path.basename(model_path).split('.')[0]
        out_path = os.path.join(output_dir, f"{model_name}_trained")
        cmd = f"accelerate launch train_dreambooth.py --pretrained_model_name_or_path={model_path} --instance_data_dir={dataset_path} --output_dir={out_path}"
        result = os.system(cmd)
        logs.append((model_name, result))
    return logs
