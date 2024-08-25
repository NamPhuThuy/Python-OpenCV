import numpy as np
import cv2
import matplotlib.pyplot as plt
from Utils import show_image

image = cv2.imread('../images/wukong.jpg')

# Add 60 to every pixel on the image. The result will look lighter:
M = np.ones(image.shape, dtype="uint8") * 60
added_image = cv2.add(image, M)

# Subtract 60 from every pixel. The result will look darker:
subtracted_image = cv2.subtract(image, M)

# Additionally, we can build an scalar and add/subtract it:
scalar = np.ones((1, 3), dtype="float") * 110
added_image_2 = cv2.add(image, scalar)
subtracted_image_2 = cv2.subtract(image, scalar)

# Create lists and add to the method
image_list = [image, added_image, subtracted_image, added_image_2, subtracted_image_2]
title_list = ["image", "added 60 (image + image)", "subtracted 60 (image - images)", "added 110 (image + scalar)", "subtracted 110 (image - scalar)"]
pos_list = [1, 2, 3, 5, 6]
show_image.show_images_with_titles_and_positions(image_list, title_list, pos_list, "Arithmetic with images")
