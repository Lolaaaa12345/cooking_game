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

crab_in = False
fish_in = False
jelly_in = False
seahorse_in = False
squid_in = False

crab_out = False
fish_out = False
jelly_out = False
seahorse_out = False
squid_out = False

# crab_in_time = random.randint(0, 20)
crab_in_time = 57
fish_in_time = random.randint(5, 10)
jelly_in_time = random.randint(15, 16)
seahorse_in_time = random.randint(0, 15)
squid_in_time = random.randint(0, 5)

#time variables
user_hit_the_start_button = False
start_the_game_timer = time.time()
start_time = float(time.time())
current_time = start_time
time_countdown = 20


#render text for later
display_money = stats_font.render("$0", True, (0, 0, 0))
display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255, 255, 255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255, 255, 255))
display_instructions_three = instructions_font.render("To give a customer their order, walk into them", True, (255, 255, 255))

display_fries_status = stats_font.render("Fries: " + str(fries), True, (255, 255, 255))
display_burger_status = stats_font.render("Burger: " + str(burger), True, (255, 255, 255))
display_soda_status = stats_font.render("Soda: " + str(soda), True, (255, 255,255))

display_end_one = end_font.render("Congrats you made it to the end!", True, (255, 255, 255))

#characters rectangles

p = Player(500, 200)

crab = Crab(-100, -100)
fish = Fish(-100, -100)
jelly = Jellyfish(-100, -100)
seahorse = Seahorse(-100, -100)
squid = Squid(-100, -100)

s = Soda(710, 10)
f = Fries(710, 250)
b = Burger(710, 500)


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
                crab_move_in = True
            if round(total_time) == fish_in_time:
                fish_in = True
            if round(total_time) == jelly_in_time:
                jelly_in = True
            if round(total_time) == seahorse_in_time:
                seahorse_in = True
            if round(total_time) == squid_in_time:
                squid_in = True

        #to pick up food
        if p.rect.colliderect(s.rect):
            soda = True
        if p.rect.colliderect(b.rect):
            burger = True
        if p.rect.colliderect(f.rect):
            fries = True

        #to complete ordersd
        if p.rect.colliderect(crab.rect) and crab_out is False:
            money, crab_out, fries, burger, soda = crab.get_food(fries, soda, burger, money, crab_out)
            play_sound = True
            print("crab")
        if p.rect.colliderect(fish.rect) and fish_out is False:
            money, fish_out, fries, burger, soda = fish.get_food(fries, soda, burger, money, fish_out)
            play_sound = True
            print("fish")
        if p.rect.colliderect(jelly.rect) and jelly_out is False:
            money, jelly_out, fries, burger, soda = jelly.get_food(fries, soda, burger, money, jelly_out)
            play_sound = True
        if p.rect.colliderect(seahorse.rect) and seahorse_out is False:
            money, seahorse_out, fries, soda = seahorse.get_food(fries, soda, money, seahorse_out)
            play_sound = True
        if p.rect.colliderect(squid.rect) and squid_out is False:
            money, squid_out, burger, soda = squid.get_food(soda, burger, money, squid_out)
            play_sound = True


        if play_sound == True:
            mixer.music.play()
            play_sound = False

        if crab_in == True:
            crab.enter_restaurant(50, 50)
        if fish_in == True:
            fish.enter_restaurant(300, 50)
        if jelly_in == True:
            jelly.enter_restaurant(50, 250)
        if seahorse_in == True:
            seahorse.enter_restaurant(350, 250)
        if squid_in == True:
            squid.enter_restaurant(250, 450)




        #updating status
        display_money = stats_font.render(str(money), True, (0,0, 0))
        display_fries_status = stats_font.render("Fries: " + str(fries), True, (0,0, 0))
        display_burger_status = stats_font.render("Burger: " + str(burger), True, (0,0, 0))
        display_soda_status = stats_font.render("Soda: " + str(soda), True, (0,0, 0))

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
        if crab_in == True and crab_out is False:
            screen.blit(crab.image, crab.rect)
        if fish_in == True and fish_out is False:
            screen.blit(fish.image, fish.rect)
        if jelly_in == True and jelly_out is False:
            screen.blit(jelly.image, jelly.rect)
        if seahorse_in == True and seahorse_out is False:
            screen.blit(seahorse.image, seahorse.rect)
        if squid_in == True and squid_out is False:
            screen.blit(squid.image, squid.rect)
        screen.blit(p.image, p.rect)
        screen.blit(b.image, b.rect)
        screen.blit(s.image, s.rect)
        screen.blit(f.image, f.rect)
        screen.blit(display_fries_status, (10, 5))
        screen.blit(display_burger_status, (150, 5))
        screen.blit(display_soda_status, (300, 5))
        screen.blit(display_time, (10, 30))
        screen.blit(display_money, (10, 60))

        pygame.draw.rect(screen, (0, 0, 0), fish.rect, 2)
        pygame.display.update()

    elif game_over == True:
        screen.blit(night_background, (0,0))
        screen.blit(display_end_one, (20, 150))
        screen.blit(display_end_two, (40, 200))
        pygame.display.update()


pygame.display.update()
