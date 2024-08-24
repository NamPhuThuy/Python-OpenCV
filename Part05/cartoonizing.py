"""
Cartoonizing images using both custom and OpenCV functions
"""
import cv2
import matplotlib.pyplot as plt
from Utils import show_image

def sketch_image(img):
    """Sketches the image applying a laplacian operator to detect the edges"""
    
    # Convert to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filter
    img_gray = cv2.medianBlur(img_gray, 5)

    # Detect edges using cv2.Laplacian()
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)

    # Threshold the edges image:
    ret, thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    return thresholded


def cartonize_image(img, gray_mode=False):
    """Cartoonizes the image applying cv2.bilateralFilter()"""

    # Get the sketch:
    thresholded = sketch_image(img)

    # Apply bilateral filter with "big numbers" to get the cartoonized effect:
    filtered = cv2.bilateralFilter(img, 10, 250, 250)

    # Perform 'bitwise and' with the thresholded img as mask in order to set these values to the output
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)

    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)

    return cartoonized

image = cv2.imread('../images/avatar.png')

# Call the created functions for sketching and cartoonizing images:
custom_sketch_image = sketch_image(image)
custom_cartonized_image = cartonize_image(image)
custom_cartonized_image_gray = cartonize_image(image, True)

# Call the OpenCV functions to get a similar output:
sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=30, sigma_r=0.1, shade_factor=0.1)
stylizated_image = cv2.stylization(image, sigma_s=60, sigma_r=0.07)

# Create lists and add to the method
image_BGR_list = [image, cv2.cvtColor(custom_sketch_image, cv2.COLOR_GRAY2BGR), cv2.cvtColor(sketch_gray, cv2.COLOR_GRAY2BGR), sketch_color, stylizated_image, custom_cartonized_image, cv2.cvtColor(custom_cartonized_image_gray, cv2.COLOR_GRAY2BGR)]
title_list = ["image", "custom sketch", "sketch gray cv2.pencilSketch()", "sketch color cv2.pencilSketch()", "cartoonized cv2.stylization()", "custom cartoonized", "custom cartoonized gray"]
pos_list = [1, 2, 3, 4, 5, 6, 7]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Cartoonizing images")
