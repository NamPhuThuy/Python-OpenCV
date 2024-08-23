import cv2
import matplotlib.pyplot as plt

def show_image_with_matplotlib(img):
    # If you run an interactive ipython session, and want to use highgui windows, do cv2.startWindowThread() first.
    cv2.startWindowThread()
    # cv2.imshow("original image", img)

    # OpenCV works with BGR image space -> color images are stored in three channels (B,G,R) following this specific order. So, when you load an image using OpenCV cv2.imread(), it loads that image into BGR color space by default. 
    # Matplotlib used the RGB space, so we have to convert the BGR image to RGB. To do this, we will use **cv2.cvtColor()** to convert the image from the BGR color space to RGB. Let's do it
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Two different images
    plt.imshow(img)
    plt.show()

    plt.imshow(img_RGB)
    plt.show()
    


if __name__ == "__main__":
    img = cv2.imread('../images/wukong.jpg')
    show_image_with_matplotlib(img)
    # show_image_region_with_matplotlib(img, 200, 300, 240, 300)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
   