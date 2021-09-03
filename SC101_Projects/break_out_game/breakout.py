"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!

    while True:
        pause(FRAME_RATE)
        # 當三條命還沒用完時，可以繼續重新開始遊戲，且當移除的bricks數小於總bricks數時，還可以繼續遊戲。
        if graphics.lives < NUM_LIVES and graphics.count < graphics.finish:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())  # 球移動
            graphics.if_bounce_against_wall()   # 若撞到視窗邊界反彈
            graphics.ball_collision()  # 確認球是否碰撞，撞到的東西是bricks還是paddle
            graphics.lives_reduce()  # 若球超過視窗底部，graphics.lives會+1
        else:  # 三條命用完 或 移除的bricks數等於畫面中所有的bricks數(即bricks被全部消除時)
            break  # 離開迴圈


if __name__ == '__main__':
    main()
