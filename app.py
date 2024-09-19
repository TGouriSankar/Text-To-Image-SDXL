import gradio as gr
import torch
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import StableDiffusionPipeline

# Load the model and tokenizer
model_id = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe = pipe.to("cpu")

def generate_image(prompt, negative_prompt, size):
    if not prompt:
        prompt = "a beautiful landscape"
    if not negative_prompt:
        negative_prompt = ""
        
    width, height = map(int, size.split('x'))
    generator = torch.Generator("cpu").manual_seed(42)
    
    # Generate the image
    result = pipe(prompt, height=height, width=width, negative_prompt=negative_prompt, generator=generator)
    
    if result is not None and 'images' in result:
        return result.images[0]
    else:
        return None

with gr.Blocks() as demo:
    gr.Markdown("## Text to Image SDXL")
    
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="Prompt", placeholder="Enter the prompt here...")
            negative_prompt = gr.Textbox(label="Negative Prompt", placeholder="Enter the negative prompt here...")
            size = gr.Dropdown(choices=["512x512", "768x768", "1024x1024"], value="1024x1024", label="Size")
            submit = gr.Button("Submit")
        with gr.Column():
            output = gr.Image(label="Output")

    submit.click(generate_image, inputs=[prompt, negative_prompt, size], outputs=output)

demo.launch()

# import gradio as gr
# import torch
# from transformers import CLIPTextModel, CLIPTokenizer
# from diffusers import StableDiffusionPipeline

# # Load the model and tokenizer
# model_id = "stabilityai/stable-diffusion-xl-base-1.0"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
# pipe = pipe.to("cpu")

# def generate_image(prompt, negative_prompt, size):
#     width, height = map(int, size.split('x'))
#     generator = torch.Generator("cpu").manual_seed(42)
#     image = pipe(prompt, height=height, width=width, negative_prompt=negative_prompt, generator=generator).images[0]
#     return image

# with gr.Blocks() as demo:
#     gr.Markdown("## Text to Image SDXL")
    
#     with gr.Row():
#         with gr.Column():
#             prompt = gr.Textbox(label="Prompt")
#             negative_prompt = gr.Textbox(label="Negative Prompt")
#             size = gr.Dropdown(choices=["512x512", "768x768", "1024x1024"], value="1024x1024", label="Size")
#             submit = gr.Button("Submit")
#         with gr.Column():
#             output = gr.Image(label="Output")

#     submit.click(generate_image, inputs=[prompt, negative_prompt, size], outputs=output)

# demo.launch()
