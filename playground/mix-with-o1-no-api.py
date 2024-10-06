# %load_ext autoreload
# %autoreload 2

import os
import sys
sys.path.append('/data/srivats/workplace/Omost')

##################################
#
#  ChatGPT o1-preview response
#
##################################

from PIL import Image
import matplotlib.pyplot as plt

# from playground.plans.manual.photosynthesis_v1 import canvas as my_canvas
from playground.plans.manual.tidal_movement_v1 import canvas as my_canvas


from playground.plans.o1.photosynthesis_v1 import canvas as o1_canvas
# from playground.plans.o1.volcanic_erruption_v1 import canvas as o1_canvas
# from playground.plans.o1.volcanic_erruption_v2 import canvas as o1_canvas
# from playground.plans.o1.tidal_movement_v1 import canvas as o1_canvas
# from playground.plans.o1.tidal_movement_v2 import canvas as o1_canvas
# from playground.plans.o1.tidal_movement_v3 import canvas as o1_canvas
# from playground.plans.o1.earthquake_v1 import canvas as o1_canvas
# from playground.plans.o1.rainbow_formation_v1 import canvas as o1_canvas
# from playground.plans.o1.lunar_eclipse_v1 import canvas as o1_canvas
# from playground.plans.o1.water_cycle_v1 import canvas as o1_canvas

# from playground.plans.o1.photosynthesis_bbox_v1 import canvas as o1_canvas
# from playground.plans.o1.water_cycle_bbox_v1 import canvas as o1_canvas
# from playground.plans.o1.lunar_eclipse_bbox_v1 import canvas as o1_canvas
# from playground.plans.o1.rainbow_formation_bbox_v1 import canvas as o1_canvas
# from playground.plans.o1.earthquake_bbox_v1 import canvas as o1_canvas


# from playground.plans.omost.photosynthesis_v1 import canvas as omost_canvas
# from playground.plans.omost.volcanic_erruption_v1 import canvas as omost_canvas
# from playground.plans.omost.volcanic_erruption_v2 import canvas as omost_canvas
# from playground.plans.omost.tidal_movement_v1 import canvas as omost_canvas

# from playground.plans.omost.earthquake_v1 import canvas as omost_canvas
from playground.plans.omost.rainbow_formation_v1 import canvas as omost_canvas
# from playground.plans.omost.lunar_eclipse_v1 import canvas as omost_canvas
# from playground.plans.omost.water_cycle_v1 import canvas as omost_canvas


# canvas_outputs = my_canvas.process()
# canvas_outputs = o1_canvas.process()
canvas_outputs = omost_canvas.process()


img = Image.fromarray(canvas_outputs['initial_latent'])
plt.imshow(img)
plt.show()
# img.save('/data/srivats/workplace/Omost/playground/plans/o1/tidal_movement_v3.jpg')

# for cond in canvas_outputs['bag_of_conditions']:
#     print("Mask")
#     plt.imshow(cond['mask'])
#     plt.show()
#     print("Prefixes", cond['prefixes'])
#     print("Suffixes")
#     for suffix in cond['suffixes']:
#         print(" - ", suffix)


######################
#
#  Image Generation
#
######################

import torch
import numpy as np
from transformers import CLIPTextModel, CLIPTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from diffusers import AutoencoderKL, UNet2DConditionModel
from diffusers.models.attention_processor import AttnProcessor2_0
from lib_omost.pipeline import StableDiffusionXLOmostPipeline

import lib_omost.memory_management as memory_management

@torch.inference_mode()
def pytorch2numpy(imgs):
    results = []
    for x in imgs:
        y = x.movedim(0, -1)
        y = y * 127.5 + 127.5
        y = y.detach().float().cpu().numpy().clip(0, 255).astype(np.uint8)
        results.append(y)
    return results

@torch.inference_mode()
def numpy2pytorch(imgs):
    h = torch.from_numpy(np.stack(imgs, axis=0)).float() / 127.5 - 1.0
    h = h.movedim(-1, 1)
    return h


def resize_without_crop(image, target_width, target_height):
    pil_image = Image.fromarray(image)
    resized_image = pil_image.resize((target_width, target_height), Image.LANCZOS)
    return np.array(resized_image)



####  Loading Models  ####

# SDXL
sdxl_name = 'SG161222/RealVisXL_V4.0'

tokenizer = CLIPTokenizer.from_pretrained(
    sdxl_name, subfolder="tokenizer")
tokenizer_2 = CLIPTokenizer.from_pretrained(
    sdxl_name, subfolder="tokenizer_2")
text_encoder = CLIPTextModel.from_pretrained(
    sdxl_name, subfolder="text_encoder", torch_dtype=torch.float16, variant="fp16")
text_encoder_2 = CLIPTextModel.from_pretrained(
    sdxl_name, subfolder="text_encoder_2", torch_dtype=torch.float16, variant="fp16")
