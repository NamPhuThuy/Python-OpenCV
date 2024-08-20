import cv2

def print_pixel_value_of_image(img, id1, id2):
    (b, g, r) = img[id1, id2]

    # Print the values:
    print("Pixel at ({}, {}):".format(id1, id2))
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    
    # We can access only one channel at a time.
    b = img[0, 0, 0]
    g = img[0, 0, 1]
    r = img[0, 0, 2]
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    
def modify_pixel_of_image(img, id1, id2, r, g, b):
    img[id1, id2] = (r, g, b)

def show_image(image):
    img = cv2.resize(image, (400, 300))
    cv2.imshow("image", img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    img = cv2.imread('../images/3x3pixels.png')
    print_pixel_value_of_image(img, 0,0)
    # change_pixel_of_image(img, 0, 0, 255, 255, 255)
    
    show_image(img)
    # print_pixel_value_of_image(img, 0, 0)
