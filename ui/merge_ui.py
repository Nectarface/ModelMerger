
import gradio as gr
from scripts.merge_logic import merge_models
from scripts.weight_utils import normalize_weights
from scripts.merge_templates import save_template, load_template
from scripts.preview_generator import generate_preview

def launch_ui():
    with gr.Blocks() as interface:
        gr.Markdown("## 🧬 Enhanced Checkpoint Merger")

        model_files = gr.File(label="Model Files", file_types=[".ckpt", ".safetensors"], file_count="multiple")
        weights_input = gr.Textbox(label="Weights (comma-separated)", placeholder="e.g. 0.5,0.3,0.2")
        normalize_btn = gr.Button("Normalize Weights")
        normalized_out = gr.Textbox(label="Normalized Output")
        
        output_path = gr.Textbox(label="Output Path", value="merged_output.ckpt")
        run_btn = gr.Button("Merge")
        save_template_btn = gr.Button("Save Merge Template")
        load_template_btn = gr.File(label="Load Merge Template", file_types=[".json"])
        preview_image = gr.Image(label="Preview", type="filepath")
        status = gr.Textbox(label="Status")

        def normalize(weights_str):
            weights = [float(w.strip()) for w in weights_str.split(',')]
            return ",".join(map(str, normalize_weights(weights)))

        def run_merge(models, weights_str, output_path):
            weights = [float(w.strip()) for w in weights_str.split(',')]
            if len(models) != len(weights):
                return f"❌ Count mismatch", None
            result_path = merge_models(models, weights, output_path)
            preview = generate_preview(result_path)
            return f"✅ Merged model saved: {result_path}", preview

        def save_template_handler(models, weights_str):
            weights = [float(w.strip()) for w in weights_str.split(',')]
            save_template(models, weights)
            return "✅ Template saved as merge_template.json"

        def load_template_handler(file_json):
            models, weights = load_template(file_json)
            return models, ",".join(map(str, weights))

        normalize_btn.click(fn=normalize, inputs=weights_input, outputs=normalized_out)
        run_btn.click(fn=run_merge, inputs=[model_files, weights_input, output_path], outputs=[status, preview_image])
        save_template_btn.click(fn=save_template_handler, inputs=[model_files, weights_input], outputs=status)
        load_template_btn.change(fn=load_template_handler, inputs=[load_template_btn], outputs=[model_files, weights_input])

    return interface
