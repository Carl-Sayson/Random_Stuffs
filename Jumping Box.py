import random
import tkinter.messagebox
from tkinter import *

root = Tk()
root.title('Flying Box')

screen_height = 500
screen_width = 750

# centerline for references
sc_height_mid = screen_height/2
sc_width_mid = screen_width/2

# how fast are the jumps and descend
dy_up = -20
dy_down = 20

# Stuffs used for the whole thing
score = 0
true_score = 0
points_hitbox = []
obstacles = []

# assets and display
game_screen = Canvas(root, height=screen_height, width=screen_width)

background = game_screen.create_rectangle(0, 0, screen_width, screen_height, fill='sky blue', width=0)
ground = game_screen.create_rectangle(0, sc_height_mid+150, screen_width, screen_height, fill='green', width=0)
character = game_screen.create_oval(sc_width_mid-25, sc_height_mid+100, sc_width_mid+25, sc_height_mid+150,
                                    fill='yellow')
score_display = game_screen.create_text(sc_width_mid, sc_height_mid-175, anchor='center',
                                        font=('Arial', 20), fill='black', text=('Score: ' + str(true_score)))
game_screen.pack()


def create_obs():
    box_height = random.randrange(200, 300)
    box_width = 100
    global obstacles
    # testing
    randomizer = ['Top', 'Bottom']
    rand = random.choice(randomizer)

    if rand == 'Top':
        box_obstacle = game_screen.create_rectangle(screen_width, 0, screen_width+box_width,
                                                    box_height, fill='light green', width=1)
        hitbox_block = game_screen.create_rectangle(screen_width, box_height, screen_width+box_width,
                                                    sc_height_mid+150, width=0)
        obstacles.append(box_obstacle)
        points_hitbox.append(hitbox_block)
        game_screen.after(2000, create_obs)

    elif rand == 'Bottom':
        box_obstacle = game_screen.create_rectangle(screen_width, sc_height_mid+150, screen_width + box_width,
                                                    sc_height_mid+150-box_height, fill='light green', width=1)
        hitbox_block = game_screen.create_rectangle(screen_width, sc_height_mid+150-box_height,
                                                    screen_width + box_width, 0, width=0)

        points_hitbox.append(hitbox_block)
        obstacles.append(box_obstacle)
        game_screen.after(2000, create_obs)


def moving_obs():
    global obstacles, true_score
    multiplier = 25*(true_score/10)
    for boxes in obstacles:
        game_screen.move(boxes, -25-multiplier, 0)
    for points in points_hitbox:
        game_screen.move(points, -25-multiplier, 0)
    game_screen.after(100, moving_obs)


def collision():
    global obstacles
    x1, y1, x2, y2 = game_screen.coords(character)
    for obstacle in obstacles:
        (x_1, y_1, x_2, y_2) = game_screen.coords(obstacle)
        if x2 > x_1 and y_2 > y1 and x1 < x_2 and y2 > y_1:
            tkinter.messagebox.showinfo('Game Over!', 'Your total score is: ' + str(true_score))
            return restart()
    game_screen.after(100, collision)


def score_displayer():
    global points_hitbox, score, true_score
    x1, y1, x2, y2 = game_screen.coords(character)
    for points in points_hitbox:
        (x_1, y_1, x_2, y_2) = game_screen.coords(points)
        if x2 >= x_1 and x1 <= x_2:
            score += 1
            if score == 6:
                true_score += int(score/6)
                game_screen.itemconfigure(score_display, text='Score: ' + str(true_score))
                score = 0

    game_screen.after(100, score_displayer)



def restart():
    global character, obstacles, points_hitbox, true_score
    for obstacle_made in obstacles:
        game_screen.delete(obstacle_made)
        game_screen.move(obstacle_made, screen_width, 0)
    for points in points_hitbox:
        game_screen.delete(points)
    obstacles.clear()
    points_hitbox.clear()
    game_screen.delete(character)
    character = game_screen.create_oval(sc_width_mid - 25, sc_height_mid + 100, sc_width_mid + 25, sc_height_mid + 150,
                                        fill='yellow')
    game_screen.itemconfigure(score_display, text='Score: ' + str(0))
    true_score -= true_score
    game_screen.pack()
    game_screen.after(100, collision)


def up(event):
    x1, y1, x2, y2 = game_screen.coords(character)
    if 8 <= y1:
        game_screen.move(character, 0, dy_up)


def down(event):
    x1, y1, x2, y2 = game_screen.coords(character)
    if sc_height_mid + 145 >= y2:
        game_screen.move(character, 0, dy_down)


game_screen.bind('<Up>', up)
game_screen.bind('<Down>', down)
game_screen.focus_set()

game_screen.after(1000, create_obs)
game_screen.after(100, moving_obs)
game_screen.after(100, collision)
game_screen.after(100, score_displayer)

if __name__ == '__main__':
    root.mainloop()
