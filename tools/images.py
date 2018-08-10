import matplotlib.pyplot as plt


def show_image(image_data):
    plt.figure()
    plt.imshow(image_data)
    plt.colorbar()
    plt.gca().grid(False)
    plt.show()
