import cv2
import numpy as np

def bit_plane_slicing(image, plane):
    """
    Performs bit-plane slicing on an image.

    Args:
        image: The input image.
        plane: The bit plane to extract (0-7 for 8-bit images).

    Returns:
        The extracted bit plane.
    """

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the specified bit plane
    mask = 1 << plane
    bit_plane = (gray & mask) >> plane

    return bit_plane

# Load the image
image = cv2.imread('../images/cat-face.png')

# Extract bit planes 0-7
bit_planes = [bit_plane_slicing(image, i) for i in range(8)]

# Display the bit planes
for i, bit_plane in enumerate(bit_planes):
    cv2.imshow(f'Bit Plane {i}', bit_plane)
    cv2.waitKey(0)

cv2.destroyAllWindows()