vae = AutoencoderKL.from_pretrained(
    sdxl_name, subfolder="vae", torch_dtype=torch.bfloat16, variant="fp16")  # bfloat16 vae
unet = UNet2DConditionModel.from_pretrained(
    sdxl_name, subfolder="unet", torch_dtype=torch.float16, variant="fp16")

unet.set_attn_processor(AttnProcessor2_0())
vae.set_attn_processor(AttnProcessor2_0())

pipeline = StableDiffusionXLOmostPipeline(
    vae=vae,
    text_encoder=text_encoder,
    tokenizer=tokenizer,
    text_encoder_2=text_encoder_2,
    tokenizer_2=tokenizer_2,
    unet=unet,
    scheduler=None,  # We completely give up diffusers sampling system and use A1111's method
)

####  Generation  ####

use_initial_latent = True
eps = 0.05

image_width = 600
image_height = 800
image_width, image_height = int(image_width // 64) * 64, int(image_height // 64) * 64

seed = 123456
rng = torch.Generator(device=memory_management.gpu).manual_seed(seed)

memory_management.load_models_to_gpu([text_encoder, text_encoder_2])

negative_prompt = 'no text, no arrows, no annotations, lowres, bad anatomy, bad hands, cropped, worst quality'
positive_cond, positive_pooler, negative_cond, negative_pooler = pipeline.all_conds_from_canvas(canvas_outputs, negative_prompt)

if use_initial_latent:
    memory_management.load_models_to_gpu([vae])
    initial_latent = torch.from_numpy(canvas_outputs['initial_latent'])[None].movedim(-1, 1) / 127.5 - 1.0
    initial_latent_blur = 40
    initial_latent = torch.nn.functional.avg_pool2d(
        torch.nn.functional.pad(initial_latent, (initial_latent_blur,) * 4, mode='reflect'),
        kernel_size=(initial_latent_blur * 2 + 1,) * 2, stride=(1, 1))
    initial_latent = torch.nn.functional.interpolate(initial_latent, (image_height, image_width))
    initial_latent = initial_latent.to(dtype=vae.dtype, device=vae.device)
    initial_latent = vae.encode(initial_latent).latent_dist.mode() * vae.config.scaling_factor
else:
    initial_latent = torch.zeros(size=(num_samples, 4, image_height // 8, image_width // 8), dtype=torch.float32)

memory_management.load_models_to_gpu([unet])

initial_latent = initial_latent.to(dtype=unet.dtype, device=unet.device)

steps = 100
num_samples = 3
cfg = 15.0
latents = pipeline(
    initial_latent=initial_latent,
    strength=1.0,
    num_inference_steps=int(steps),
    batch_size=num_samples,
    prompt_embeds=positive_cond,
    negative_prompt_embeds=negative_cond,
    pooled_prompt_embeds=positive_pooler,
    negative_pooled_prompt_embeds=negative_pooler,
    generator=rng,
    guidance_scale=float(cfg),
).images

memory_management.load_models_to_gpu([vae])
latents = latents.to(dtype=vae.dtype, device=vae.device) / vae.config.scaling_factor
pixels = vae.decode(latents).sample
B, C, H, W = pixels.shape
pixels = pytorch2numpy(pixels)

#### AttributeError: 'Tensor' object has no attribute '__array_interface__'
# highres_scale = 1.5
# highres_denoise = 0.4
# highres_steps = 25
# if highres_scale > 1.0 + eps:
#     pixels = [
#         resize_without_crop(
#             image=p,
#             target_width=int(round(W * highres_scale / 64.0) * 64),
#             target_height=int(round(H * highres_scale / 64.0) * 64)
#         ) for p in pixels
#     ]

#     pixels = numpy2pytorch(pixels).to(device=vae.device, dtype=vae.dtype)
#     latents = vae.encode(pixels).latent_dist.mode() * vae.config.scaling_factor

#     memory_management.load_models_to_gpu([unet])
#     latents = latents.to(device=unet.device, dtype=unet.dtype)

#     latents = pipeline(
#         initial_latent=latents,
#         strength=highres_denoise,
#         num_inference_steps=highres_steps,
#         batch_size=num_samples,
#         prompt_embeds=positive_cond,
#         negative_prompt_embeds=negative_cond,
#         pooled_prompt_embeds=positive_pooler,
#         negative_pooled_prompt_embeds=negative_pooler,
#         generator=rng,
#         guidance_scale=float(cfg),
#     ).images

#     memory_management.load_models_to_gpu([vae])
#     latents = latents.to(dtype=vae.dtype, device=vae.device) / vae.config.scaling_factor
#     pixels = vae.decode(latents).sample
#     pixels = pytorch2numpy(pixels)


for i in range(len(pixels)):
    image = Image.fromarray(pixels[i])
    plt.imshow(image)
    plt.show()
