import cv2
import numpy as np
import matplotlib.pyplot as plt
import constant_colors


def show_with_matplotlib(img, title):
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    
    # We create the canvas to draw: 400 x 1200 pixels, 3 channels, uint8 (8-bit unsigned integers)
    # We set background to black using np.zeros():
    image = np.zeros((400, 1200, 3), dtype="uint8")
    
    # If you want another background color you can do the following:
    image[:] = constant_colors.LIGHT_GRAY
    
    # Assign parameters to be used in the drawing functions:
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5
    thickness = 5
    text = 'abcdefghijklmnopqrstuvwxyz'
    circle_radius = 10
    
    # We get the size of the text:
    ret, baseline = cv2.getTextSize(text, font, font_scale, thickness)
    
    # We get the text width and text height from ret:
    text_width, text_height = ret
    
    # We center the text in the image:
    text_x = int(round((image.shape[1] - text_width) / 2))
    text_y = int(round((image.shape[0] + text_height) / 2))
    
    # Draw this point for reference:
    cv2.circle(image, (text_x, text_y), circle_radius, constant_colors.GREEN, -1)
    
    # Draw the rectangle (bounding box of the text):
    cv2.rectangle(image, (text_x, text_y + baseline), (text_x + text_width - thickness, text_y - text_height),
                  constant_colors.BLUE, thickness)
    
    # Draw the circles defining the rectangle:
    cv2.circle(image, (text_x, text_y + baseline), circle_radius, constant_colors.RED, -1)
    cv2.circle(image, (text_x + text_width - thickness, text_y - text_height), circle_radius, constant_colors.CYAN, -1)
    
    # Draw the baseline line:
    cv2.line(image, (text_x, text_y + int(round(thickness / 2))), (text_x + text_width - thickness, text_y +
                                                                   int(round(thickness / 2))), constant_colors.YELLOW, thickness)
    # Write the text centered in the image:
    cv2.putText(image, text, (text_x, text_y), font, font_scale, constant_colors.MAGENTA, thickness)
    
    # Show image:
    show_with_matplotlib(image, 'cv2.getTextSize() + cv2.putText()')
