"""
File: blur.py
Name: Angel Chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: put the old and unprocessed image into this blur function.
    :return: return the picture, which was being blurred to the main function.
    """
    new_w = img.width
    new_h = img.height
    new_img = SimpleImage.blank(new_w, new_h)
    for x in range(0, new_w):
        for y in range(0, new_h):
            b = c = d = t = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if new_w > i >= 0 and new_h > j > 0:
                        z = new_img.get_pixel(x, y)
                        a = img.get_pixel(i, j)
                        b += a.red
                        c += a.green
                        d += a.blue
                        t += 1
                        if t == 9:
                            z.red = b / 9
                            z.green = c / 9
                            z.blue = d / 9
                        elif t == 6:
                            z.red = b / 6
                            z.green = c / 6
                            z.blue = d / 6
                        elif t == 4:
                            z.red = b / 4
                            z.green = c / 4
                            z.blue = d / 4
    return new_img


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


pass

if __name__ == '__main__':
    main()
