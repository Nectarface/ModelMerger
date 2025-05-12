
import gradio as gr
from scripts.merge_logic import merge_models

def launch_ui():
    with gr.Blocks() as interface:
        gr.Markdown("## 🧬 Model Merger (Multi-Model)")
        models = [gr.File(label=f"Model {i+1}") for i in range(3)]
        weights = [gr.Slider(0, 1, value=1/3, label=f"Weight {i+1}") for i in range(3)]
        output_path = gr.Textbox(label="Output Path", value="merged_model.ckpt")
        run_btn = gr.Button("Merge")
        status = gr.Textbox(label="Status")

        def run_merge(*args):
            model_paths = args[:3]
            model_weights = args[3:6]
            out = args[6]
            try:
                result = merge_models(model_paths, model_weights, out)
                return f"✅ Merged to: {result}"
            except Exception as e:
                return f"❌ Error: {str(e)}"

        run_btn.click(fn=run_merge, inputs=models + weights + [output_path], outputs=status)
    return interface
