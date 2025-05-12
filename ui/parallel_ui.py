
import gradio as gr
import os
from scripts.parallel_utils import run_parallel_merges
from scripts.merge_logic import merge_models

def launch_parallel_ui():
    with gr.Blocks() as ui:
        gr.Markdown("## ⚡ Parallel Merge Queue")
        model_files = gr.File(label="Upload Multiple Models", file_types=['.ckpt', '.safetensors'], file_count='multiple')
        weight_text = gr.Textbox(label="Comma-Separated Weights", placeholder="e.g., 0.5,0.3,0.2")
        output_base = gr.Textbox(label="Output File Prefix", value="merged_model_")
        run_button = gr.Button("Run Parallel Merge")
        status = gr.Textbox(label="Merge Results")

        def run_merge_parallel(files, weights_str, output_base):
            weights = [float(w) for w in weights_str.split(',')]
            assert len(files) == len(weights), "Model and weight count mismatch"
            tasks = []
            for i, f in enumerate(files):
                other_models = files[:i] + files[i+1:]
                other_weights = weights[:i] + weights[i+1:]
                tasks.append(([f] + other_models, [weights[i]] + other_weights, f"{output_base}{i}.ckpt"))
            results = run_parallel_merges(tasks)
            return "\n".join(results)

        run_button.click(fn=run_merge_parallel, inputs=[model_files, weight_text, output_base], outputs=status)
    return ui
