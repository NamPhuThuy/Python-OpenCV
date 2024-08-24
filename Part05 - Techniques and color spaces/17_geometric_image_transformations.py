"""Geometric image transformations"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from Utils import show_image

image = cv2.imread('../images/lena_image.png')

# 1. Scaling or resizing
# Resize the input image using cv2.resize()
# Resize using the scaling factor for each dimension of the image
# In this case the scaling factor is 0.5 in every dimension
scale_down = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Get the height and width of the image:
height, width = image.shape[:2]

# You can resize also the image specifying the new size:
scale_up = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)

# 2. Translation
# You need to create the 2x3 transformation matrix making use of numpy array with float values (float32)
# Translation in the x direction: 200 pixels, and a translation in the y direction: 30 pixels:
M = np.float32([[1, 0, 20], [0, 1, 10]])

# Once this transformation Matrix is created, we can pass it to the function cv2.warpAffine():
translated_image = cv2.warpAffine(image, M, (width, height))

# 3. Rotation
# To rotate the image we make use of the function  cv.getRotationMatrix2D() to build the 2x3 rotation matrix:
# In this case, we are going to rotate the image 180 degrees (upside down):
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 1)
rotated_180 = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(rotated_180, (round(width / 2.0), round(height / 2.0)), 5, (255, 0, 0), -1)

# Now, we are going to rotate the image 30 degrees changing the center of rotation
M = cv2.getRotationMatrix2D((width / 1.5, height / 1.5), 30, 1)
rotated_30 = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(rotated_30, (round(width / 1.5), round(height / 1.5)), 5, (255, 0, 0), -1)

M = cv2.getRotationMatrix2D((width / 1.5, height / 1.5), 60, 1)
rotated_60 = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(rotated_60, (round(width / 1.5), round(height / 1.5)), 5, (255, 0, 0), -1)

# 4. Affine Transformation
# In an affine transformation we first make use of the function cv2.getAffineTransform()
# to build the 2x3 transformation matrix, which is obtained from the relation between three points
# from the input image and their corresponding coordinates in the transformed image.

# A copy of the image is created to show the points that will be used for the affine transformation:
before_affline_image = image.copy()
cv2.circle(before_affline_image, (135, 45), 5, (255, 0, 255), -1)
cv2.circle(before_affline_image, (385, 45), 5, (255, 0, 255), -1)
cv2.circle(before_affline_image, (135, 230), 5, (255, 0, 255), -1)

# We create the arrays with the aforementioned three points and the desired positions in the output image:
pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])

# We get the 2x3 tranformation matrix based on pts_1 and pts_2 and apply cv2.warpAffine():
M = cv2.getAffineTransform(pts_1, pts_2)
after_affline_image = cv2.warpAffine(before_affline_image, M, (width, height))


# 5. Perspective transformation
# A copy of the image is created to show the points that will be used for the perspective transformation:
before_perspective = image.copy()
cv2.circle(before_perspective, (450, 65), 5, (255, 0, 255), -1)
cv2.circle(before_perspective, (517, 65), 5, (255, 0, 255), -1)
cv2.circle(before_perspective, (431, 164), 5, (255, 0, 255), -1)
cv2.circle(before_perspective, (552, 164), 5, (255, 0, 255), -1)

# cv2.getPerspectiveTransform() needs four pairs of points
# (coordinates of a quadrangle in both the source and output image)
# We create the arrays for these four pairs of points:
pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])

# To correct the perspective (also known as perspective transformation) you need to create the transformation matrix
# making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix is constructed:
M = cv2.getPerspectiveTransform(pts_1, pts_2)

# Then, apply cv2.warpPerspective(), where the source image is transformed applying
# the specified matrix and with a specified size:
after_perspective = cv2.warpPerspective(image, M, (300, 300))

# 6. Cropping
# A copy of the image is created to show the points that will be used for the cropping example:
before_cropping = image.copy()

# Show the points and lines connecting the points:
cv2.circle(before_cropping, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(before_cropping, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(before_cropping, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(before_cropping, (330, 200), 5, (0, 0, 255), -1)
cv2.line(before_cropping, (230, 80), (330, 80), (0, 0, 255))
cv2.line(before_cropping, (230, 200), (330, 200), (0, 0, 255))
cv2.line(before_cropping, (230, 80), (230, 200), (0, 0, 255))
cv2.line(before_cropping, (330, 200), (330, 80), (0, 0, 255))

# For cropping, we make use of numpy slicing:
after_cropping = image[80:200, 230:330]


image_BGR_list = [image, scale_down, scale_up, translated_image, rotated_180, rotated_30, rotated_60, before_affline_image, after_affline_image, before_perspective, after_perspective, before_cropping, after_cropping]
title_list = ['Original', 'Scale down', 'Scale up again', 'Translated image', 'Image rotated 180 degrees', 'Image rotated 30 degrees', 'Image rotated 60 degrees', 'before affine transformation', 'After affine transformation', 'Before perspective transformation', 'After perspective transformation', 'Before cropping', 'After cropping']
pos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Big title")