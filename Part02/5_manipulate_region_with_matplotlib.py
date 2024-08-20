import cv2
import matplotlib.pyplot as plt

def show_image_region(img, left, width, top, height):
    top_left_corner = img[left:(left + width), top:(top + height)]
    img_RGB = cv2.cvtColor(top_left_corner, cv2.COLOR_BGR2RGB)

    plt.imshow(img_RGB)
    plt.show()

def copy_image_region(img, left, width, top, height):
    top_left_corner = img[left:(left + width), top:(top + height)]
    # Copy this ROI into another region of the image:
    img[50:(50 + width), 50:(50 + height)] = top_left_corner

    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img_RGB)
    plt.show()

def change_image_region_color(img, left, width, top, height):
    # Wrong approach
    top_left_corner = img[left:(left + width), top:(top + height)]
    top_left_corner = (255, 0, 0)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img_RGB)
    plt.show()

    # Right approach
    img[left:(left + width), top:(top + height)] = (255, 0, 0)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img_RGB)
    plt.show()

if __name__ == "__main__":
    img = cv2.imread('../images/wukong.jpg')
    # show_image_region(img, 200, 300, 240, 300)
    # copy_image_region(img, 200, 300, 240, 300)
    change_image_region_color(img, 200, 300, 240, 300)
