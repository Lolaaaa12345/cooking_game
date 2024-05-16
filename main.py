import pygame
import time
from player import Player
from jellyfish import Jellyfish
from squid import Squid

# set up pygame modules
pygame.init()
pygame.font.init()
stats_font = pygame.font.SysFont('Arial', 20)
instructions_font = pygame.font.SysFont('Times New Roman', 40)
end_font = pygame.font.SysFont('Times New Roman', 50)

#set up variables for the display
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

player_load = pygame.image.load("chef real.png")
jellyfish_load = pygame.image.load("jellyfish food.png")
squid_load = pygame.image.load("squid food.png")
# seahorse_load = pygame.image.load("seahorse food.png")
#fish_load = pygame.image.load("fish food.png")

#variables:
customers_in_store = 0
money = 0
instructions = True
user_hit_the_start_button = False

#time variables
user_hit_the_start_button = False


#render text for later
display_money = stats_font.render("$0", True, (255,255,255))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255, 255, 255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255, 255, 255))
display_instructions_three = instructions_font.render("To give a customer their order", True, (255, 255, 255))
display_instructions_four = instructions_font.render("simply walk into them", True, (255, 255, 255))

#characters rectangles

p = Player(500, 200)

#all the characters come in from lower left coords (600, 0)
jelly = Jellyfish(600, 0)
squid = Squid(600, 0)


run = True
# -------- Main Program Loop -----------
while run:
# --- Main event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_direction("right")
    if keys[pygame.K_a]:
        p.move_direction("left")
    if keys[pygame.K_w]:
        p.move_direction("up")
    if keys[pygame.K_s]:
        p.move_direction("down")

    #start the game, end instructions
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            instructions = False
            user_hit_the_start_button = True
        if event.type == pygame.QUIT:
            run = False
    # if instructions == False:
    #     if user_hit_the_start_button:
    #         start_the_game_timer = time.time()
    #         user_hit_the_start_button = False
    #     current_time = time.time()
    #     for i in range(1):
    #         current_time = current_time + 1
    #         total_time = round(time_countdown - (current_time - start_the_game_timer), 2)
    #         display_time = stats_font.render("Time left: " + str(total_time) + "s", True, (255, 255, 255))


 # --- Main event loop
    screen.fill((173, 216, 230))
    if instructions:
        screen.blit(display_instructions_one, (30, 70))
        screen.blit(display_instructions_two, (30, 120))
        screen.blit(display_instructions_three, (30, 170))
        screen.blit(display_instructions_four, (30, 220))
        pygame.display.update()
    else:
        screen.fill((255, 255, 255))
        screen.blit(p.image, p.rect)
        pygame.display.update()


pygame.display.update()


