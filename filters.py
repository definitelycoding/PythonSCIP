"""
 During one of the lessons we were taught to create image filters- looping through pixels to alter them
 I created my own filter: vintage_pink.
 I dived in further to check Pillow's functions and chose to use the brighten function as I think it fits the image.

"""

from simpleimage import SimpleImage
from PIL import Image, ImageEnhance


def vintage_pink(filename):
    """
    Reads image from file specified by filename.
    Turns image vintage pink by dividing red, green, blue values.
    Returns a new filter applied to the image.
    """
    # Looping through each pixel in the image,
    # Changing each pixel to a new pinkish colour.
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red // 1.3
        pixel.green = pixel.green // 1.5
        pixel.blue = pixel.blue // 1.2
    return image


def brighten_image(filename):
    """
    Reads image from file specified by filename.
    A variable picture is used to put the image in it for changes
    Using the built-in function ImageEnhance.Brightness to brighten the image
    Return the changed image.
    """
    picture = Image.open("images/BTS2.jpeg")
    enhancer = ImageEnhance.Brightness(picture)
    factor = 1.24 # factor<0 darkens the image and factor>0 brightens the image.
    brightened_picture = enhancer.enhance(factor)
    brightened_picture.save('brightened_BTS2.jpeg')

    return brightened_picture


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original_picture = SimpleImage('images/BTS2.jpeg')
    original_picture.show()

    pink_filter = vintage_pink('images/BTS2.jpeg')
    pink_filter.show()

    bright_filter = brighten_image('images/BTS2.jpeg')
    bright_filter.show()



if __name__ == '__main__':
    main()

