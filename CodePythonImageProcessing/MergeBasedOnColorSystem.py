import cv2
import numpy as np

def merge_hsv_channels():
    # Load individual channels
    h = cv2.imread('output_h.jpg')
    s = cv2.imread('output_s.jpg')
    v = cv2.imread('output_v.jpg')

    # Ensure all channels have the same shape
    h, s, v = [cv2.resize(channel, (v.shape[1], v.shape[0])) for channel in [h, s, v]]

    # Merge channels
    hsv_image = cv2.merge([h, s, v])
    cv2.imshow('Temp', hsv_image)
    # hsv_image.astype(np.uint8)
    # 
    # # Convert to BGR for display (if needed)
    # merged_bgr = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    # # 
    # cv2.imshow('Merged HSV Image', merged_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return hsv_image

if __name__ == "__main__":
    merge_hsv_channels()