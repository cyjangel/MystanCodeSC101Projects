"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE

total extensions: --> Extension1: draw the "lives remaining label", Extension2 : draw the "scoreboard label",
 Extension3: if lives remaining == 0 , show "GAME OVER", Extension4: if all bricks were removed, show "YOU WIN!!!"
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics2   # 引進extension中的新Class

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics2()
    # Add animation loop here!

    while True:
        pause(FRAME_RATE)
        # 當三條命還沒用完時，可以繼續重新開始遊戲，且當移除的bricks數小於總bricks數時，還可以繼續遊戲。
        if graphics.lives < NUM_LIVES and graphics.count < graphics.finish:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.if_bounce_against_wall()
            graphics.ball_collision()
            graphics.lives_reduce()  # 若球超過視窗底部，graphics.lives會+1
        else:  # 三條命用完 或 移除的bricks數等於畫面中所有的bricks數(即bricks被全部消除時)
            break  # 離開迴圈


if __name__ == '__main__':
    main()
