"""
File:  bouncing_ball
Name:  Angel Chen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # 球的水平速度
DELAY = 10  # 動畫停格多少毫秒(ms)
GRAVITY = 1  # 模擬重力加速度
SIZE = 20  # 球的直徑
REDUCE = 0.9  # 每一次反彈，球垂直速度所剩的比例
START_X = 30  # 球的起始值x
START_Y = 40  # 球的起始值y
vy = 0  # 球的初始垂直速度
total = 0  # 執行這個程式的次數

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)  # 將實心球放入視窗的設定初始值
    onmouseclicked(bounce)
    pass


def bounce(mouse):
    global total, vy
    if ball.x == START_X and ball.y == START_Y:  # 如果點擊時，球在初始值，就繼續進行下列程式
        total += 1  # 程式執行次數+1
        while ball.x <= window.width and total <= 3:  # 若球的水平方向的再視窗內，且執行次數還未超過三次，則進行以下程式
            if ball.y + SIZE < window.height:   # 球的高度在視窗內
                vy += GRAVITY
            else:   # 球的高度超過視窗，需要反彈
                if vy > 0:  # 若球的方向是向下的話，要反方向運動，且速度會折損
                    vy = -vy*REDUCE
            ball.move(VX, vy)
            pause(DELAY)
        ball.x = START_X  # 球超過邊界或已經執行三次了，則球回到初始座標
        ball.y = START_Y
    else:
        pass


# def not_disturb(same):
#     if ball.x != START_X and ball.y != START_Y:  # 點擊時球不在初始位置，不干擾球
#         pass
#     else:
#         bounce(same)   # 球在初始位置，重新運動
#     pass



#
#
# def bounce(m):
#     global START_X, START_Y
#     n = 0
#     ball.filled = True
#     window.add(ball, START_X, START_Y)
#     while True:
#         if START_X < 800:
#             if START_Y < 500:
#                 n += 1
#                 pause(DELAY)
#                 window.clear()
#                 window.add(ball, START_X, START_Y)
#                 pause(DELAY)
#                 START_X += VX
#                 START_Y += GRAVITY*n


# def main():
#     """
#     This program simulates a bouncing ball at (START_X, START_Y)
#     that has VX as x velocity and 0 as y velocity. Each bounce reduces
#     y velocity to REDUCE of itself.
#     """
#     ball.filled = True
#     window.add(ball, START_X, START_Y)
#     onmouseclicked(move)
#
#
# def move(mouse):
#     global vy
#     print(vy)
#     while True:
#         global VX
#         if 0 < ball.x < window.width:
#             if ball.y < 0 or ball.y > window.height:
#                 vy = -(vy * REDUCE)
#                 ball.move(VX, vy)
#             else:
#                 ball.move(VX, vy)
#             vy += GRAVITY
#             pause(DELAY)
#         else:
#             window.add(ball, START_X, START_Y)
#             break

    # if ball.height < 0 or ball.height > window.height:
    #     vy = -vy
    # else:
    #     ball.move(VX, 0)
    #     print("a")
    #     pause(DELAY)


if __name__ == "__main__":
    main()
