#initialisation
import pygame as pg
import sys
pg.init()
width = int(500)
height = int(600)
screen = pg.display.set_mode((800, 600))
border_colour =(255, 255, 255) 
border_thickness = 10
pg.display.set_caption("MiniMix")
font = pg.font.Font("Text_Font.ttf", 50)

#Main Game Loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((10,35,66))
    pg.display.flip()
pg.quit()
sys.exit()

#Game States
Menu = "menu"
Hangman = "hangman"
Number_Game = "2048"
current_state = "menu"

#Functions
def draw_text(text, font, color, surface, x, y):
    """Helper to draw text on screen"""
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y))
    surface.blit(txt, rect)
def menu_screen():
    screen.fill((226,109,90))
    draw_text("Welcome to MiniMix.", font,((0,0,0),screen,width//2,70))