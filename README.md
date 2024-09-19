# ✨ Image Generation App Gradio ✨
**Text to Image SDXL Gradio App**

This repository contains a Gradio-based web interface for generating images from text using the Stable Diffusion XL model. Users can input a text prompt and a negative prompt, choose the image size, and generate an image using a pre-trained model from the Diffusers library by Hugging Face.
Features

   - Prompt-based image generation: Input custom text prompts to generate images using Stable Diffusion XL.
   - Negative prompts: Control undesired elements in image generation using negative prompts.
   - Multiple image sizes: Choose from various image sizes (512x512, 768x768, 1024x1024).
  -  Gradio interface: Easy-to-use Gradio Blocks interface for interacting with the model.

**Gradio app ui**
![SDXL-3-APP](https://github.com/TGouriSankar/Text-To-Image-SDXL/blob/main/SDXL-3-APP.png)
**App Link**:- [Click For Gradio App](https://huggingface.co/spaces/kasper-boy/image-generator-ai-sd-3-medium)

**Result of the model**
<p align="center">
  <img src="https://github.com/TGouriSankar/Text-To-Image-SDXL/blob/main/generated_image.png" alt="Image 1" width="45%">
  <img src="https://github.com/TGouriSankar/Text-To-Image-SDXL/blob/main/white.jpeg" alt="Image 2" width="45%">
</p>


> **Model Information**

This project uses the following pre-trained model:

  - Model: Stable Diffusion XL Base 1.0
  - Library: Diffusers

Requirements

- Python 3.8 or later
- PyTorch
- Hugging Face transformers, diffusers, and gradio libraries

You can install the required dependencies using the following command:
      
      pip install -r requirements.txt

> **Installation**

  1. Clone the repository:

         git clone https://github.com/your-username/text-to-image-sdxl.git
         cd text-to-image-sdxl      
  2. Install the required dependencies:

         pip install -r requirements.txt
  3. Run the application:

         python app.py
  4. The app will launch locally, and you can access it via the URL provided by Gradio.

**Usage**

  - Prompt: Enter a description of the image you want to generate in the prompt field.
  - Negative Prompt: Optionally, add elements you don't want in the image.
  - Size: Select the desired image size (512x512, 768x768, 1024x1024).
  - Click Submit to generate the image, and it will be displayed on the right-hand side.

> Example

**Future Enhancements**

  - Support for more advanced prompt customization.
  - Option to download the generated image.
  - GPU support for faster image generation.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
