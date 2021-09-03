"""
File: draw_line
Name: Angel Chen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
pit = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(hole)


def hole(first):  # 按第一下時，創造一個空心圓圈
    pit.filled = False
    window.add(pit, x=first.x-SIZE/2, y=first.y-SIZE/2)
    onmouseclicked(line)


def line(second):   # 按第二下時，將第二點的位置與第一點的位置連成一線，並移除第一點的空心圓圈
    link = GLine(pit.x+SIZE/2, pit.y+SIZE/2, second.x, second.y)
    window.add(link)
    window.remove(pit)
    onmouseclicked(hole)  # 創造完一條線，之後下一次要回去hole，創一個空心圓

    pass


if __name__ == "__main__":
    main()
