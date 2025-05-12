
import gradio as gr

def launch_log_viewer():
    with gr.Blocks() as ui:
        gr.Markdown("## 📜 Merge Logs")
        log_path = gr.Textbox(label="Log File Path", value="merge_log.txt")
        refresh = gr.Button("Refresh Log")
        content = gr.Textbox(label="Log Contents", lines=20)

        def read_log(path):
            try:
                with open(path, 'r') as f:
                    return f.read()
            except:
                return "Log file not found or unreadable."

        refresh.click(fn=read_log, inputs=[log_path], outputs=[content])
    return ui
