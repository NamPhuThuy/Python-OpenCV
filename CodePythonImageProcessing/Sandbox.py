import cv2

def save_hsv_channels(img, output_prefix):
    """Saves individual H, S, V channels as images.
  
    Args:
      img: The input image in BGR format.
      output_prefix: The prefix for the output image filenames.
    """

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Split into channels
    h, s, v = cv2.split(hsv)

    # Save channels
    cv2.imwrite(f"{output_prefix}_h.jpg", h)
    cv2.imwrite(f"{output_prefix}_s.jpg", s)
    cv2.imwrite(f"{output_prefix}_v.jpg", v)

# Load image
img = cv2.imread('Books.png')

# Save HSV channels
save_hsv_channels(img, 'output')