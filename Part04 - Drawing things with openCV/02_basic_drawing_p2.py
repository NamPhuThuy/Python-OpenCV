import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import constant_colors


def show_with_matplotlib(img, title):
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

    
def cliplines_example():
    
    # two points of the line
    linep1 = (0, 0)
    linep2 = (300, 300)
    
    # two points of the rectangle
    rectp1 = (0, 0)
    rectp2 = (100, 100)
    
    # Draw a rectangle and a line:
    cv2.line(image, linep1, linep2, constant_colors.GREEN, 3)
    cv2.rectangle(image, rectp1, rectp2, constant_colors.BLUE, 3)
    
    # We call the function cv2.clipLine():
    ret, p1, p2 = cv2.clipLine((rectp1 + rectp2), linep1, linep2)
    # ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), linep1, linep2)
    
    # cv2.clipLine() returns False if the line is outside the rectangle
    # And returns True otherwise
    if ret:
        cv2.line(image, p1, p2, constant_colors.YELLOW, 3)
    
    show_with_matplotlib(image, 'cv2.clipLine()')
    image[:] = constant_colors.LIGHT_GRAY
    
def arrowedLine_example():
    # 2. We are going to see how cv2.arrowedLine() works:
    cv2.arrowedLine(image, (50, 50), (200, 50), constant_colors.RED, 3, 8, 0, 0.1)
    cv2.arrowedLine(image, (50, 120), (200, 120), constant_colors.GREEN, 3, cv2.LINE_AA, 0, 0.3)
    cv2.arrowedLine(image, (50, 200), (200, 200), constant_colors.BLUE, 3, 8, 0, 0.3)
    
    show_with_matplotlib(image, 'cv2.arrowedLine()')
    image[:] = colors['light_gray']

def ellipse_example():    
    # 3. We are going to see how cv2.ellipse() works:
    cv2.ellipse(image, (80, 80), (60, 40), 0, 0, 360, constant_colors.RED, -1)
    cv2.ellipse(image, (80, 200), (80, 40), 0, 0, 360, constant_colors.GREEN, 3)
    cv2.ellipse(image, (80, 200), (10, 40), 0, 0, 360, constant_colors.BLUE, 3)
    cv2.ellipse(image, (200, 200), (10, 40), 0, 0, 180, constant_colors.YELLOW, 3)
    cv2.ellipse(image, (200, 100), (10, 40), 0, 0, 270, constant_colors.CYAN, 3)
    cv2.ellipse(image, (250, 250), (30, 30), 0, 0, 360, constant_colors.MAGENTA, 3)
    cv2.ellipse(image, (250, 100), (20, 40), 45, 0, 360, constant_colors.GRAY, 3)

    show_with_matplotlib(image, 'cv2.ellipse()')
    image[:] = constant_colors.LIGHT_GRAY

def polylines_example():
    # 4. We are going to draw several polylines
    # These points define a triangle:
    pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes: this line is not necessary, only for visualization:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with True option:
    cv2.polylines(image, [pts], True, constant_colors.GREEN, 3)
    
    # These points define a triangle:
    pts = np.array([[250, 105], [220, 180], [280, 180]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with False option:
    cv2.polylines(image, [pts], False, constant_colors.GREEN, 3)
    
    # These points define a pentagon:
    pts = np.array([[20, 90], [60, 60], [100, 90], [80, 130], [40, 130]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with True option:
    cv2.polylines(image, [pts], True, constant_colors.BLUE, 3)
    
    # These points define a pentagon:
    pts = np.array([[20, 180], [60, 150], [100, 180], [80, 220], [40, 220]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with False option:
    cv2.polylines(image, [pts], False, constant_colors.BLUE, 3)
    
    # These points define a rectangle:
    pts = np.array([[150, 100], [200, 100], [200, 150], [150, 150]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with False option:
    cv2.polylines(image, [pts], True, constant_colors.YELLOW, 3)
    
    # These points define a rectangle:
    pts = np.array([[150, 200], [200, 200], [200, 250], [150, 250]], np.int32)
    # Reshape to shape (number_vertex, 1, 2)
    pts = pts.reshape((-1, 1, 2))
    # Print the shapes:
    print("shape of pts '{}'".format(pts.shape))
    # Draw this polygon with False option:
    cv2.polylines(image, [pts], False, constant_colors.YELLOW, 3)
    
    show_with_matplotlib(image, 'cv2.polylines()')
    image[:] = constant_colors.LIGHT_GRAY
    
def circle_polygon_example():
    # We create the canvas to draw: 640 x 640 pixels, 3 channels, uint8 (8-bit unsigned integers)
    # We set background to black using np.zeros():
    image = np.zeros((640, 640, 3), dtype="uint8")
    
    # If you want another background color you can do the following:
    # image[:] = colors['light_gray']
    image.fill(255)
    
    # Create the necessary (12 in this case) points to build the circle polygon:
    pts = np.array(
        [(600, 320), (563, 460), (460, 562), (320, 600), (180, 563), (78, 460), (40, 320), (77, 180), (179, 78), (319, 40),
         (459, 77), (562, 179)])
    
    # Reshape to shape (number_vertex, 1, 2):
    pts = pts.reshape((-1, 1, 2))
    
    # Call cv2.polylines() to build the polygon:
    cv2.polylines(image, [pts], True, constant_colors.GREEN, 5)
    
    # Show image:
    show_with_matplotlib(image, 'polygon with the shape of a circle using 12 points')

if __name__ == "__main__":
    image = np.zeros((300, 300, 3), dtype="uint8")
    image[:] = constant_colors.LIGHT_GRAY
    
    # cliplines_example()
    # arrowedLine_example()
    # ellipse_example()
    # polylines_example()
    circle_polygon_example()
    