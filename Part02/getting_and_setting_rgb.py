"""
Accessing, manipulating pixels in OpenCV (getting and setting methods) with BGR images
"""

# import the necessary packages
import cv2

img = cv2.imread('../images/avatar.png')

# img.shape: get the dimensions of the image use 
# If color image: returns a tuple of number of rows, columns and channels
# If grayscale image: returns a tuple of number of rows and columns
dimensions = img.shape
print(dimensions)
# This will print '(99, 82, 3)'

# Get height, width and the number of channels of the input image
(h, w, c) = img.shape
print("Dimensions of the image - Height: {}, Width: {}, Channels: {}".format(h, w, c))
# This will print 'Dimensions of the image - Height: 99, Width: 82, Channels: 3'

# Total number of elements is obtained by img.size:
total_number_of_pixels = img.size
print("Total number of elements: {}".format(total_number_of_pixels))
# This will print 'Total number of pixels: 24354'

# The total number of pixels is equal to the multiplication of 'height', 'width' and 'channels':
print("Total number of elements: {}".format(h * w * c))
# This will print 'Total number of pixels: 24354'

# Image datatype is obtained by img.dtype.
# img.dtype is very important because a large number of errors is caused by invalid datatype.
image_dtype = img.dtype
print("Image datatype: {}".format(image_dtype))
# This should print 'Image datatype: uint8', (uint8) = unsigned char

cv2.imshow("original image", img)

cv2.waitKey(0)

# You can access a pixel value by row and column coordinates.
# For BGR image, it returns an array of (Blue, Green, Red) values.
# Get the value of the pixel (x=40, y=6):
(b, g, r) = img[6, 40]

# Print the values:
print("Pixel at (6,40) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# This will print 'Pixel at (6,40) - Red: 247, Green: 18, Blue: 36'

# We can access only one channel at a time.
# In this case, we will use row, column and the index of the desired channel for indexing.
# Get only blue value of the pixel (x=40, y=6):
b = img[6, 40, 0]

# Get only green value of the pixel (x=40, y=6):
g = img[6, 40, 1]

# Get only red value of the pixel (x=40, y=6):
r = img[6, 40, 2]

# Print the values again:
print("Pixel at (6,40) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# This will print 'Pixel at (6,40) - Red: 247, Green: 18, Blue: 36'

# You can modify the pixel values of the image in the same way.
# Set the pixel to red ((b - g - r) format):
img[6, 40] = (0, 0, 255)

# Get the value of the pixel (x=40, y=6) after modifying it
(b, g, r) = img[6, 40]

# Print it:
print("Pixel at (6,40) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# This will print 'Pixel at (6,40) - Red: 255, Green: 0, Blue: 0'

# Sometimes, you will have to play with certain region of images rather than one pixel at a time
# In this case, we get the top left corner of the image:
top_left_corner = img[0:50, 0:50]

# We show this ROI:
cv2.imshow("top left corner original", top_left_corner)

# Wait indefinitely for a key stroke (in order to see the created window):
cv2.waitKey(0)

# Copy this ROI into another region of the image:
img[20:70, 20:70] = top_left_corner

# We show the modified image:
cv2.imshow("modified image", img)

# Wait indefinitely for a key stroke (in order to see the created window):
cv2.waitKey(0)

# Set top left corner of the image to blue
img[0:50, 0:50] = (255, 0, 0)

# Show modified image;
cv2.imshow("modified image", img)

# Wait indefinitely for a key stroke (in order to see the created windows):
cv2.waitKey(0)
