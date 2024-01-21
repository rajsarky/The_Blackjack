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
    if my_total_points == sum(computer_cards):
        print("It's a draw.")
    elif my_total_points > 21:
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


def ace():
    ace_handling = ""
    temp = False
    while not temp:
        if choice_of_the_player == "y":
            if my_cards[0] == 11 or my_cards[1] == 11:
                ace_handling = input(
                    f"You got an 'Ace', you have: {my_cards}, do you want to count the Ace as 1? (y or n)")
            else:
                ace_handling = input(
                    f"You got an 'Ace', computer has {computer_cards}, you have: {my_cards}, do you want to count the Ace as 1? (y or n)")
            if ace_handling == "y" or "n":
                temp = True

    if ace_handling == "n" and choice_of_the_player == "n":
        my_cards[my_cards.index(11)] = 11
    elif ace_handling == "n" and choice_of_the_player == "y":
        my_cards.append(11)
    elif ace_handling == "y" and choice_of_the_player == "n":
        my_cards[my_cards.index(11)] = 1
    else:
        my_cards.append(1)


if choice_of_the_player == "y" and 11 not in my_cards:
    hit = random.choice(cards)
    if hit == 11:
        ace()
        player_win(sum(my_cards))
    else:
        my_cards.append(hit)
        player_win(sum(my_cards))
elif choice_of_the_player == "y" and 11 in my_cards:
    hit = random.choice(cards)
    if hit == 11:
        ace()
        print("you have another 'Ace', what do you want to count ")
        ace()
        player_win(sum(my_cards))
    else:
        my_cards.append(hit)
        player_win(sum(my_cards))
elif choice_of_the_player == "n" and 11 not in my_cards:
    player_win(sum(my_cards))
elif choice_of_the_player == "n" and 11 in my_cards:
    ace()
    print(sum(my_cards))
