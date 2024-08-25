"""
Comparing different kernels using cv2.filter2D()
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_image

image = cv2.imread('../images/avatar.png')

# We try different kernels
# Identify kernel (does not modify the image)
kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]])

# Try different kernels for edge detection:
kernel_edge_detection_1 = np.array([[1, 0, -1],
                                    [0, 0, 0],
                                    [-1, 0, 1]])

kernel_edge_detection_2 = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

kernel_edge_detection_3 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])

# Try different kernels for sharpening:
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

kernel_unsharp_masking = -1 / 256 * np.array([[1, 4, 6, 4, 1],
                                              [4, 16, 24, 16, 4],
                                              [6, 24, -476, 24, 6],
                                              [4, 16, 24, 16, 4],
                                              [1, 4, 6, 4, 1]])

# Try different kernels for smoothing:
kernel_blur = 1 / 9 * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])

gaussian_blur = 1 / 16 * np.array([[1, 2, 1],
                                   [2, 4, 2],
                                   [1, 2, 1]])

# Try a kernel for embossing:
kernel_emboss = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]])

# Try different kernels for edge detection:
sobel_x_kernel = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

outline_kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

# Apply all the kernels:
original_image = cv2.filter2D(image, -1, kernel_identity)
edge_image_1 = cv2.filter2D(image, -1, kernel_edge_detection_1)
edge_image_2 = cv2.filter2D(image, -1, kernel_edge_detection_2)
edge_image_3 = cv2.filter2D(image, -1, kernel_edge_detection_3)
sharpen_image = cv2.filter2D(image, -1, kernel_sharpen)
unsharp_masking_image = cv2.filter2D(image, -1, kernel_unsharp_masking)
blur_image = cv2.filter2D(image, -1, kernel_blur)
gaussian_blur_image = cv2.filter2D(image, -1, gaussian_blur)
emboss_image = cv2.filter2D(image, -1, kernel_emboss)
sobel_x_image = cv2.filter2D(image, -1, sobel_x_kernel)
sobel_y_image = cv2.filter2D(image, -1, sobel_y_kernel)
outline_image = cv2.filter2D(image, -1, outline_kernel)

image_BGR_list = [original_image, edge_image_1, edge_image_2, edge_image_3, sharpen_image, unsharp_masking_image, blur_image, gaussian_blur_image, emboss_image, sobel_x_image, sobel_y_image, outline_image]
title_list = ["identity kernel", "edge detection 1", "edge detection 2", "edge detection 3", "sharpen", "unsharp masking", "blur image", "gaussian blur image", "emboss image", "sobel x image", "sobel y image", "outline image"]
pos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Comparing different kernels using cv2.filter2D()")


