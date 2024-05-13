import pygame
import time
from player import Player

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

#time variables
user_hit_the_start_button = False
start_the_game_timer = time.time()

start_time = float(time.time())
current_time = start_time
time_countdown = 60


#render for later
display_money = stats_font.render("$0", True, (255,255,255))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255, 255, 255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255, 255, 255))
display_instructions_three = instructions_font.render("To give a customer their order, simply walk into them", True, (255, 255, 255))

# display_day_end_one = end_font.render("Congrats! You made it to the end of the day", True, (255, 255, 255))
# display_day_end_two = end_font.render("You made $" + str(money_made) + " today!", True, (255, 255, 255))

p = Player(500, 200)

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
    if instructions == False:
        if user_hit_the_start_button:
            start_the_game_timer = time.time()
            user_hit_the_start_button = False
        current_time = time.time()
        for i in range(1):
            current_time = current_time + 1
            total_time = round(time_countdown - (current_time - start_the_game_timer), 2)
            display_time = my_font.render("Time left: " + str(total_time) + "s", True, (255, 255, 255))
            if round(total_time) == 0:

 # --- Main event loop
    screen.fill((100, 10, 60))
    if instructions:
        screen.blit(display_instructions_one, (30, 70))
        screen.blit(display_instructions_two, (30, 120))
        screen.blit(display_instructions_three, (30, 170))
    else:
        screen.blit(p.image, p.rect)


pygame.display.update()


