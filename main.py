import pygame
import time
import random

from player import Player
from crab import Crab
from fish import Fish
from jellyfish import Jellyfish
from seahorse import Seahorse
from squid import Squid
from soda import Soda
from fries import Fries
from burger import Burger
from pygame import mixer


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
main_background = pygame.image.load("background new.png")

#variables:
customers_in_store = 0
money = 0
instructions = True
game_over = False
main_game = False

mixer.init()
mixer.music.load("cash ringer.mp3")
play_sound = False

burger = False
fries = False
soda = False
want_burger = False
want_fries = False
want_soda = False
collision = True

crab_in = False
fish_in = False
jelly_in = False
seahorse_in = False
squid_in = False

crab_in_time = random.randint(0, 20)
fish_in_time = random.randint(10, 30)
jelly_in_time = random.randint(20, 40)
seahorse_in_time = random.randint(30, 50)
squid_in_time = random.randint(40, 50)


#time variables
user_hit_the_start_button = False

start_the_game_timer = time.time()
start_time = float(time.time())
current_time = start_time
time_countdown = 60


#render text for later
display_money = stats_font.render("$0", True, (0, 0, 0))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255, 255, 255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255, 255, 255))
display_instructions_three = instructions_font.render("To give a customer their order, walk into them", True, (255, 255, 255))

display_end_one = end_font.render("Congrats you made it to the end!", True, (255, 255, 255))

#characters rectangles

p = Player(500, 200)

crab = Crab(600, 0)
fish = Fish(600, 0)
jelly = Jellyfish(600, 0)
seahorse = Seahorse(600, 0)
squid = Squid(600, 0)

s = Soda(710, 10)
f = Fries(710, 250)
b = Burger(710, 500)


def pay_burger(money):
    money = money + 5
    return money
def pay_fries(money):
    money = money + 3
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

            #bring the sprites in
            if round(total_time) == crab_in_time:
                crab_in = True
            if round(total_time) == fish_in_time:
                fish_in = True
            if round(total_time) == jelly_in_time:
                jelly = True
            if round(total_time) == seahorse_in_time:
                seahorse_in = True
            if round(total_time) == squid_in_time:
                squid_in = True

        if p.rect.colliderect(s.rect):
            soda = True
            print("picked up soda")
        if p.rect.colliderect(b.rect):
            burger = True
            print("picked up burger")
        if p.rect.colliderect(f.rect):
            fries = True
            print("picked up fries")

        if p.rect.colliderect(crab.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            play_sound = True
            complete_order(collision)
        if p.rect.colliderect(fish.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            play_sound = True
            complete_order(collision)
        if p.rect.colliderect(jelly.rect):
            want_burger = True
            want_fries = True
            want_soda = True
            collision = True
            play_sound = True
            complete_order(collision)
        if p.rect.colliderect(seahorse.rect):
            want_fries = True
            want_soda = True
            collision = True
            play_sound = True
            complete_order(collision)
        if p.rect.colliderect(squid.rect):
            want_burger = True
            want_soda = True
            collision = True
            play_sound = True
            complete_order(collision)

        if play_sound == True:
            mixer.music.play()
            play_sound = False

        display_money = stats_font.render(str(money), True, (0,0, 0))
        display_end_two = end_font.render("You  made $" + str(money) + " today", True, (255, 255, 255))


 # --- Main event loop
    screen.fill((173, 216, 230))
    if instructions:
        screen.blit(display_instructions_one, (150, 170))
        screen.blit(display_instructions_two, (90, 220))
        screen.blit(display_instructions_three, (30, 270))
        pygame.display.update()
    elif main_game:
        screen.blit(main_background, (0, 0))
        # if crab_in == True:
        screen.blit(crab.image, crab.rect)
        # if fish_in == True:
        screen.blit(fish.image, fish.rect)
        # if jelly_in == True:
        screen.blit(jelly.image, jelly.rect)
        # if seahorse_in == True:
        screen.blit(seahorse.image, seahorse.rect)
        # if squid_in == True:
        screen.blit(squid.image, squid.rect)
        screen.blit(p.image, p.rect)
        screen.blit(b.image, b.rect)
        screen.blit(s.image, s.rect)
        screen.blit(f.image, f.rect)
        screen.blit(display_time, (10, 5))
        screen.blit(display_money, (10, 30))

        pygame.draw.rect(screen, (0, 0, 0), f.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), s.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), b.rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), jelly.rect, 2)
        pygame.display.update()

    elif game_over == True:
        screen.blit(night_background, (0,0))
        screen.blit(display_end_one, (20, 150))
        screen.blit(display_end_two, (40, 200))
        pygame.display.update()


pygame.display.update()
