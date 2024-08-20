import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(img_OpenCV, img_matplotlib):
    # Show both images (img_OpenCV and img_matplotlib) using matplotlib
    # This will show the image in wrong color:
    plt.subplot(121)
    plt.imshow(img_OpenCV)
    plt.title('img OpenCV')
    # This will show the image in true color:
    plt.subplot(122)
    plt.imshow(img_matplotlib)
    plt.title('img matplotlib')
    plt.show()

def show_with_opencv(img_OpenCV, img_matplotlib):
    # To stack horizontally (img_OpenCV to the left of img_matplotlib):
    img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=1)

    # Now, we show the concatenated image:
    cv2.imshow('bgr image and rgb image', img_concats)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def show_with_numpy(img_OpenCV):
    # Using numpy capabilities to get the channels and two build the RGB image
    # Get the three channels (instead of using cv2.split):
    B = img_OpenCV[:, :, 0]
    G = img_OpenCV[:, :, 1]
    R = img_OpenCV[:, :, 2]

    # Transform the image BGR to RGB using Numpy capabilities:
    img_RGB = img_OpenCV[:, :, ::-1]

    # Now, we show the RGB image:
    cv2.imshow('img RGB (wrong color)', img_RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    img_OpenCV = cv2.imread('../images/wukong.jpg')
    img_OpenCV = cv2.resize(img_OpenCV, (600, 400))

    # Split the loaded image into its three channels (b, g, r):
    b, g, r = cv2.split(img_OpenCV)

    # Merge again the three channels but in the RGB format:
    img_matplotlib = cv2.merge([r, g, b])
    
    show_with_matplotlib(img_OpenCV, img_matplotlib)
    show_with_opencv(img_OpenCV, img_matplotlib)
    # show_with_numpy(img_OpenCV)
   