import cv2



def show_region_of_image(img, left, width, top, height):
    

    # Get the top left corner of the image
    top_left_corner = img[left:(left + width), top:(top + height)]

    cv2.imshow("top left corner original", top_left_corner)

def copy_region_of_image(img, left, width, top, height):
    top_left_corner = img[left:(left + width), top:(top + height)]
    # Copy this ROI into another region of the image:
    img[50:(50 + width), 50:(50 + height)] = top_left_corner

    # We show the modified image:
    cv2.imshow("modified image", img)
    
def change_region_color(img, left, width, top, height):
    top_left_corner = img[left:(left + width), top:(top + height)]

    # Set top left corner of the image to blue
    img[0:250, 0:250] = (255, 0, 0)

    # Show modified image;
    cv2.imshow("modified image", img)
    
def highlight_region(img, left, width, top, height):
    img = cv2.rectangle(img, (left, top), (left + width, top + height), (0, 255, 0), 2)
    cv2.imshow('img', img)

if __name__ == "__main__":
    img = cv2.imread("../images/wukong.jpg")
    # show_region_of_img(img, 200, 300, 240, 300)
    copy_region_of_image(img, 200, 300, 240, 300)
    # change_region_color(img, 200, 300, 240, 300)
    # highlight_region(img, 200, 300, 240, 300)
    cv2.waitKey(0)
