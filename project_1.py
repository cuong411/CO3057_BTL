from matplotlib.image import imread
import matplotlib.pyplot as plt

input_image = imread("dogo.jpg")
#input_image = imread("dogo_gray.jpg")

r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

def rgb2gray(input_image):
    r,g,b = input_image[:,:,0], input_image[:,:,1], input_image[:,:,2]

    grayscale_image = r_const * r + g_const * g + b_const * b

    plt.imshow(grayscale_image, cmap="gray")

    plt.imsave("dogo_gray.jpg", grayscale_image)

def gray2rgb(input_image):
    r,g,b = input_image[:,:,0], input_image[:,:,1], input_image[:,:,2]

    rgb_image = (1 / r_const) * r + (1 / g_const) * g + (1 / b_const) * b

    plt.imshow(rgb_image, cmap="rainbow")

    plt.imsave("dogo_color.jpg", rgb_image)

rgb2gray(input_image)
#gray2rgb(input_image)

plt.show()