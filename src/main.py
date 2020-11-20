import random
import pygame
import tkinter as tk
from tkinter import messagebox

from entities.entity import Snake, Square


def draw_grid(w, row, surface):
    """
    initializes the grid
    :param w: the width - int
    :param row: the number of rows - int
    :param surface: Surface
    :return: -
    """
    size_between = w // row

    x = 0
    y = 0
    for lin in range(row):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    """
    when a game is lost, this function reinitialize the window
    :param surface: Surface
    :return: -
    """
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(row, item):
    """
    places a snack in a random cell that is free
    :param row: int
    :param item: a colour
    :return: the valid random position for the snack
    """
    positions = item.body

    while True:
        x = random.randrange(row)
        y = random.randrange(row)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    """

    :param subject:
    :param content:
    :return:
    """
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    """
    creates the main objects as snake (Snake), initializes the board, places a snack (Snack)
    every time the snake has moved, checks if there is still a snack on the board and if it isn't, it adds one
    stops the game if the snake made an illegal move
    :return:
    """
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Square(random_snack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Square(random_snack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Your score: ', len(s.body))
                message_box('You Lost!', 'Play again... ')
                s.reset((10, 10))
                break

        redraw_window(win)



main()
