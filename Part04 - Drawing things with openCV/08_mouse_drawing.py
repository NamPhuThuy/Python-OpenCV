import cv2
import numpy as np
from Utils import constant_colors


# This is the mouse callback function:
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(image, (x, y), 10, constant_colors.MAGENTA, -1)

    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")

    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")

    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")


image = np.zeros((600, 600, 3), dtype="uint8")

# cv2.NamedWindow(), cv2.setMouseCallback(), cv2.imshow() should have the same windowName-parameter to work properly
windowName = 'Image mouse window'
cv2.namedWindow(windowName)

# Set a callback function to be called whenever a mouse event occurs within the specified window.
cv2.setMouseCallback(windowName, draw_circle)

while True:
    # Show image 'Image mouse':
    cv2.imshow(windowName, image)

    # Continue until 'q' is pressed:
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Destroy all generated windows:
cv2.destroyAllWindows()
