"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2, self.window.height-PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS, BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

        # Draw bricks:
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                if j < 2:
                    brick.fill_color = "Red"
                elif 2 <= j < 4:
                    brick.fill_color = "orange"
                elif 4 <= j < 6:
                    brick.fill_color = "yellow"
                elif 6 <= j < 8:
                    brick.fill_color = "green"
                elif 8 <= j < 10:
                    brick.fill_color = "blue"
                space = BRICK_SPACING
                # self.window.add(brick, BRICK_WIDTH * i + space * i, 0)
                self.window.add(brick, BRICK_WIDTH * i + space * i, BRICK_HEIGHT * j + space * j+BRICK_OFFSET)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0

        # set lives ??????????????????
        self.lives = 0

        # ?????????????????????bricks???
        self.count = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)  # ??????????????????????????????
        onmousemoved(self.paddle_move)  # ?????????????????????paddle????????????

        self.finish = brick_rows*brick_cols  # ???bricks??? = bricks???rows*cols
        self.ball_collision()  # ????????????????????????????????????paddle??????bricks
        self.lives_reduce()  # ???????????????????????????????????????self.lives???+1??????user??????lives???NUM_LIVES??????????????????????????????????????????

    def lives_reduce(self):  # ??????????????????????????????????????????(?????????)???????????????self.lives???+1
        if self.ball.y > self.window.height:
            self.ball.x = (self.window.width-self.ball.width)/2
            self.ball.y = (self.window.height-self.ball.height)/2
            self.__dx = 0
            self.__dy = 0
            self.lives += 1

    def start_game(self, event2):  # ????????????????????????
        initial_x_pos = (self.window.width-self.ball.width)/2
        initial_y_pos = (self.window.height-self.ball.height)/2
        if self.ball.x == initial_x_pos and self.ball.y == initial_y_pos:  # ?????????????????????????????????????????????
            self.__dy = INITIAL_Y_SPEED   # ???????????????????????????????????????dy, dx???
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
        else:
            pass

    def set_dx(self):  # ??????????????????????????????????????????
        self.__dx *= -1

    def set_dy(self):  # ??????????????????????????????????????????
        self.__dy *= -1

    def get_dx(self):   # Getter
        return self.__dx

    def get_dy(self):   # Getter
        return self.__dy

    def paddle_move(self, event):  # paddle???????????????????????????????????????????????????paddle???????????????????????????
        if event.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif event.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def ball_collision(self):  # ????????????????????????
        while self.collide_object():  # ?????????????????????????????????=True
            obj = self.collide_object()
            if obj is self.paddle:  # ??????paddle
                # ??????
                if self.__dy > 0:  # ???????????????>0????????????????????????
                    self.__dy *= -1  # ????????????
                    self.ball.move(self.__dx, self.__dy)
                else:   # ???????????????<=0????????????????????????????????????dy????????????????????????????????????????????????paddle??????bug
                    self.__dy *= 1
                    self.ball.move(self.__dx, self.__dy)
            else:  # ??????bricks
                # ???????????????
                self.window.remove(obj)
                self.count += 1
                self.__dy *= -1
                self.ball.move(self.__dx, self.__dy)

    def if_bounce_against_wall(self):  # ?????????????????????????????????????????????????????????????????????
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.set_dx()
        if self.ball.y <= 0:
            self.set_dy()

    def collide_object(self):  # ????????????????????????????????????????????????????????????????????????????????????True
        detect1 = self.window.get_object_at(self.ball.x, self.ball.y)
        if detect1 is not None:
            return detect1
        detect2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if detect2 is not None:
            return detect2
        detect3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if detect3 is not None:
            return detect3
        detect4 = self.window.get_object_at(self.ball. x + self.ball.width, self.ball.y + self.ball.height)
        if detect4 is not None:
            return detect4












