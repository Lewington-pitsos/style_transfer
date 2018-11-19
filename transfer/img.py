from typing import Any
from matplotlib import pyplot as plt
import cv2

def load(path: str) -> Any:
  bgr_img = cv2.imread(path)
  return cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

def show(img: Any):
  plt.imshow(img)
  plt.show()
