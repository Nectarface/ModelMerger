
import gradio as gr
from core.workflow_manager.workflow_engine import init_workflows, load_workflow, save_workflow

init_workflows()

def launch_workflow_ui():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧠 Multi-Workflow Control Panel (10x Workflow Engine)")

        dropdown = gr.Dropdown(choices=[f"Workflow {i+1}" for i in range(10)], label="Select Workflow", value="Workflow 1")
        json_box = gr.Code(label="Workflow Settings", language="json")
        save_btn = gr.Button("Save Workflow")
        status = gr.Textbox(label="Status")

        def on_select(name):
            index = int(name.split()[-1]) - 1
            data = load_workflow(index)
            return gr.update(value=json.dumps(data, indent=2))

        def on_save(name, json_str):
            index = int(name.split()[-1]) - 1
            try:
                settings = json.loads(json_str)
                return save_workflow(index, settings)
            except Exception as e:
                return f"❌ Error: {str(e)}"

        dropdown.change(fn=on_select, inputs=dropdown, outputs=json_box)
        save_btn.click(fn=on_save, inputs=[dropdown, json_box], outputs=status)

    return ui
