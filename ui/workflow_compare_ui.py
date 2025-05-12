
import gradio as gr

AVAILABLE_MODELS = [
    "dreamlike-photoreal-2.0.ckpt",
    "realisticVision-v51.safetensors",
    "revAnimated-v122.ckpt",
    "stable-diffusion-v15.ckpt",
    "anyLoRA-model.pt",
    "anime-style-v4.ckpt",
    "dreambooth-facefusion.ckpt",
    "ultra-dream-v2.ckpt",
    "fantasyFusion-v1.ckpt",
    "deepPortrait-v3.ckpt"
]

def launch_workflow_comparison_ui():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧪 Compare Outputs Across 10 Workflows")

        prompts = []
        images = []
        model_selectors = []

        for i in range(10):
            with gr.Row():
                model_selectors.append(gr.Dropdown(choices=AVAILABLE_MODELS, label=f"Workflow {i+1} Model", value=AVAILABLE_MODELS[i]))
            with gr.Row():
                prompts.append(gr.Textbox(label=f"Prompt {i+1}", placeholder="Enter prompt..."))
            with gr.Row():
                images.append(gr.Image(label=f"Output {i+1}", type="filepath"))

        generate_btn = gr.Button("Generate All")
        status = gr.Textbox(label="Status")

        def generate_all(*args):
            all_prompts = args[::2]
            selected_models = args[1::2]
            results = []
            for i in range(10):
                # Placeholder image path using model name and prompt
                results.append(f"/fake/path/output_wf{i+1}_{selected_models[i].replace('.ckpt','')}.png")
            return results + ["✅ Simulated generation using model-per-workflow."]

        generate_btn.click(fn=generate_all, inputs=sum(zip(prompts, model_selectors), ()), outputs=images + [status])

    return ui
