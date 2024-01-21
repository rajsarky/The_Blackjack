from art import logo
print(logo)

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)

