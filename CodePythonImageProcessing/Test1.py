import cv2
import numpy as np

# Read the image
img = cv2.imread('books.png')


# Resize image
img = cv2.resize(img, (400, 300))

# Rotate 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90 degrees counterclockwise
# rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Rotate 180 degrees
# rotated_img = cv2.rotate(img, cv2.ROTATE_180)

# Rotate image
# M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 45, 1)
# rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Display the image
cv2.imshow('Rotated img', rotated_img)
# cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()