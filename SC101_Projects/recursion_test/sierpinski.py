"""
File: sierpinski.py
Name: Angel Chen
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:  the number of inverted triangle, order1 is the biggest, and order2 is draw 3 inverted triangle in it.
	:param length: the length of the triangle
	:param upper_left_x: location x. every inverted triangle draws begin at the upper_left_x
	:param upper_left_y: location y. every inverted triangle draws begin at the upper_lefy y
	:return: draw numerous triangle, according to the order.
	"""
	if order == 0:
		# first triangle
		pass
	else:
		triangle1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		triangle2 = GLine(upper_left_x, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		triangle3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		window.add(triangle1)
		window.add(triangle2)
		window.add(triangle3)
		pause(100)
		# 左上
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# 右上
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# 下方
		sierpinski_triangle(order-1, length/2, 0.25*length + upper_left_x, 0.433*length + upper_left_y)


if __name__ == '__main__':
	main()