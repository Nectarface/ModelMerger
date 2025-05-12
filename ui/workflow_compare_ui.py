
import gradio as gr
import requests
import os

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

API_URL = "http://127.0.0.1:7860"

def generate_image(prompt, model_name, index):
    try:
        # Set model
        requests.post(f"{API_URL}/sdapi/v1/options", json={"sd_model_checkpoint": model_name})

        # Generate image
        payload = {
            "prompt": prompt,
            "steps": 25,
            "width": 512,
            "height": 512,
            "sampler_index": "Euler a"
        }
        response = requests.post(f"{API_URL}/sdapi/v1/txt2img", json=payload).json()
        image_data = response["images"][0]
        output_dir = "outputs/workflow_compare"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"workflow_{index+1}.png")
        with open(output_path, "wb") as f:
            f.write(requests.get(f"data:image/png;base64,{image_data}".split(",", 1)[1]).content)
        return output_path
    except Exception as e:
        return f"❌ Error in workflow {index+1}: {str(e)}"

def launch_workflow_comparison_ui():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧪 Real-Time Comparison Across 10 Workflows (txt2img)")

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
        status = gr.Textbox(label="Status", lines=2)

        def generate_all(*args):
            all_prompts = args[::2]
            selected_models = args[1::2]
            output_paths = []
            for i in range(10):
                path = generate_image(all_prompts[i], selected_models[i], i)
                output_paths.append(path)
            return output_paths + ["✅ All images generated."]
        
        generate_btn.click(fn=generate_all, inputs=sum(zip(prompts, model_selectors), ()), outputs=images + [status])

    return ui
