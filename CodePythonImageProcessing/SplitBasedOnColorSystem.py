import cv2
import numpy as np



def split_based_RGB():
    # Read the image
    img = cv2.imread('Avatar.png')
    
    
    # Resize image
    img = cv2.resize(img, (400, 300))
    
    # Split the image into its color channels
    b, g, r = cv2.split(img)
    
    # Convert the channels to numpy arrays
    b_np = np.array(b)
    g_np = np.array(g)
    r_np = np.array(r)
    
    # Print the shapes of the matrices
    print("Blue channel shape:", b_np.shape)
    print("Green channel shape:", g_np.shape)
    print("Red channel shape:", r_np.shape)
    
    # Display the color channels as images
    cv2.imshow("Blue", b)
    cv2.imshow("Green", g)
    cv2.imshow("Red", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def split_based_HSV():
    print(cv2.__version__)
    # Load image
    img = cv2.imread('Avatar.png')

    # Resize image
    img = cv2.resize(img, (400, 300))
    
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Split into channels
    h, s, v = cv2.split(hsv)
    
    # Display channels
    cv2.imshow("Hue", h)
    cv2.imshow("Saturation", s)
    cv2.imshow("Value", v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def split_and_save_based_HSV():
    # Load image
    img = cv2.imread('Books.png')
    output_prefix = 'output'

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Split into channels
    h, s, v = cv2.split(hsv)

    # Save channels
    cv2.imwrite(f"{output_prefix}_h.jpg", h)
    cv2.imwrite(f"{output_prefix}_s.jpg", s)
    cv2.imwrite(f"{output_prefix}_v.jpg", v)

def quantize_image(img, n_colors=8):
    """Quantizes an image into n_colors dominant colors.
  
    Args:
      img: The input image.
      n_colors: The number of colors to quantize to.
  
    Returns:
      A quantized image.
    """

    # Convert image to a 2D array of pixels
    pixels = img.reshape(-1, 3)

    # Apply K-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert back to image format
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res2 = res.reshape(img.shape)

    return res2

def show_color_matrices(img):
    """Shows the number-matrices of dominant colors in an image.
  
    Args:
      img: The input image.
    """

    # Quantize the image
    quantized_img = quantize_image(img)

    # Find unique colors
    unique_colors = np.unique(quantized_img.reshape(-1, 3), axis=0)

    for color in unique_colors:
        color_mask = np.all(quantized_img == color, axis=-1)
        color_matrix = color_mask.astype(np.uint8) * 255
        cv2.imshow(f"Color Matrix {color}", color_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    split_based_HSV()
    # # Load image
    # img = cv2.imread('image.jpg')
    # 
    # # Show color matrices
    # show_color_matrices(img)