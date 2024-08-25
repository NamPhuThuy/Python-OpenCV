"""Example for testing custom colors maps in OpenCV and ploting the legend"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_image

def build_lut_image(cmap, height):
    """Builds the legend image"""

    lut = build_lut(cmap)
    image = np.repeat(lut[np.newaxis, ...], height, axis=0)

    return image


def build_lut(cmap):
    """Builds look up table based on 'key colors' using np.linspace()"""

    lut = np.empty(shape=(256, 3), dtype=np.uint8)
    max = 256
    # build lookup table:
    lastval, lastcol = cmap[0]
    for step, col in cmap[1:]:
        val = int(step * max)
        for i in range(3):
            lut[lastval:val, i] = np.linspace(lastcol[i], col[i], val - lastval)

        lastcol = col
        lastval = val

    return lut


def apply_color_map_1(gray, cmap):
    """Applies a custom color map using cv2.LUT()"""

    lut = build_lut(cmap)
    s0, s1 = gray.shape
    out = np.empty(shape=(s0, s1, 3), dtype=np.uint8)

    for i in range(3):
        out[..., i] = cv2.LUT(gray, lut[:, i])
    return out


def apply_color_map_2(gray, cmap):
    """Applies a custom color map using cv2.applyColorMap()"""

    lut = build_lut(cmap)
    lut2 = np.reshape(lut, (256, 1, 3))
    im_color = cv2.applyColorMap(gray, lut2)
    return im_color

# Read grayscale image:
gray_img = cv2.imread('../images/lenna.png', cv2.IMREAD_GRAYSCALE)

# Build the color maps (b,g,r) values:
custom_1 = apply_color_map_1(gray_img, ((0, (255, 0, 255)), (0.25, (255, 0, 180)), (0.5, (255, 0, 120)),
                                        (0.75, (255, 0, 60)), (1.0, (255, 0, 0))))

custom_2 = apply_color_map_2(gray_img, ((0, (0, 255, 128)), (0.25, (128, 184, 64)), (0.5, (255, 128, 0)),
                                        (0.75, (64, 128, 224)), (1.0, (0, 128, 255))))

# Build the legend images:
legend_1 = build_lut_image(((0, (255, 0, 255)), (0.25, (255, 0, 180)), (0.5, (255, 0, 120)),
                            (0.75, (255, 0, 60)), (1.0, (255, 0, 0))), 20)

legend_2 = build_lut_image(((0, (0, 255, 128)), (0.25, (128, 184, 64)), (0.5, (255, 128, 0)),
                            (0.75, (64, 128, 224)), (1.0, (0, 128, 255))), 20)

image_BGR_list = [legend_1, custom_1, legend_2, custom_2]
title_list = ["", "", "", ""]
pos_list = [1, 3, 2, 4]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Custom color maps based on key colors and legend", 2)