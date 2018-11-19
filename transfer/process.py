import random
from typing import Any

def rand_crop(img: Any, crop_height: int, crop_width: int) -> Any:
  full_height, full_width, _ = img.shape
  start_h = random.randint(0, full_height - crop_height)
  start_w = random.randint(0, full_width - crop_width)

  return img[start_h:start_h + crop_height, start_w: start_w + crop_width]

def all_crops(img: Any, crop_height: int, crop_width: int) -> list:
  crops = []
  full_height, full_width, _ = img.shape

  height_steps = full_height // crop_height
  width_steps = full_width // crop_width

  for height_step in range(height_steps + 1):
    start_h = crop_height * height_step if height_step < height_steps else full_height - crop_height
    
    for width_step in range(width_steps + 1):
      start_w = crop_width * width_step if width_step < width_steps else full_width - crop_width
      
      crops.append(img[start_h: start_h + crop_height, start_w: start_w + crop_width])
  
  return crops

def cropped_to_match(content_img: Any, style_img: Any) -> Any:
    return rand_crop(style_img, content_img.shape[0], content_img.shape[1])