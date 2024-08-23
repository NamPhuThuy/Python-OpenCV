import cv2
import numpy as np

def rle_encode(img):
    """Encodes an image using Run-Length Encoding.

    Args:
        img: The input image as a NumPy array.

    Returns:
        A list of tuples, where each tuple contains the pixel value and its run length.
    """

    encoded_data = []
    prev_pixel = None
    run_length = 0

    for row in img:
        for pixel in row:
            if pixel != prev_pixel:
                if prev_pixel is not None:
                    encoded_data.append((prev_pixel, run_length))
                prev_pixel = pixel
                run_length = 1
            else:
                run_length += 1

    if prev_pixel is not None:
        encoded_data.append((prev_pixel, run_length))

    return encoded_data

def rle_decode(encoded_data, shape):
    """Decodes an RLE-encoded image.

    Args:
        encoded_data: The RLE-encoded data as a list of tuples.
        shape: The shape of the original image.

    Returns:
        The decoded image as a NumPy array.
    """

    decoded_img = np.zeros(shape, dtype=np.uint8)
    i = 0

    for pixel, run_length in encoded_data:
        decoded_img[i:i+run_length] = pixel
        i += run_length

    return decoded_img

if __name__ == "__main__":
    # Load an image
    img = cv2.imread('../images/avatar.png')
    # img = cv2.resize(img, (400, 300))

    # Convert to grayscale for simplicity
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Encode the image
    encoded_data = rle_encode(thresh)

    # Decode the image
    decoded_img = rle_decode(encoded_data, gray.shape)

    # Print the encoded data
    print_data = [(f"{pixel}", run_length) for pixel, run_length in encoded_data]

    print(print_data)
    
    
    # Display the original and decoded images
    # cv2.imshow('Original Image', gray)
    cv2.imshow('Decoded Image', decoded_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()