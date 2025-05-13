
import launch
import os
import sys
import subprocess
import gradio as gr
from modules import script_callbacks

def on_ui_tabs():
    with gr.Blocks() as interface:
        gr.Markdown("## 🔧 Launch ModelForge Generator Suite")
        launch_button = gr.Button("Launch ModelForge Generator Suite")
        
        def launch_modelforge():
            subprocess.Popen(["python", "ModelForge_UI.py"], cwd=os.path.dirname(__file__))

        launch_button.click(fn=launch_modelforge, inputs=[], outputs=[])
    return [(interface, "ModelForge", "modelforge")]

script_callbacks.on_ui_tabs(on_ui_tabs)
