"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE

total extensions: --> Extension1: draw the "lives remaining label", Extension2 : draw the "scoreboard label",
 Extension3: if lives remaining == 0 , show "GAME OVER", Extension4: if all bricks were removed, show "YOU WIN!!!"
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


class BreakoutGraphics2:

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

        # set lives 計算遊戲的生命值
        self.lives = 0

        # Extension1: draw the "lives remaining label" 在視窗的右下角顯示還有幾命
        self.lives_label = GLabel("Lives : " + str(3-self.lives))
        self.lives_label.font = "-15"
        self.lives_label.color = "red"
        self.window.add(self.lives_label, window_width-130, self.window.height-10)

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)  # 點擊滑鼠後，開始遊戲
        onmousemoved(self.paddle_move)  # 當滑鼠移動時，paddle跟著移動

        self.count = 0  # 計算總共移除了多少個磚塊
        self.show_lose = 0  # 顯示遊戲輸了
        self.show_win = 0  # 顯示遊戲贏了

        # Extension2 : draw the "scoreboard label" 在視窗左下角顯示出現在的分數板
        self.score_label = GLabel("Score: " + str(self.count))
        self.score_label.font = "-15"
        self.score_label.color = "blue"
        self.window.add(self.score_label, 50, self.window.height-10)

        self.finish = brick_rows*brick_cols  # 設定磚塊的總數目
        self.ball_collision()  # 球是否碰撞，並判斷是撞到paddle還是bricks
        self.lives_reduce()  # 偵測球是否超過底線，若是，self.lives會+1，作為user端lives是否等於NUM_LIVES遊戲結束的依據

    def lives_reduce(self):  # 球若超過底線，球會回到正中央(一開始)靜止，且self.lives會+1
        if self.ball.y > self.window.height:
            self.ball.x = (self.window.width-self.ball.width)/2
            self.ball.y = (self.window.height-self.ball.height)/2
            self.__dx = 0
            self.__dy = 0
            self.lives += 1
            self.lives_label.text = "Lives : " + str(3-self.lives)
            # Extension3: if lives remaining == 0 (when the self.lives == NUM_LIVES = 3), show "GAME OVER"
            # 當已經花了三次生命值，磚塊還沒被完全消除的話，就在畫面印出GAME OVER的字樣
            if self.lives == 3:
                self.show_lose = GLabel("GAME   OVER")
                self.show_lose.font = "-50"
                self.show_lose.color = "salmon"
                self.window.add(self.show_lose, (self.window.width-self.show_lose.width)/2, 450)

    def start_game(self, event2):  # 點按後，遊戲開始
        initial_x_pos = (self.window.width-self.ball.width)/2
        initial_y_pos = (self.window.height-self.ball.height)/2
        if self.ball.x == initial_x_pos and self.ball.y == initial_y_pos: # 若球在初始位置，會重新開始遊戲
            self.__dy = INITIAL_Y_SPEED  # 決定此次遊戲開始的初始速度
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
        else:
            pass

    def set_dx(self):  # 若左右碰到視窗邊界，反彈回來
        self.__dx *= -1

    def set_dy(self):  # 若上面碰到視窗邊界，反彈回來
        self.__dy *= -1

    def get_dx(self):   # Getter
        return self.__dx

    def get_dy(self):   # Getter
        return self.__dy

    def paddle_move(self, event):  # paddle跟著滑鼠移動，且若滑鼠移超過視窗，paddle仍完整停留在視窗中
        if event.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif event.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def ball_collision(self):  # 判斷球是否碰撞，並判斷碰撞到的是paddle還是bricks
        while self.collide_object():  # 若收到回傳值是True，代表有碰撞，且不會是碰撞到計分板與生命條，而是bricks或paddle擇一
            obj = self.collide_object()
            if obj is self.paddle:  # 撞到paddle
                # 反彈
                if self.__dy > 0:  # 若球的速度>0，即球的方向向下
                    self.__dy *= -1  # 球要反彈，即self.__dy要變號
                    self.ball.move(self.__dx, self.__dy)
                else:  # 若球的速度<=0，代表球的方向向上，此時dy就不變號了，可以排除球看起來黏在paddle上的bug
                    self.__dy *= 1
                    self.ball.move(self.__dx, self.__dy)
            else:  # 撞到bricks
                # 移除、反彈
                self.window.remove(obj)
                self.count += 1
                self.__dy *= -1
                self.ball.move(self.__dx, self.__dy)
                self.score_label.text = "Score: " + str(self.count)
                # Extension4: if all bricks were removed, show "YOU WIN!!!" 當所有磚塊被消除，在視窗中顯示你贏了
                if self.count == self.finish:  # 當計算消除的磚塊數=此次遊戲磚塊的總數目
                    self.show_win = GLabel("YOU   WIN  !!!")
                    self.show_win.color = "magenta"
                    self.show_win.font = "-60"
                    self.window.add(self.show_win, (self.window.width - self.show_win.width) / 2, 300)

        # while self.collide_object():  # 若回傳值為True，則代表有碰撞，要判斷他是撞到paddle還是bricks
            # if self.ball.y == 578.5:  # self.paddle.y  # 碰到paddle
            #     self.__dy = - self.__dy
            #     self.ball.move(self.__dx, self.__dy)
            # elif 0 <= self.ball.x <= self.window.width-self.ball.width:  # 碰到bricks
            #     if BRICK_OFFSET <= self.ball.y <= BRICK_OFFSET+BRICK_COLS*(BRICK_HEIGHT+BRICK_SPACING):
            #         bricks = self.window.get_object_at(self.ball.x, self.ball.y)
            #         bricks2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            #         bricks3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
            #         bricks4 = self.window.get_object_at(self.ball.x , self.ball.y + self.ball.height)
            #         if bricks:  # 要移除碰到的bricks，並計算總共移除了多少個磚塊，已確認遊戲結束了沒，並反彈
            #             self.window.remove(bricks)
            #             self.count += 1
            #             print(self.count)
            #         elif bricks2:
            #             self.window.remove(bricks2)
            #             self.count += 1
            #             print(self.count)
            #         elif bricks3:
            #             self.window.remove(bricks3)
            #             self.count += 1
            #             print(self.count)
            #         elif bricks4:
            #             self.window.remove(bricks4)
            #             self.count += 1
            #             print(self.count)
            #         self.__dy = - self.__dy        # 移除後球反彈運動
            #         self.ball.move(self.__dx, self.__dy)
            # elif 578.5 < self.ball.y <= 600:  # 若球在超過paddle後便不再反彈
            #     break
        # print("5")
        # if self.ball.y > PADDLE_OFFSET:
        #     self.ball.x = (self.window.width-self.ball.width)/2
        #     self.ball.y = (self.window.height-self.ball.height)/2

    def if_bounce_against_wall(self):  # 若左右碰到邊界和上面碰到視窗的話，會反彈回來
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.set_dx()
        if self.ball.y <= 0:
            self.set_dy()

    def collide_object(self):
        # 偵測球的四個邊角有無偵測到物體，並判斷此時球的高度是否<視窗高度-25。若有偵測到物體且高度符合限定，則會回傳True
        detect1 = self.window.get_object_at(self.ball.x, self.ball.y)
        if detect1 is not None and self.ball.y < self.window.height-25:  # 有偵測到物體，且不是計分板或生命條，會回傳True
            return detect1
        detect2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if detect2 is not None and self.ball.y < self.window.height-25:
            return detect2
        detect3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if detect3 is not None and self.ball.y + self.ball.height < self.window.height-25:
            return detect3
        detect4 = self.window.get_object_at(self.ball. x + self.ball.width, self.ball.y + self.ball.height)
        if detect4 is not None and self.ball.y + self.ball.height < self.window.height-25:
            return detect4












