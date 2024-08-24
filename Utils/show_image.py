import matplotlib.pyplot as plt

def show_with_matplotlib(img_BGR, title):
    # Convert BGR image to RGB:
    img_RGB = img_BGR[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()