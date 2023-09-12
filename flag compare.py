# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import random
from PIL import Image

allflags = list()
for img in os.listdir("C:/Users/robph/Desktop/flags"):
    allflags.append(img)
choice = random.randint(0, len(allflags) - 1)
chosenImage = "C:/Users/robph/Desktop/flags/" + allflags[choice]
print(chosenImage)
flag = Image.open(chosenImage).convert('RGB')
#flag.show()
if flag.size != (2560, 1707):
    resized = flag.resize((2560, 1707))

    resized.show()
