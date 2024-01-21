import random

# from art import logo
# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)

print(f"Your cards: {my_cards} , current score: {sum(my_cards)}")
print(f"Computer's first card: {computer_cards[0]}")


def player_win(my_total_points):
    print(f"""Your cards: {my_cards}, Your total: {my_total_points} 
    Computer cards: {computer_cards}, Computer total: {sum(computer_cards)}""")
    if my_total_points > 21:
        print("You lose.")
    elif sum(computer_cards) > my_total_points:
        print("You lose.")
    else:
        print("You win!")


should_continue_asking = True

choice_of_the_player = ""
while should_continue_asking:
    choice_of_the_player = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if choice_of_the_player == "y" or choice_of_the_player == "n":
        should_continue_asking = False

if choice_of_the_player == "y":
    hit = random.choice(cards)
    my_cards.append(hit)
    player_win(sum(my_cards))
else:
    player_win(sum(my_cards))

