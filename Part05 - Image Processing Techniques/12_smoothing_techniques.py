"""Comparing different methods for smoothing images"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_image

image = cv2.imread('../images/cat-face.png')

# We create the kernel for smoothing images
# In this case a (10,10) kernel is created
kernel_averaging_10_10 = np.ones((10, 10), np.float32) / 100

# Additionally, if you know the values, you can put them directly in the kernel:
# kernel_averaging_5_5 = np.ones((5, 5), np.float32)/25
kernel_averaging_5_5 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04]])

print("kernel: {}".format(kernel_averaging_5_5))

# The function cv2.filter2D() applies an arbitrary linear filter to the provided image:
smooth_image_f2D_5_5 = cv2.filter2D(image, -1, kernel_averaging_5_5)
smooth_image_f2D_10_10 = cv2.filter2D(image, -1, kernel_averaging_10_10)

# The function cv2.blur() smooths an image using the normalized box filter
smooth_image_b = cv2.blur(image, (10, 10))

# When the parameter normalize (by default True) of cv2.boxFilter() is equals to True,
# cv2.filter2D() and cv2.boxFilter() perform the same operation:
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)

# The function cv2.GaussianBlur() convolves the source image with the specified Gaussian kernel
# This kernel can be controlled using the parameters ksize (kernel size),
# sigmaX(standard deviation in the x direction of the gaussian kernel) and
# sigmaY (standard deviation in the y direction of the gaussian kernel)
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)

# The function cv2.medianBlur(), which blurs the image with a median kernel:
smooth_image_mb = cv2.medianBlur(image, 9)

# The function cv2.bilateralFilter() can be applied to the input image in order to apply a bilateral filter:
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
smooth_image_bf_2 = cv2.bilateralFilter(image, 9, 200, 200)

image_BGR_list = [image, smooth_image_f2D_5_5, smooth_image_f2D_10_10, smooth_image_b, smooth_image_bfi, smooth_image_gb,  smooth_image_mb, smooth_image_bf, smooth_image_bf_2]
title_list = ["original", "cv2.filter2D() (5,5) kernel", "cv2.filter2D() (10,10) kernel", "cv2.blur()", "cv2.boxFilter()", "cv2.GaussianBlur()", "cv2.medianBlur()", "cv2.bilateralFilter() - small values", "cv2.bilateralFilter() - big values"]
pos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Smoothing techniques", 3)