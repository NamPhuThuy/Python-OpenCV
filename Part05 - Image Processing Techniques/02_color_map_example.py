"""Example for testing colors maps in OpenCV"""
import cv2
import matplotlib.pyplot as plt
from Utils import show_image

# We load the image using cv2.imread() and using 'cv2.IMREAD_GRAYSCALE' argument:
gray_img = cv2.imread('../images/lenna.png', cv2.IMREAD_GRAYSCALE)

# We apply the color map 'cv2.COLORMAP_HSV'
img_COLORMAP_HSV = cv2.applyColorMap(gray_img, cv2.COLORMAP_HSV)

image_BGR_list = [cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR), img_COLORMAP_HSV]
title_list = ["Gray image", 'HSV Image']
pos_list = [1, 2]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Colormaps", 2)