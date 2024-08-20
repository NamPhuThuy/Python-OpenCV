import cv2

img = cv2.imread('../images/wukong.jpg')

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