import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('../images/wukong.jpg', cv2.IMREAD_GRAYSCALE)
dimensions = gray_img.shape
print(dimensions)

# gray_image.shape doesn't have channels-attribute
(h, w) = gray_img.shape
print("Dimensions of the image - Height: {}, Width: {}".format(h, w))
total_number_of_pixels = gray_img.size
print("Total number of elements: {}".format(total_number_of_pixels))
print("Total number of elements: {}".format(h * w))

image_dtype = gray_img.dtype
print("Image datatype: {}".format(image_dtype))

cv2.startWindowThread()
cv2.imshow("original image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Matplotlib
plt.imshow(gray_img, cmap='gray')
plt.show()

i = gray_img[6, 40]
print("Pixel at (6,40) - Intensity: {}".format(i))

gray_img[6, 40] = 0
i = gray_img[6, 40]
print("Pixel at (6,40) - Intensity: {}".format(i))

top_left_corner = gray_img[0:300, 0:300]
plt.imshow(top_left_corner,cmap='gray')
plt.show()

gray_img[100:400, 100:400] = top_left_corner
plt.imshow(gray_img, cmap='gray')
plt.show()

gray_img[100:500, 100:500] = 0
plt.imshow(gray_img, cmap='gray')
plt.show()