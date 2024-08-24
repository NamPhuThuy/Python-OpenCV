import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import constant_colors
import Utils

def draw_lines_example():
    cv2.line(image, (0, 0), (400, 400), constant_colors.GREEN, 3)
    cv2.line(image, (0, 400), (400, 0), constant_colors.BLUE, 3)
    cv2.line(image, (200, 0), (200, 400), constant_colors.RED, 10)
    cv2.line(image, (0, 200), (400, 200), constant_colors.YELLOW, 10)

    Utils.show_image.show_with_matplotlib(image, 'cv2.line()')

    # Clean the canvas to draw again:
    image[:] = constant_colors.LIGHT_GRAY




def draw_rectangles_example():
    cv2.rectangle(image, (10, 50), (60, 300), constant_colors.GREEN, 3)
    cv2.rectangle(image, (80, 50), (130, 300), constant_colors.BLUE, -1)
    cv2.rectangle(image, (150, 50), (350, 100), constant_colors.RED, -1)
    cv2.rectangle(image, (150, 150), (350, 300), constant_colors.CYAN, 10)

    Utils.show_image.show_with_matplotlib(image, 'cv2.rectangle()')

    image[:] = constant_colors.LIGHT_GRAY
    
def draw_circles_example():
    # 3. We are going to see how cv2.circle() works:
    cv2.circle(image, (50, 50), 20, constant_colors.GREEN, 3)
    cv2.circle(image, (100, 100), 30, constant_colors.BLUE, -1)
    cv2.circle(image, (200, 200), 40, constant_colors.MAGENTA, 10)
    cv2.circle(image, (300, 300), 40, constant_colors.CYAN, -1)
    
    Utils.show_image.show_with_matplotlib(image, 'cv2.circle()')

if __name__ == "__main__":
    # Create the canvas to draw: 400 x 400 pixels, 3 channels, uint8
    # Set the background to black using np.zeros():
    image = np.zeros((400, 400, 3), dtype="uint8")
    
    # If you want another background color you can do the following:
    image[:] = constant_colors.LIGHT_GRAY

    # Show image:
    Utils.show_image.show_with_matplotlib(image, '')
    
    
    draw_lines_example()
    draw_rectangles_example()
    draw_circles_example()

