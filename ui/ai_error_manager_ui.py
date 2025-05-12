
import gradio as gr
from core.ai_error_manager.error_fixer import monitor_logs

def launch_error_monitor_ui():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧠 AI-Powered Error Detection & Fixer")
        start_btn = gr.Button("Start Error Fixer")
        stop_btn = gr.Button("Stop Error Fixer")
        status = gr.Textbox(label="Status")

        def start_error_fixer():
            start_btn.disabled = True
            stop_btn.disabled = False
            status.update("Monitoring logs... Fixing errors as they occur.")
            monitor_logs("webui.log")

        def stop_error_fixer():
            start_btn.disabled = False
            stop_btn.disabled = True
            status.update("Error Fixer Stopped.")
        
        start_btn.click(start_error_fixer, outputs=status)
        stop_btn.click(stop_error_fixer, outputs=status)

    return ui
