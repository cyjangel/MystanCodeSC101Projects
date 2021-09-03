"""
File: my_drawing_forever_young
Name: Angel Chen
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


def main():
    """
    TODO:
    """
    window = GWindow(width=1000, height=600)

    # 天空
    sky = GRect(1000, 270)
    sky.filled = True
    sky.color = "steelblue"
    sky.fill_color = "steelblue"
    window.add(sky)

    sky1 = GRect(1000, 235)
    sky1.filled = True
    sky1.color = "lightblue"
    sky1.fill_color = "lightblue"
    window.add(sky1, 0, 265)

    sky2 = GRect(1000, 223)
    sky2.filled = True
    sky2.color = "lightsage"
    sky2.fill_color = "lightsage"
    window.add(sky2, 0, 472)

    # 地球
    earth = GArc(500, 900, 0, 180, 236, 435)
    earth.filled = True
    earth.fill_color = "cornflowerblue"
    window.add(earth)

    # 地球上綠色土地
    ground = GOval(30, 30)
    ground.color = "forestgreen"
    ground.filled = True
    ground.fill_color = "forestgreen"
    window.add(ground, 400, 452)

    ground1 = GOval(30, 30)
    ground1.color = "forestgreen"
    ground1.filled = True
    ground1.fill_color = "forestgreen"
    window.add(ground1, 388, 450)

    ground2 = GOval(50, 50)
    ground2.color = "forestgreen"
    ground2.filled = True
    ground2.fill_color = "forestgreen"
    window.add(ground2, 390, 470)

    ground3 = GOval(50, 50)
    ground3.color = "forestgreen"
    ground3.filled = True
    ground3.fill_color = "forestgreen"
    window.add(ground3, 361.5, 456.5)

    ground4 = GOval(50, 50)
    ground4.color = "forestgreen"
    ground4.filled = True
    ground4.fill_color = "forestgreen"
    window.add(ground4, 345, 465)

    ground5 = GOval(50, 50)
    ground5.color = "forestgreen"
    ground5.filled = True
    ground5.fill_color = "forestgreen"
    window.add(ground5, 328, 475.5)

    ground6 = GOval(50, 50)
    ground6.color = "forestgreen"
    ground6.filled = True
    ground6.fill_color = "forestgreen"
    window.add(ground6, 358, 490)

    ground7 = GOval(50, 50)
    ground7.color = "forestgreen"
    ground7.filled = True
    ground7.fill_color = "forestgreen"
    window.add(ground7, 385, 490)

    ground8 = GOval(30, 30)
    ground8.color = "forestgreen"
    ground8.filled = True
    ground8.fill_color = "forestgreen"
    window.add(ground8, 405, 520)

    ground9 = GOval(25, 25)
    ground9.color = "forestgreen"
    ground9.filled = True
    ground9.fill_color = "forestgreen"
    window.add(ground9, 415, 540)

    ground10 = GOval(23, 23)
    ground10.color = "forestgreen"
    ground10.filled = True
    ground10.fill_color = "forestgreen"
    window.add(ground10, 420, 555)

    ground11 = GOval(40, 40)
    ground11.color = "forestgreen"
    ground11.filled = True
    ground11.fill_color = "forestgreen"
    window.add(ground11, 410, 575)

    ground12 = GOval(35, 35)
    ground12.color = "forestgreen"
    ground12.filled = True
    ground12.fill_color = "forestgreen"
    window.add(ground12, 426, 573)

    ground13 = GOval(35, 35)
    ground13.color = "forestgreen"
    ground13.filled = True
    ground13.fill_color = "forestgreen"
    window.add(ground13, 400, 575)

    ground14 = GOval(40, 40)
    ground14.color = "forestgreen"
    ground14.filled = True
    ground14.fill_color = "forestgreen"
    window.add(ground14, 380, 571)

    ground15 = GOval(35, 35)
    ground15.color = "forestgreen"
    ground15.filled = True
    ground15.fill_color = "forestgreen"
    window.add(ground15, 574, 459)

    ground16 = GOval(35, 35)
    ground16.color = "forestgreen"
    ground16.filled = True
    ground16.fill_color = "forestgreen"
    window.add(ground16, 590, 466)

    ground17 = GOval(35, 35)
    ground17.color = "forestgreen"
    ground17.filled = True
    ground17.fill_color = "forestgreen"
    window.add(ground17, 689, 579)

    ground18 = GOval(45, 45)
    ground18.color = "forestgreen"
    ground18.filled = True
    ground18.fill_color = "forestgreen"
    window.add(ground18, 657, 565)

    # 太陽
    sun = GOval(300, 295)
    sun.color = "gold"
    sun.filled = True
    sun.fill_color = "gold"
    window.add(sun, -130, -130)

    # 太陽的墨鏡
    eye1 = GPolygon()
    eye1.add_vertex((0, 60))
    eye1.add_vertex((12, 48))
    eye1.add_vertex((25, 60))
    eye1.add_vertex((48, 38))
    eye1.add_vertex((36, 25))
    eye1.add_vertex((58, 3))
    eye1.add_vertex((84, 25))
    eye1.add_vertex((59, 49))
    eye1.add_vertex((50, 40))
    eye1.add_vertex((27, 62))
    eye1.add_vertex((37, 72))
    eye1.add_vertex((11, 97))
    eye1.add_vertex((-12, 72))
    # eye1.add_vertex((5, 57.5))
    # eye1.add_vertex((0, 50))
    eye1.filled = True
    eye1.fill_color = "black"
    window.add(eye1)

    # 太陽的腮紅
    cheek1 = GOval(12, 12)
    cheek1.filled = True
    cheek1.color = "coral"
    cheek1.fill_color = "coral"
    window.add(cheek1, 105, 15)

    cheek2 = GOval(12, 12)
    cheek2.filled = True
    cheek2.color = "coral"
    cheek2.fill_color = "coral"
    window.add(cheek2, 113, 6)

    cheek3 = GOval(12, 12)
    cheek3.filled = True
    cheek3.color = "coral"
    cheek3.fill_color = "coral"
    window.add(cheek3, 6, 110)

    cheek4 = GOval(12, 12)
    cheek4.filled = True
    cheek4.color = "coral"
    cheek4.fill_color = "coral"
    window.add(cheek4, -2, 120)

    # 太陽的領帶
    tie = GPolygon()
    tie.add_vertex((55, 85))
    tie.add_vertex((70, 100))
    tie.add_vertex((75, 60))
    tie.add_vertex((90, 75))
    window.add(tie)
    tie.filled = True
    tie.fill_color = "black"

    tie2 = GPolygon()
    tie2.add_vertex((72.5, 80))
    tie2.add_vertex((89, 79))
    # tie2.add_vertex((110, 100))
    tie2.add_vertex((91.5, 97))
    # tie2.add_vertex((115, 115))
    # tie2.add_vertex((94.5, 117.5))
    tie2.add_vertex((73.5, 96.5))
    tie2.add_vertex((72.5, 80))
    window.add(tie2)
    tie2.color = "magenta"
    tie2.filled = True
    tie2.fill_color = "white"

    # 海綿寶寶的手

    # l_hand = GPolygon()
    # l_hand.filled = True
    # l_hand.fill_color = "white"
    # l_hand.add_vertex((365, 205))
    # l_hand.add_vertex((361, 205))
    # l_hand.add_vertex((350, 240))
    # l_hand.add_vertex((370, 245))
    # window.add(l_hand)

    l_hand = GArc(120, 140, 55, 135, 350, 236)
    l_hand.filled = False
    window.add(l_hand)

    l_hand1 = GPolygon()
    l_hand1.add_vertex((350, 285))
    l_hand1.add_vertex((370, 287))
    l_hand1.filled = False
    window.add(l_hand1)

    l_hand2 = GPolygon()
    l_hand2.add_vertex((355, 286))
    l_hand2.add_vertex((365, 287))
    l_hand2.add_vertex((343, 320))
    l_hand2.add_vertex((420, 350))
    l_hand2.add_vertex((415, 356))
    l_hand2.add_vertex((330, 325))
    l_hand2.filled = True
    l_hand2.fill_color = "yellow"
    window.add(l_hand2)

    r_hand = GArc(140, 140, -5, 110, 514, 237)
    r_hand.filled = False
    window.add(r_hand)

    r_hand1 = GPolygon()
    r_hand1.add_vertex((602, 279))
    r_hand1.add_vertex((580, 282))
    r_hand1.filled = False
    window.add(r_hand1)

    r_hand2 = GPolygon()
    r_hand2.add_vertex((585, 280))
    r_hand2.add_vertex((596, 279))
    r_hand2.add_vertex((623, 320))
    r_hand2.add_vertex((520, 350))
    r_hand2.add_vertex((515, 345))
    r_hand2.add_vertex((610, 315))
    r_hand2.filled = True
    r_hand2.fill_color = "yellow"
    window.add(r_hand2)

    # 海綿寶寶的頭
    sponge = GPolygon()
    sponge.add_vertex((360, 95))
    sponge.add_vertex((590, 95))
    sponge.add_vertex((580, 315))
    sponge.add_vertex((370, 315))
    # sponge.add_vertex((90, 75))
    sponge.color = "olive"
    sponge.filled = True
    sponge.fill_color = "yellow"
    window.add(sponge)

    # 海綿寶寶衣服
    cloth = GRect(210, 25)
    cloth.filled = True
    cloth.fill_color = "white"
    window.add(cloth, 370, 315)

    cloth1 = GOval(4, 5)
    cloth1.color = "white"
    cloth1.filled = True
    cloth1.fill_color = "white"
    window.add(cloth1, 362, 249.5)

    cloth2 = GOval(7, 8)
    cloth2.color = "white"
    cloth2.filled = True
    cloth2.fill_color = "white"
    window.add(cloth2, 358.5, 252.5)

    cloth3 = GOval(12, 12)
    cloth3.color = "white"
    cloth3.filled = True
    cloth3.fill_color = "white"
    window.add(cloth3, 354, 258)

    cloth4 = GOval(15, 15)
    cloth4.color = "white"
    cloth4.filled = True
    cloth4.fill_color = "white"
    window.add(cloth4, 351.5, 265)

    cloth5 = GOval(15, 15)
    cloth5.color = "white"
    cloth5.filled = True
    cloth5.fill_color = "white"
    window.add(cloth5, 351.5, 270)

    cloth6 = GRect(10, 20)
    cloth6.color = "white"
    cloth6.filled = True
    cloth6.fill_color = "white"
    window.add(cloth6, 356, 265)

    cloth1 = GOval(3, 6)
    cloth1.color = "white"
    cloth1.filled = True
    cloth1.fill_color = "white"
    window.add(cloth1, 584.1, 246.6)

    cloth2 = GOval(7, 8)
    cloth2.color = "white"
    cloth2.filled = True
    cloth2.fill_color = "white"
    window.add(cloth2, 584.5, 250.5)

    cloth3 = GOval(12, 12)
    cloth3.color = "white"
    cloth3.filled = True
    cloth3.fill_color = "white"
    window.add(cloth3, 584, 256)

    cloth4 = GOval(15, 15)
    cloth4.color = "white"
    cloth4.filled = True
    cloth4.fill_color = "white"
    window.add(cloth4, 585, 263)

    cloth5 = GOval(5, 5)
    cloth5.color = "white"
    cloth5.filled = True
    cloth5.fill_color = "white"
    window.add(cloth5, 586, 264)

    cloth6 = GRect(10, 22)
    cloth6.color = "white"
    cloth6.filled = True
    cloth6.fill_color = "white"
    window.add(cloth6, 584, 256)

    cloth6 = GOval(5, 5)
    cloth6.color = "white"
    cloth6.filled = True
    cloth6.fill_color = "white"
    window.add(cloth6, 596, 273.5)

    # 海綿寶寶褲子
    pants = GRect(210, 30)
    pants.filled = True
    pants.fill_color = "peru"
    window.add(pants, 370, 340)

    pants1 = GRect(38, 13)
    pants1.filled = True
    pants1.fill_color = "saddle brown"
    window.add(pants1, 407, 370)

    pants2 = GRect(38, 13)
    pants2.filled = True
    pants2.fill_color = "saddle brown"
    window.add(pants2, 505, 370)

    # 海綿寶寶的領帶
    sl_tie = GPolygon()
    sl_tie.add_vertex((433, 315))
    sl_tie.add_vertex((455, 330))
    sl_tie.add_vertex((468, 315))
    window.add(sl_tie)

    sl_tie1 = GPolygon()
    sl_tie1.add_vertex((468, 315))
    sl_tie1.add_vertex((472, 330))
    sl_tie1.add_vertex((479, 330))
    sl_tie1.add_vertex((483, 315))
    sl_tie1.filled = True
    sl_tie1.fill_color = "tomato"
    window.add(sl_tie1)

    sl_tie2 = GPolygon()
    sl_tie2.add_vertex((472, 330))
    sl_tie2.add_vertex((479, 330))
    sl_tie2.add_vertex((485, 355))
    sl_tie2.add_vertex((475.5, 364))
    sl_tie2.add_vertex((466, 355))
    sl_tie2.filled = True
    sl_tie2.fill_color = "tomato"
    window.add(sl_tie2)

    sl_tie3 = GPolygon()
    sl_tie3.add_vertex((483, 315))
    sl_tie3.add_vertex((496, 330))
    sl_tie3.add_vertex((518, 315))
    window.add(sl_tie3)

    # 海綿寶寶的腳
    foot1 = GRect(9, 13)
    foot1.filled = True
    foot1.fill_color = "yellow"
    window.add(foot1, 422, 383)

    foot2 = GRect(9, 13)
    foot2.filled = True
    foot2.fill_color = "yellow"
    window.add(foot2, 520, 383)

    # 海綿寶寶的鞋子
    l_shoe = GOval(25, 25)
    l_shoe.filled = True
    l_shoe.fill_color = "black"
    window.add(l_shoe, 416, 425)

    l_shoe1 = GOval(20, 20)
    l_shoe1.filled = True
    l_shoe1.fill_color = "black"
    window.add(l_shoe1, 409, 435)

    l_shoe2 = GOval(22, 22)
    l_shoe2.filled = True
    l_shoe2.fill_color = "black"
    window.add(l_shoe2, 404, 437)

    l_shoe3 = GOval(32, 32)
    l_shoe3.filled = True
    l_shoe3.fill_color = "black"
    window.add(l_shoe3, 388, 435)

    l_shoe4 = GRect(14, 18)
    l_shoe4.filled = True
    l_shoe4.fill_color = "black"
    window.add(l_shoe4, 425, 438)

    r_shoe = GOval(25, 25)
    r_shoe.filled = True
    r_shoe.fill_color = "black"
    window.add(r_shoe, 510, 425)

    r_shoe1 = GOval(20, 20)
    r_shoe1.filled = True
    r_shoe1.fill_color = "black"
    window.add(r_shoe1, 523, 432)

    r_shoe2 = GOval(22, 22)
    r_shoe2.filled = True
    r_shoe2.fill_color = "black"
    window.add(r_shoe2, 526, 432)

    r_shoe3 = GOval(32, 32)
    r_shoe3.filled = True
    r_shoe3.fill_color = "black"
    window.add(r_shoe3, 533, 428)

    l_shoe1 = GRect(14, 18)
    l_shoe1.filled = True
    l_shoe1.fill_color = "black"
    window.add(l_shoe1, 512, 437)

    # 海綿寶寶的襪子
    left_sock1 = GRect(9, 2)
    left_sock1.color = "blue"
    left_sock1.filled = True
    left_sock1.fill_color = "blue"
    window.add(left_sock1, 422, 396)

    left_sock2 = GRect(9, 6)
    left_sock2.filled = True
    left_sock2.fill_color = "white"
    window.add(left_sock2, 422, 398)

    left_sock3 = GRect(9, 2)
    left_sock3.color = "blue"
    left_sock3.filled = True
    left_sock3.fill_color = "blue"
    window.add(left_sock3, 422, 404)

    left_sock4 = GRect(9, 5)
    left_sock4.filled = True
    left_sock4.fill_color = "white"
    window.add(left_sock4, 422, 406)

    left_sock5 = GRect(9, 2)
    left_sock5.color = "red"
    left_sock5.filled = True
    left_sock5.fill_color = "red"
    window.add(left_sock5, 422, 411)

    left_sock6 = GRect(9, 18)
    left_sock6.filled = True
    left_sock6.fill_color = "white"
    window.add(left_sock6, 422, 413)

    right_sock1 = GRect(9, 2)
    right_sock1.color = "blue"
    right_sock1.filled = True
    right_sock1.fill_color = "blue"
    window.add( right_sock1, 520, 396)

    right_sock2 = GRect(9, 6)
    right_sock2.filled = True
    right_sock2.fill_color = "white"
    window.add(right_sock2, 520, 398)

    right_sock3 = GRect(9, 2)
    right_sock3.color = "blue"
    right_sock3.filled = True
    right_sock3.fill_color = "blue"
    window.add(right_sock3, 520, 404)

    right_sock4 = GRect(9, 5)
    right_sock4.filled = True
    right_sock4.fill_color = "white"
    window.add(right_sock4, 520, 406)

    right_sock5 = GRect(9, 2)
    right_sock5.color = "red"
    right_sock5.filled = True
    right_sock5.fill_color = "red"
    window.add( right_sock5, 520, 411)

    right_sock6 = GRect(9, 18)
    right_sock6.filled = True
    right_sock6.fill_color = "white"
    window.add(right_sock6, 520, 413)

    # 海綿寶寶的睫毛
    l_eyelashes = GPolygon()
    l_eyelashes.add_vertex((426, 113))
    l_eyelashes.add_vertex((433, 113))
    l_eyelashes.add_vertex((434, 129))
    l_eyelashes.add_vertex((428, 129))
    l_eyelashes.filled = True
    l_eyelashes.fill_color = "black"
    window.add(l_eyelashes)

    l_eyelashes1 = GPolygon()
    l_eyelashes1.add_vertex((452, 118))
    l_eyelashes1.add_vertex((459, 119))
    l_eyelashes1.add_vertex((456, 130))
    l_eyelashes1.add_vertex((450, 128))
    l_eyelashes1.filled = True
    l_eyelashes1.fill_color = "black"
    window.add(l_eyelashes1)

    l_eyelashes2 = GPolygon()
    l_eyelashes2.add_vertex((402, 123))
    l_eyelashes2.add_vertex((408, 120))
    l_eyelashes2.add_vertex((416, 130))
    l_eyelashes2.add_vertex((414, 138))
    l_eyelashes2.filled = True
    l_eyelashes2.fill_color = "black"
    window.add(l_eyelashes2)

    r_eyelashes = GPolygon()
    r_eyelashes.add_vertex((511, 112.5))
    r_eyelashes.add_vertex((517, 112.5))
    r_eyelashes.add_vertex((516, 129))
    r_eyelashes.add_vertex((510, 129))
    r_eyelashes.filled = True
    r_eyelashes.fill_color = "black"
    window.add(r_eyelashes)

    r_eyelashes1 = GPolygon()
    r_eyelashes1.add_vertex((486, 119))
    r_eyelashes1.add_vertex((493, 118))
    r_eyelashes1.add_vertex((502, 135))
    r_eyelashes1.add_vertex((495, 135))
    r_eyelashes1.filled = True
    r_eyelashes1.fill_color = "black"
    window.add(r_eyelashes1)

    r_eyelashes2 = GPolygon()
    r_eyelashes2.add_vertex((535, 117))
    r_eyelashes2.add_vertex((541, 119))
    r_eyelashes2.add_vertex((537, 130))
    r_eyelashes2.add_vertex((530, 130))
    r_eyelashes2.filled = True
    r_eyelashes2.fill_color = "black"
    window.add(r_eyelashes2)

    # 海綿寶寶的眼睛
    s_eye = GOval(80, 80)
    s_eye.filled = True
    s_eye.fill_color = "white"
    window.add(s_eye, 395, 125)

    sr_eye = GOval(80, 80)
    sr_eye.filled = True
    sr_eye.fill_color = "white"
    window.add(sr_eye, 475, 125)

    # 海綿寶寶瞳孔
    s_eye1 = GOval(35, 35)
    s_eye1.filled = True
    s_eye1.fill_color = "deepskyblue"
    window.add(s_eye1, 420, 150)

    s_eye2 = GOval(21, 21)
    s_eye2.filled = True
    s_eye2.fill_color = "black"
    window.add(s_eye2, 427, 157)

    s_eye3 = GOval(35, 35)
    s_eye3.filled = True
    s_eye3.fill_color = "deepskyblue"
    window.add(s_eye3, 495, 150)

    s_eye4 = GOval(21, 21)
    s_eye4.filled = True
    s_eye4.fill_color = "black"
    window.add(s_eye4, 502, 157)

    # 海綿寶寶的臉頰
    s_cheek = GArc(40, 55, -15, 220, 385, 185)
    s_cheek.filled = False
    s_cheek.color = "red"
    window.add(s_cheek)

    s_cheek1 = GOval(15, 15)
    s_cheek1.filled = True
    s_cheek1.color = "yellow"
    s_cheek1.fill_color = "yellow"
    window.add(s_cheek1, 398, 186)

    s_cheek2 = GOval(15, 15)
    s_cheek2.filled = True
    s_cheek2.color = "yellow"
    s_cheek2.fill_color = "yellow"
    window.add(s_cheek2, 403, 187.5)

    s_cheek3 = GOval(15, 15)
    s_cheek3.filled = True
    s_cheek3.color = "yellow"
    s_cheek3.fill_color = "yellow"
    window.add(s_cheek3, 407.9, 191.5)

    # 右臉頰

    s_cheek = GArc(41, 72, -10, 200, 525, 185)
    s_cheek.filled = False
    s_cheek.color = "red"
    window.add(s_cheek)

    sr_cheek1 = GOval(15, 15)
    sr_cheek1.filled = True
    sr_cheek1.color = "yellow"
    sr_cheek1.fill_color = "yellow"
    window.add(sr_cheek1, 526.5, 192.5)

    sr_cheek2 = GOval(15, 15)
    sr_cheek2.filled = True
    sr_cheek2.color = "yellow"
    sr_cheek2.fill_color = "yellow"
    window.add(sr_cheek2, 530, 189)

    s_cheek3 = GOval(15, 15)
    s_cheek3.filled = True
    s_cheek3.color = "yellow"
    s_cheek3.fill_color = "yellow"
    window.add(s_cheek3, 537, 185.5)

    s_cheek4 = GOval(5, 5)
    s_cheek4.filled = True
    s_cheek4.color = "yellow"
    s_cheek4.fill_color = "coral"
    window.add(s_cheek4, 400, 198)

    s_cheek5 = GOval(5, 5)
    s_cheek5.filled = True
    s_cheek5.color = "yellow"
    s_cheek5.fill_color = "coral"
    window.add(s_cheek5, 392, 194.5)

    s_cheek6 = GOval(5, 5)
    s_cheek6.filled = True
    s_cheek6.color = "yellow"
    s_cheek6.fill_color = "coral"
    window.add(s_cheek6, 413, 193)

    s_cheek7 = GOval(5, 5)
    s_cheek7.filled = True
    s_cheek7.color = "yellow"
    s_cheek7.fill_color = "coral"
    window.add(s_cheek7, 553.5, 194.5)

    s_cheek8 = GOval(5, 5)
    s_cheek8.filled = True
    s_cheek8.color = "yellow"
    s_cheek8.fill_color = "coral"
    window.add(s_cheek8, 535, 193)

    s_cheek9 = GOval(5, 5)
    s_cheek9.filled = True
    s_cheek9.color = "yellow"
    s_cheek9.fill_color = "coral"
    window.add(s_cheek9, 543, 198)

    # 海綿寶寶微笑
    smile = GArc(140, 153, 180, 180, 406, 170)
    smile.filled = False
    smile.color = "black"
    window.add(smile)

    # mouth1 = GArc(142, 320, 180, 180, 405, 130)
    # mouth1.filled = False
    # window.add(mouth1)
    mouth1 = GArc(35, 30, 180, 180, 443, 265)
    mouth1.filled = False
    mouth1.color = "red"
    window.add(mouth1)

    mouth2 = GArc(35, 30, 180, 180, 479, 265)
    mouth2.filled = False
    mouth2.color = "red"
    window.add(mouth2)

    # 海綿凹洞
    cave = GOval(21, 30)
    cave.filled = True
    cave.color = "yellow"
    cave.fill_color = "olivedrab"
    window.add(cave, 380, 105)

    cave1 = GOval(10, 15)
    cave1.filled = True
    cave1.color = "yellow"
    cave1.fill_color = "olivedrab"
    window.add(cave1, 370, 140)

    cave2 = GOval(15, 20)
    cave2.filled = True
    cave2.color = "yellow"
    cave2.fill_color = "olivedrab"
    window.add(cave2, 376, 250)

    cave3 = GOval(25, 30)
    cave3.filled = True
    cave3.color = "yellow"
    cave3.fill_color = "olivedrab"
    window.add(cave3, 378, 275)

    cave4 = GOval(15, 20)
    cave4.filled = True
    cave4.color = "yellow"
    cave4.fill_color = "olivedrab"
    window.add(cave4, 560, 110)

    cave5 = GOval(30, 35)
    cave5.filled = True
    cave5.color = "yellow"
    cave5.fill_color = "olivedrab"
    window.add(cave5, 545, 260)

    cave6 = GOval(12, 17)
    cave6.filled = True
    cave6.color = "yellow"
    cave6.fill_color = "olivedrab"
    window.add(cave6, 537, 289)

    # 海綿寶寶的牙齒
    tooth1 = GPolygon()
    tooth1.add_vertex((457, 245.5))
    tooth1.add_vertex((455, 263))
    tooth1.add_vertex((474, 263))
    tooth1.add_vertex((474, 247))
    tooth1.filled = False
    window.add(tooth1)

    tooth2 = GPolygon()
    tooth2.add_vertex((480, 247))
    tooth2.add_vertex((480, 263))
    tooth2.add_vertex((498, 263))
    tooth2.add_vertex((498, 246))
    tooth2.filled = False
    window.add(tooth2)

    tooth3 = GOval(12, 12)
    tooth3.color = "white"
    tooth3.filled = True
    tooth3.fill_color = "white"
    window.add(tooth3, 485, 248)

    tooth4 = GOval(12, 12)
    tooth4.color = "white"
    tooth4.filled = True
    tooth4.fill_color = "white"
    window.add(tooth4, 480.5, 247.5)

    tooth5 = GOval(12, 12)
    tooth5.color = "white"
    tooth5.filled = True
    tooth5.fill_color = "white"
    window.add(tooth5, 480.5, 249.5)

    tooth6 = GRect(14, 14)
    tooth6.color = "white"
    tooth6.filled = True
    tooth6.fill_color = "white"
    window.add(tooth6, 482, 248)

    tooth7 = GRect(13, 13)
    tooth7.color = "white"
    tooth7.filled = True
    tooth7.fill_color = "white"
    window.add(tooth7, 458, 248)

    # 海綿寶寶的鼻子
    nose = GArc(25, 180, 0, 178, 464, 168)
    nose.filled = False
    window.add(nose)

    nose1 = GOval(15, 15)
    nose1.color = "yellow"
    nose1.filled = True
    nose1.fill_color = "yellow"
    window.add(nose1, 467, 180)

    nose2 = GOval(15, 15)
    nose2.color = "yellow"
    nose2.filled = True
    nose2.fill_color = "yellow"
    window.add(nose2, 471, 183)

    nose3 = GOval(15, 15)
    nose3.color = "yellow"
    nose3.filled = True
    nose3.fill_color = "yellow"
    window.add(nose3, 469.5, 176)

    nose4 = GOval(10, 12)
    nose4.color = "yellow"
    nose4.filled = True
    nose4.fill_color = "yellow"
    window.add(nose4, 471, 170)

    # 講話
    say1 = GOval(330, 150)
    say1.color = "palevioletred"
    say1.filled = True
    say1.fill_color = "palevioletred"
    window.add(say1, 640, 10)

    say2 = GOval(30, 30)
    say2.color = "salmon"
    say2.filled = True
    say2.fill_color = "salmon"
    window.add(say2, 627, 128)

    say3 = GOval(16, 16)
    say3.color = "lightpink"
    say3.filled = True
    say3.fill_color = "lightpink"
    window.add(say3, 600, 157)

    label = GLabel("你為什麼不問問 ", 700, 80)
    label.font = "Courier-30-italic"
    label.color = "darkviolet"
    window.add(label)

    label1 = GLabel("神奇海螺呢？", 725, 130)
    label1.font = "Courier-30-italic"
    label1.color = "darkviolet"
    window.add(label1)

    pass


if __name__ == '__main__':
    main()
