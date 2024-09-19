import gradio as gr
import torch
from duffusers import StableDiffusers3Pipeline

def image_generation(prompt):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipeline = StableDiffusers3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers",
                                                        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                                                        text_encoder_3 = None,
                                                        tokenizer_3 = None)
    # pipeline.to(device)
    pipeline.enable_model_cpu_offload()

    image = pipeline(
        prompt = prompt,
        negative_prompt = "blurred, ugly, watermark, low resolution, blurry, nude",
        num_inference_steps = 40,
        height=1024,
        width=1024,
        guidance_scale=8.0
    ).images[0]

    image.show()

interface= gr.interface(
    fn=image_generation,
    inputs = gr.Textbox(lines="2", placeholder="Enter Your Prompt ..."),
    outputs = gr.Image(type="pil"),
    title = "AI Text Generation By SD-3M",
    examples = "A magician cat doing spell"
)

interface.launch()