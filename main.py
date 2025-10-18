import pygame as pg
import random
import sys

pg.init()

width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Word Guessing Game")
font = pg.font.Font("Text_Font.ttf", 40)
small_font = pg.font.Font("Text_Font.ttf", 30)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BURNT_SIENNA = (233, 116, 81)
GRAY = (200, 200, 200)
GREEN = (0, 180, 0)
RED = (200, 0, 0)

def draw_text(text, font, color, surface, x, y):
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y))
    surface.blit(txt, rect)
    return rect

categories = {
    1: ['hadestown', 'hamilton', 'six', 'mamma mia', 'wicked'],
    2: ['cheesecake', 'brownie', 'applepie', 'tiramisu', 'icecream', 'cupcake', 'pudding'],
    3: ['football', 'basketball', 'tennis', 'cricket', 'hockey', 'golf', 'netball'],
}
category_names = {1: "Musicals", 2: "Desserts", 3: "Sports"}

# --- Game states ---
MENU = "menu"
PLAYING = "playing"
END = "end"

state = MENU
chosen_word = ""
guesses = ""
turns = 12
message = ""

# --- Main loop ---
running = True
while running:
    screen.fill(BURNT_SIENNA)
    mouse_pos = pg.mouse.get_pos()
    clicked = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
        elif event.type == pg.KEYDOWN and state == PLAYING:
            if event.unicode.isalpha():
                guess = event.unicode.lower()
                if guess not in guesses:
                    guesses += guess
                    if guess not in chosen_word:
                        turns -= 1
                        if turns == 0:
                            state = END
                            message = f"You Lose! The word was '{chosen_word}'."
                    else:
                        # Check win
                        if all(ch in guesses or ch == " " for ch in chosen_word):
                            state = END
                            message = f"You Win! The word was '{chosen_word}'."

    if state == MENU:
        draw_text("Choose a Category", font, BLACK, screen, width//2, 100)
        btns = []
        y = 250
        for i, name in category_names.items():
            rect = draw_text(f"{i}. {name}", small_font, BLACK, screen, width//2, y)
            btns.append((rect, i))
            y += 80

        if clicked:
            for rect, cat_num in btns:
                if rect.collidepoint(mouse_pos):
                    chosen_word = random.choice(categories[cat_num])
                    guesses = ""
                    turns = 12
                    state = PLAYING

    elif state == PLAYING:
        draw_text("Word Guessing Game", font, BLACK, screen, width//2, 50)
        draw_text(f"Turns left: {turns}", small_font, BLACK, screen, width//2, 100)

        # Display word progress
        display_word = ""
        for ch in chosen_word:
            if ch == " ":
                display_word += "   "
            elif ch in guesses:
                display_word += ch + " "
            else:
                display_word += "_ "
        draw_text(display_word.strip(), font, BLACK, screen, width//2, height//2)

        draw_text("Type letters to guess!", small_font, BLACK, screen, width//2, height - 100)


    elif state == END:
        draw_text(message, font, GREEN if "Win" in message else RED, screen, width//2, height//2)
        rect = draw_text("Click to return to menu", small_font, BLACK, screen, width//2, height - 100)
        if clicked and rect.collidepoint(mouse_pos):
            state = MENU

    pg.display.flip()

pg.quit()
sys.exit()
