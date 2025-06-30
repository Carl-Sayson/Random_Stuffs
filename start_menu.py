import tkinter
import random

root = tkinter.Tk()
root.title('Ping Pong')

window_height = 500
window_width = 800

# assets for the game
game_screen = tkinter.Canvas(root, height=window_height,  width=window_width)
board = game_screen.create_rectangle(0, 0, window_width, window_height, fill='green', width=0)
line = game_screen.create_line((window_width+2)/2, 0, (window_width+2)/2, window_height, fill='white', width=5)

# Displays scores of the players
score_1 = 0
score_2 = 0
player_1_scoreboard = game_screen.create_text(120, 25, anchor='ne', font=('Arial', 15),
                                              text='SCORE: ' + str(score_1), fill='white')
player_2_scoreboard = game_screen.create_text(window_width-120, 25, anchor='nw', font=('Arial', 15),
                                              text='SCORE: ' + str(score_2), fill='white')

# Paddles for the game
paddle_width = 25
paddle_height = 75

paddle_left = game_screen.create_rectangle(30, (window_height/2)-paddle_height, paddle_width+30,
                                           (window_height/2)+paddle_height, fill="white", width='0')
paddle_right = game_screen.create_rectangle(window_width-30, (window_height/2)-paddle_height,
                                            window_width-(paddle_width+30), (window_height/2)+paddle_height,
                                            fill="white", width='0')

# The ping-pong ball
ball = game_screen.create_oval((window_width+2)/2 - 20, (window_height+2)/2 - 20,
                               (window_width+2)/2 + 20, (window_height+2)/2 + 20, fill='orange',
                               width=0)
# used for determining the direction of the ball
direction_y = random.choice([-1, 1])
direction_x = random.choice([-1, 1])
# used for how fast the ball will travel
dy = 20
dx = 10

# ball travels
x = (dx*direction_x)
y = (dy*direction_y)

game_screen.pack()


# paddle collisions
def collision_ballmovement():
    # pass
    (p_onex1, p_oney1, p_onex2, p_oney2) = game_screen.coords(paddle_right)
    (p_twox1, p_twoy1, p_twox2, p_twoy2) = game_screen.coords(paddle_left)
    (bx1, by1, bx2, by2) = game_screen.coords(ball)
    coord_x = x
    coord_y = y

    if by1 <= 0 or by2 >= window_height:
        coord_y = -coord_y
    # if by2 >= window_height:
    #     coord_y = -coord_y
    if bx2 >= p_onex1 and by2 >= p_oney1 and by1 <= p_oney2:  # Right paddle
        coord_x = -coord_x
        coord_y = -coord_y
    if bx1 <= p_twox2 and by2 >= p_twoy1 and by1 <= p_twoy2:  # Left paddle
        coord_x = -coord_x
        coord_y = -coord_y

    game_screen.move(ball, coord_x, coord_y)
    game_screen.after(100, collision_ballmovement)


def scoring():
    pass


def restart():
    pass
    # After a game of 12 points or more


def Up_P2(event):
    x1, y1, x2, y2 = game_screen.coords(paddle_left)
    if y1 > 20:
        game_screen.move(paddle_left, 0, -25)


def Down_P2(event):
    x1, y1, x2, y2 = game_screen.coords(paddle_left)
    if y2 <= window_height-20:
        game_screen.move(paddle_left, 0, 25)


def Up_P1(event):
    x1, y1, x2, y2 = game_screen.coords(paddle_right)
    if y1 > 20:
        game_screen.move(paddle_right, 0, -25)


def Down_P1(event):
    x1, y1, x2, y2 = game_screen.coords(paddle_right)
    if y2 < window_height - 20:
        game_screen.move(paddle_right, 0, 25)


# Control Mechanism
game_screen.bind('<Up>', Up_P1)
game_screen.bind('<Down>', Down_P1)
game_screen.bind('w', Up_P2)
game_screen.bind('s', Down_P2)
game_screen.focus_set()

# used for randomize direction only
game_screen.after(1000, collision_ballmovement)



if __name__ == '__main__':
    root.mainloop()
