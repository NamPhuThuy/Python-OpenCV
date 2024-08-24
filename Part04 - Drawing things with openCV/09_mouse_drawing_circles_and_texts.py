import cv2
import numpy as np
from Utils import constant_colors


# Mouse callback function:
def draw_text():
    # Set the position to be used for drawing text:
    menu_pos = (10, 500)
    menu_pos2 = (10, 525)
    menu_pos3 = (10, 550)
    menu_pos4 = (10, 575)

    # Write the menu:
    cv2.putText(image, 'Double left click: add a circle', menu_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Single right click: delete last circle', menu_pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255))
    cv2.putText(image, 'Double right click: delete all circle', menu_pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255))
    cv2.putText(image, 'Press \'q\' to exit', menu_pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))

# Mouse callback function:
def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Add the circle with coordinates x,y
        print("event: EVENT_LBUTTONDBLCLK")
        circles.append((x, y))
    if event == cv2.EVENT_RBUTTONDBLCLK:
        # Delete all circles (clean the screen)
        print("event: EVENT_RBUTTONDBLCLK")
        circles[:] = []
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Delete last added circle
        print("event: EVENT_RBUTTONDOWN")
        try:
            circles.pop()
        except (IndexError):
            print("no circles to delete")
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")


# Structure to hold the created circles:
circles = []

image = np.zeros((600, 600, 3), dtype="uint8")
cv2.namedWindow('Image mouse')

# We set the mouse callback function to 'draw_circle':
cv2.setMouseCallback('Image mouse', draw_circle)

# We draw the menu:
draw_text()

# We get a copy with only the text printed in it:
clone = image.copy()

while True:

    # We 'reset' the image (to get only the image with the printed text):
    image = clone.copy()

    # We draw now only the current circles:
    for pos in circles:
        # We print the circle (filled) with a  fixed radius (30):
        cv2.circle(image, pos, 30, constant_colors.BLUE, -1)

    # Show image 'Image mouse':
    cv2.imshow('Image mouse', image)

    # Continue until 'q' is pressed:
    if cv2.waitKey(400) & 0xFF == ord('q'):
        break

# Destroy all generated windows:
cv2.destroyAllWindows()
