
import gradio as gr
from scripts.face_body_trainer import train_face_body
from scripts.video_frame_extractor import extract_frames

def launch_face_body_trainer():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧠 Dual-Stream Face + Body Trainer with Video Support")
        face_model = gr.File(label="Face Model")
        body_model = gr.File(label="Body Model")
        face_data = gr.Textbox(label="Face Data Path")
        body_data = gr.Textbox(label="Body Data Path")
        output = gr.Textbox(label="Merged Output Path", value="merged_face_body.pt")
        train_btn = gr.Button("Train & Merge")
        train_result = gr.Textbox(label="Status")

        video_input = gr.File(label="Video for Dataset Prep", file_types=[".mp4", ".mov"])
        frame_out = gr.Textbox(label="Frame Output Directory")
        extract_btn = gr.Button("Extract Frames")
        extract_result = gr.Textbox(label="Frames Extracted")

        def run_training(fm, bm, fd, bd, out):
            result = train_face_body(fm, bm, fd, bd, out)
            return f"✅ Output saved: {result}"

        def run_extract(video, out_dir):
            total = extract_frames(video, out_dir)
            return f"Extracted {total} frames."

        train_btn.click(fn=run_training, inputs=[face_model, body_model, face_data, body_data, output], outputs=train_result)
        extract_btn.click(fn=run_extract, inputs=[video_input, frame_out], outputs=extract_result)
    return ui
