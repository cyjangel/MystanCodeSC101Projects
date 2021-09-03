"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20  # 線與視窗的保留距離
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2      # 文字左邊與直線之間的距離
LINE_WIDTH = 2
MAX_RANK = 1000  # 排名最後一名的編號


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.
    讓 x 座標隨著不同年移動

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_site = GRAPH_MARGIN_SIZE+(width-2*GRAPH_MARGIN_SIZE)/len(YEARS)*year_index
    return x_site


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # 做兩條固定的橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # 隨著資料中的年份決定直線的數目，並在底部加上標示年份的文字
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    rank = 0
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS)):                         # len(YEARS)= 12, j=0,1,2,3....,11
            if j < len(YEARS)-1:                            # 當j的年份還不是最後一筆(即不是最右邊的一筆)
                year = YEARS[j]                             # 當年的資料
                the_next_year = YEARS[j+1]                  # 隔年的資料
                if str(year) in name_data[name]:            # 若此名字有在當年的資料中，存入當年的排名
                    rank = (name_data[name][str(year)])
                else:                                       # 若此名字不在當年的資料中，代表排名超過1000，我訂為1050名
                    rank = 1050
                if str(the_next_year) in name_data[name]:   # 若隔年的排名有在隔年的資料中，存入隔年的排名
                    the_next_rank = (name_data[name][str(the_next_year)])
                else:
                    the_next_rank = 1050                    # 若不在當年的資料中，代表排名> 1000，我訂為1050名
                if int(rank) > 1000:                        # 畫線有四種型態
                    if int(the_next_rank) > 1000:
                        # 第一型：當年與隔一年都超過1000名，為一條水平線，並標示當年名次標示為"*"
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, j+1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[i % 4])
                        canvas.create_text(TEXT_DX+get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           text=name+" "+"*", anchor=tkinter.SW, fill=COLORS[i % 4])
                    elif int(the_next_rank) < 1000:
                        # 第二型：當年超過1000名，隔一年<1000，線往斜上走，並標示當年的名次
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, j+1),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(the_next_rank)
                                           ,width=LINE_WIDTH, fill=COLORS[i % 4])
                        canvas.create_text(TEXT_DX+get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=name+" "+"*", anchor=tkinter.SW, fill=COLORS[i % 4])
                elif int(rank) < 1000:
                    if int(the_next_rank) > 1000:
                        # 第三型：當年<1000名，隔一年>1000，線往斜下走，並標示當年的名次
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(rank),
                                           get_x_coordinate(CANVAS_WIDTH, j+1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[i % 4])
                        canvas.create_text(TEXT_DX+get_x_coordinate(CANVAS_WIDTH, j),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(rank),
                                           text=name+" "+str(rank), anchor=tkinter.SW, fill=COLORS[i % 4])
                    if int(rank) < 1000 and int(the_next_rank) < 1000:
                        # 第四型：當年<1000名，隔一年也<1000，線依照兩年的名次相連，並標示當年的名次
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(rank),
                                           get_x_coordinate(CANVAS_WIDTH, j+1),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(the_next_rank)
                                           , width=LINE_WIDTH, fill=COLORS[i % 4])
                        canvas.create_text(TEXT_DX+get_x_coordinate(CANVAS_WIDTH, j),
                                           GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000*int(rank),
                                           text=name+" "+str(rank), anchor=tkinter.SW, fill=COLORS[i % 4])
            elif j == len(YEARS)-1:     # 若j的年份是最後一筆(即是最右邊的一筆)
                year = YEARS[j]
                if str(year) in name_data[name]:   # 存入最後一年份的排名
                    rank = (name_data[name][str(year)])
                if int(rank) < 1000:    # 若最後一筆的排名小於1000，便顯示實際的名次
                    canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2 * GRAPH_MARGIN_SIZE) / 1000 * int(rank),
                                       text=name+" "+str(rank), anchor=tkinter.SW, fill=COLORS[i % 4])
                else:                   # 若最後一筆的排名大於1000，顯示排名在最底下，為"*"
                    canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, j), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=name + "*", anchor=tkinter.SW, fill=COLORS[i % 4])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
