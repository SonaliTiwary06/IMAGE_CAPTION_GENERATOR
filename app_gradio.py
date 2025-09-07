import gradio as gr
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Pick device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load BLIP (base)
MODEL_NAME = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
model.eval()

def caption_image(image, max_new_tokens=32, num_beams=5, repetition_penalty=1.0, min_length=5):
    if image is None:
        return "Please upload an image."
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=int(max_new_tokens),
            num_beams=int(num_beams),
            repetition_penalty=float(repetition_penalty),
            min_length=int(min_length)
        )
    caption = processor.decode(outputs[0], skip_special_tokens=True).strip()
    return caption

with gr.Blocks(title="Image Caption Generator (BLIP)") as demo:
    gr.Markdown("# 🖼️ Image Caption Generator\nUpload an image and get a human‑like caption.")

    with gr.Row():
        with gr.Column():
            img = gr.Image(type="pil", label="Upload image")
            max_new_tokens = gr.Slider(8, 64, value=32, step=1, label="Max new tokens")
            num_beams = gr.Slider(1, 8, value=5, step=1, label="Beam search width")
            repetition_penalty = gr.Slider(0.8, 2.0, value=1.0, step=0.05, label="Repetition penalty")
            min_length = gr.Slider(0, 15, value=5, step=1, label="Min length")
            btn = gr.Button("Generate Caption")
        with gr.Column():
            out = gr.Textbox(label="Caption", lines=3)

    btn.click(
        fn=caption_image,
        inputs=[img, max_new_tokens, num_beams, repetition_penalty, min_length],
        outputs=out
    )

if __name__ == "__main__":
    demo.queue().launch()
