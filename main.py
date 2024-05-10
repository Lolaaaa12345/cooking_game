import pygame
import time

# set up pygame modules
pygame.init()
pygame.font.init()
stats_font = pygame.font.SysFont('Arial', 20)
instructions_font = pygame.font.SysFont('Times New Roman', 40)
end_font = pygame.font.SysFont('Times New Roaman', 50)

#set up variables for the display
size = (800,600)
screen = pygame.display.set.mode(size)

background = pygame.image.load("temp_background.jpeg")
player_load = pygame.image.load("chef real.png")
jellyfish_load = pygame.image.load("jellyfish food.png")
# squid_load = pygame.image.load("squid food.png")
# seahorse_load = pygame.image.load("seahorse food.png")
#fish_load = pygame.image.load("fish food.png")

#variables:
customers_in_store = 0
money = 0

start_time = float(time.time())
current_time = start_time
time_countdown = 60

#render for later
display_money = stats_font.render("$0", True, (255,255,255))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255,255,255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255,255,255))
display_instructions_three = instructions_font.render("To give a customer their order, simply walk into them", True, (255,255,255))

display_day_end_one = end_font.render("Congrats! You made it to the end of the day")
display_day_end_two = end_font.render("You made $" + str(money_made) + " today!")

run = True
# -------- Main Program Loop -----------
while run:
# --- Main event loop
    for event in pygame.event.get():  # User did something
        #change to chef
    if keys[pygame.K_d]:
        f.move_direction("right")
    if keys[pygame.K_a]:
        f.move_direction("left")
    if keys[pygame.K_w]:
        f.move_direction("up")
    if keys[pygame.K_s]: