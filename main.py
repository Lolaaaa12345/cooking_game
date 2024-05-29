import pygame
import time

from player import Player
from crab import Crab
from fish import Fish
from jellyfish import Jellyfish
from seahorse import Seahorse
from squid import Squid
from soda import Soda
from fries import Fries
from burger import Burger


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

player_load = pygame.image.load("player.png")

crab_load = pygame.image.load("crab food.png")
fish_load = pygame.image.load("fish food.png")
jellyfish_load = pygame.image.load("jellyfish food.png")
seahorse_load = pygame.image.load("sea horse.png")
squid_load = pygame.image.load("squid food.png")

soda_load = pygame.image.load("soda_station.png")
fries_load = pygame.image.load("fries_station.png")
burger_load = pygame.image.load("burger_station.png")

night_background = pygame.image.load("night_back.jpeg")

#variables:
customers_in_store = 0
money = 0
instructions = True
game_over = False
main_game = False

burger = False
fries = False
soda = False
want_burger = False
want_fries = False
want_soda = False
collision = True

#time variables
user_hit_the_start_button = False

start_the_game_timer = time.time()
start_time = float(time.time())
current_time = start_time
time_countdown = 5


#render text for later
display_money = stats_font.render("$0", True, (0, 0, 0))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255, 255, 255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255, 255, 255))
display_instructions_three = instructions_font.render("To give a customer their order", True, (255, 255, 255))
display_instructions_four = instructions_font.render("simply walk into them", True, (255, 255, 255))

#characters rectangles

p = Player(500, 200)

crab = Crab(600, 0)
fish = Fish(600, 0)
jelly = Jellyfish(600, 0)
seahorse = Seahorse(600, 0)
squid = Squid(600, 0)

soda = Soda(670, 200)
fries = Fries(550, 0)
burger = Burger(670, 400)

def pay_burger(money):
    money = money + 5
    return money
def pay_fries(money):
    money = money + 4
    return money
def pay_soda(money):
    money = money + 2
    return money
def complete_order(collision):
    if collision == True:
        if soda == True and want_soda == True:
            pay_soda(money)
            soda == False
            want_soda == False
        if burger == True and want_burger == True:
            pay_burger(money)
            burger == False
            want_burger == False
        if fries == True and want_fries == True:
            pay_fries(money)
            fries == False
            want_fries == False

run = True
# -------- Main Program Loop -----------
while run:
# --- Main event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_direction("right")
        print("right key pressed")
    if keys[pygame.K_a]:
        p.move_direction("left")
        print("left key pressed")
    if keys[pygame.K_w]:
        p.move_direction("up")
    if keys[pygame.K_s]:
        p.move_direction("down")

    #start the game, end instructions
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            instructions = False
            user_hit_the_start_button = True
            main_game = True
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
            display_time = stats_font.render("Time left: " + str(total_time) + "s", True, (0, 0, 0))
            if round(total_time) == 0:
                game_over = True
                main_game = False

        if p.rect.colliderect(soda.rect):
            soda = True
        if p.rect.colliderect(burger.rect):
            burger = True
        if p.rect.colliderect(soda.rect):
            soda = True

        if p.rect.colliderect(crab.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            complete_order(collision)
        if p.rect.colliderect(fish.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            complete_order(collision)
        if p.rect.colliderect(jelly.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            complete_order(collision)
        if p.rect.colliderect(seahorse.rect):
            want_fries = True
            want_soda = True
            collision = True
            complete_order(collision)
        if p.rect.colliderect(squid.rect):
            want_burger = True
            want_soda = True
            collision = True
            complete_order(collision)

        display_money = stats_font.render(str(money), True, (0,0, 0))



 # --- Main event loop
    screen.fill((173, 216, 230))
    if instructions:
        screen.blit(display_instructions_one, (30, 70))
        screen.blit(display_instructions_two, (30, 120))
        screen.blit(display_instructions_three, (30, 170))
        screen.blit(display_instructions_four, (30, 220))
        pygame.display.update()
    elif main_game:
        screen.fill((255, 255, 255))
        screen.blit(jelly.image, jelly.rect)
        screen.blit(p.image, p.rect)
        screen.blit(burger.image, burger.rect)
        screen.blit(soda.image, soda.rect)
        screen.blit(fries.image, fries.rect)
        screen.blit(display_time, (10, 5))
        screen.blit(display_money, (10, 30))
        pygame.display.update()

    elif game_over == True:
        screen.blit(night_background, (0,0))
        pygame.display.update()


pygame.display.update()
w