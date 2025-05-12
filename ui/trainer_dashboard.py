
import gradio as gr
from scripts.dreambooth_batch import batch_train_dreambooth

def launch_trainer_dashboard():
    with gr.Blocks() as dash:
        gr.Markdown("## 🎯 Training Dashboard")
        models = gr.File(label="Base Models (.ckpt or .safetensors)", file_types=['.ckpt', '.safetensors'], file_count="multiple")
        dataset = gr.Textbox(label="Path to Training Dataset")
        out_dir = gr.Textbox(label="Output Directory")
        run_train = gr.Button("Start Batch Training")
        result = gr.Textbox(label="Training Log")

        def start_batch(models, dataset, out_dir):
            logs = batch_train_dreambooth(models, dataset, out_dir)
            return "\n".join([f"{m}: {s}" for m, s in logs])

        run_train.click(fn=start_batch, inputs=[models, dataset, out_dir], outputs=result)
    return dash
