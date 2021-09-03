"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged   # pixel為list
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for i in range(len(pixels)):    # 計算出所有pixel中RGB的分別平均值，並將值return成一個list
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    return [red//len(pixels), green//len(pixels), blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    mini = float("inf")  # 設定此時的最小值是無限大
    average = get_average(pixels)
    red = average[0]   # RGB分別為average這個list的第1,2,3項
    green = average[1]
    blue = average[2]
    for i in range(len(pixels)):
        # 若此pixels的color_distance較小，則mini就要替換成此時的值，來搜尋整個pixels中最小的color_distance在哪裡
        if mini > get_pixel_dist(pixels[i], red, green, blue):
            pixels[0] = pixels[i]  # 將此pixel的值，存入pixel這個list的第一項，最後return第一項
            mini = get_pixel_dist(pixels[i], red, green, blue)
    return pixels[0]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # for i in range(0, len(images)):
    for x in range(result.width):
        for y in range(result.height):
            pixel = []   # 讓不同位置(不同(x, y)的pixel可以重新計算)
            for img in images:  # 將不同張照片、但同個位置的點存入pixel這個list中
                # pixel += [img.get_pixel(x, y)]
                pixel.append(img.get_pixel(x, y))
            best_pixel = get_best_pixel(pixel)  # 利用get_best_pixel找出pixel這個list中，最小的color_distance，即為最好的pixel
            result.set_pixel(x, y, best_pixel)  # set data

    # green_im = SimpleImage.blank(20, 20, "green")
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    # print(best1.red, best1.green, best1.blue)

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
