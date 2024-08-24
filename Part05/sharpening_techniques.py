"""Comparing different methods for sharpening images"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_image

def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)

image = cv2.imread('../images/cat-face.png')

# We create the kernel for sharpening images
kernel_sharpen_1 = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

kernel_sharpen_2 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

kernel_sharpen_3 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])

kernel_sharpen_4 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

# Apply all the kernels we have created:
sharp_image_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
sharp_image_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
sharp_image_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
sharp_image_4 = cv2.filter2D(image, -1, kernel_sharpen_4)

# Try the unsharped filter:
sharp_image_5 = unsharped_filter(image)

image_BGR_list = [image, sharp_image_1, sharp_image_2, sharp_image_3, sharp_image_4, sharp_image_5]
title_list = ["original", "sharp 1", "sharp 2", "sharp 3", "sharp 4", "sharp 5"]
pos_list = [1, 2, 3, 4, 5, 6]
show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Sharpening images", 3)
