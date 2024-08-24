import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import constant_colors
from Utils import show_image

if __name__ == "__main__":
    # Create the canvas to draw: 120 x 512 pixels, 3 channels, uint8 (8-bit unsigned integers)
    # Set background to black using np.zeros():
    image = np.zeros((120, 512, 3), dtype="uint8")
    
    # If you want another background color you can do the following:
    # image[:] = colors['light_gray']
    image.fill(255)
    
    # We draw some text in the image:
    cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant_colors.RED, 2,
                cv2.LINE_4)
    cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant_colors.RED, 2,
                cv2.LINE_8)
    cv2.putText(image, 'Mastering OpenCV4 with Python', (40, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, constant_colors.RED, 2,
                cv2.LINE_AA)
    
    # Show image:
    show_image.show_with_matplotlib(image, 'cv2.putText()')
    
