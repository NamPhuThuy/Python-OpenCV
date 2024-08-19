import cv2
def load_image(path):
    # cv2.imread(): read an image.
    # The image should be in the working directory or a full path of image should be provided.
    # load OpenCV logo image: 
    return cv2.imread(path)


def show_image(image):
    # cv2.imshow(): show an image in a window.
    # The window automatically fits to the image size.
    # First argument: window name.
    # Second argument: image to be displayed.
    # Each created window should have different window names.
    cv2.imshow("image", image)

    # cv2.waitKey() is a keyboard binding function.
    # Argument: time in milliseconds.
    # The function waits for specified milliseconds for any keyboard event.
    # If any key is pressed in that time, the program continues.
    # If 0 is passed, it waits indefinitely for a key stroke.
    # Wait indefinitely for a key stroke (in order to see the created window):
    cv2.waitKey(0)

    # To destroy all the windows we created
    cv2.destroyAllWindows()
    

def convert_to_grayscale(image):
    # Use cv2.cvtColor() to convert an image from one color format to another
    # In this case we use cv2.cvtColor() to convert the loaded image to grayscale (BGR to GRAY):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def write_image_to_disk(path, image):
    """this function writes to disk an image given the image to be written"""
    cv2.imwrite(path, image)


if __name__ == "__main__":
    bgr_image = load_image("../images/logo.png")
    show_image(bgr_image)
    
    gray_image = convert_to_grayscale(bgr_image)
    show_image(gray_image)

    write_image_to_disk("../images/gray_logo.png", gray_image)
