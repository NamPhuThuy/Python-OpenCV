"""Example for testing all colors maps in OpenCV"""
import cv2
import matplotlib.pyplot as plt
from Utils import show_image

gray_img = cv2.imread('../images/lenna.png', cv2.IMREAD_GRAYSCALE)

# We define all the color map names to be used later:
colormaps = ["AUTUMN", "BONE", "JET", "WINTER", "RAINBOW", "OCEAN", "SUMMER", "SPRING", "COOL", "HSV", "HOT", "PINK",
             "PARULA"]

# We create a figure() object with appropriate size and title
plt.figure(figsize=(12, 5))
plt.suptitle("", fontsize=14, fontweight='bold')

image_BGR_list = [cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)]
title_list = ['GRAY']
pos_list = [1]

# Now we iterate to apply all the colormaps and add the Figure:
for idx, val in enumerate(colormaps):
    # print("idx: {}, val: {}".format(idx, val))
    image_BGR_list.append(cv2.applyColorMap(gray_img, idx))
    title_list.append(val)
    pos_list.append(idx + 2)
    # show_with_matplotlib(cv2.applyColorMap(gray_img, idx), val, idx + 2)

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Colormaps", 7)