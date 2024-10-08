import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import constant_colors

# Getting red color:
print("red: '{}'".format(constant_colors.RED))

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

if __name__ == "__main__": 
    # We create the canvas to draw: 500 x 500 pixels, 3 channels, uint8 (8-bit unsigned integers)
    # We set background to black using np.zeros():
    image = np.zeros((500, 500, 3), dtype="uint8")
    
    # If you want another background color you can do the following:
    image[:] = colors['light_gray']
    
    # We draw all the colors to test the dictionary
    # We draw some lines each one in one color. To get the color use 'colors[key]'
    separation = 40
    for key in colors:
        # Draw a line using the function cv2.line():
        cv2.line(image, (0, separation), (500, separation), colors[key], 10)
        separation += 40
    
    # Show image:
    show_with_matplotlib(image, 'Dictionary with some predefined colors')
