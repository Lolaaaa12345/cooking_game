import pygame
import time

# set up pygame modules
pygame.init()
pygame.font.init()
stats_font = pygame.font.SysFont('Arial', 20)
instructions_font = pygame.font.SysFont('Times New Roman', 40)
end_font = pygame.font.SysFont('Times New Roaman', 50)

display_money = stats_font.render("$0", True, (255,255,255))

display_instructions_one = instructions_font.render("Fufill orders to make money!", True, (255,255,255))
display_instructions_two = instructions_font.render("Burgers are $5, fries $3 and soda $2", True, (255,255,255))
display_instructions_three = instructions_font.render("To give a customer their order, simply walk into them", True, (255,255,255))

display_day_end_one = end_font.render("Congrats! You made it to the end of the day")
display_day_end_two = end_font.render("You made $" + str(money_made) + " today!")

#variables:
customers_in_store = 0
money = 0
