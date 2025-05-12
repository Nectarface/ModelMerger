
import gradio as gr
from scripts.lora_composer import compose_loras

def launch_lora_composer():
    with gr.Blocks() as composer:
        gr.Markdown("## 🎼 LoRA Composer")
        lora_files = gr.File(label="Upload Multiple LoRAs", file_types=['.pt', '.safetensors'], file_count="multiple")
        weight_input = gr.Textbox(label="Weights (comma-separated)", placeholder="e.g., 0.6,0.2,0.2")
        output_path = gr.Textbox(label="Output LoRA Path", value="composed_lora.pt")
        run_button = gr.Button("Compose")
        status = gr.Textbox(label="Result")

        def run_composer(files, weights_str, output_path):
            weights = [float(w) for w in weights_str.strip().split(',')]
            result = compose_loras(files, weights, output_path)
            return f"✅ Composed to: {result}"

        run_button.click(fn=run_composer, inputs=[lora_files, weight_input, output_path], outputs=status)
    return composer
