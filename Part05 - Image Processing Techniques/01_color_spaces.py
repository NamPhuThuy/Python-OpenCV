"""Introduction to color spaces in OpenCV"""
import cv2
import matplotlib.pyplot as plt
from Utils import show_image

image = cv2.imread('../images/color_spaces.png')

# Convert to grayscale:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the b, g, and r components from the loaded image:
(bgr_b, bgr_g, bgr_r) = cv2.split(image)

# Convert to HSV and get the components:
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(hsv_h, hsv_s, hsv_v) = cv2.split(hsv_image)

# Convert to HLS and get the components:
hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
(hls_h, hls_l, hls_s) = cv2.split(hls_image)

# Convert to YCrCb and get the components:
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
(ycrcb_y, ycrcb_cr, ycrcb_cb) = cv2.split(ycrcb_image)

# Convert to L*a*b and get the components:
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
(lab_l, lab_a, lab_b) = cv2.split(lab_image)

image_BGR_list = [image, cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(bgr_b, cv2.COLOR_GRAY2BGR), cv2.cvtColor(bgr_g, cv2.COLOR_GRAY2BGR), cv2.cvtColor(bgr_r, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(hsv_h, cv2.COLOR_GRAY2BGR), cv2.cvtColor(hsv_s, cv2.COLOR_GRAY2BGR), cv2.cvtColor(hsv_v, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(hls_h, cv2.COLOR_GRAY2BGR), cv2.cvtColor(hls_l, cv2.COLOR_GRAY2BGR), cv2.cvtColor(hls_s, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(ycrcb_y, cv2.COLOR_GRAY2BGR), cv2.cvtColor(ycrcb_cr, cv2.COLOR_GRAY2BGR), cv2.cvtColor(ycrcb_cb, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(lab_l, cv2.COLOR_GRAY2BGR), cv2.cvtColor(lab_a, cv2.COLOR_GRAY2BGR), cv2.cvtColor(lab_b, cv2.COLOR_GRAY2BGR)]

title_list = ["BGR - image", "gray image", 
              "BGR - B comp", "BGR - G comp", "BGR - R comp",
              "HSV - H comp", "HSV - S comp", "HSV - V comp",
              "HLS - H comp", "HLS - L comp", "HLS - S comp",
              "YCrCb - Y comp", "YCrCb - Cr comp", "YCrCb - Cb comp",
              "L*a*b - L comp", "L*a*b - a comp", "L*a*b - b comp"]

pos_list = [1, 1 + 6, 
            2, 2 + 6, 2 + 6 * 2,
            3, 3 + 6, 3 + 6 * 2,
            4, 4 + 6, 4 + 6 * 2,
            5, 5 + 6, 5 + 6 * 2,
            6, 6 + 6, 6 + 6 * 2]

show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Color spaces in OpenCV", 6)