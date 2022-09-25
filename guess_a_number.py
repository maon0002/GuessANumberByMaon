import random
computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid Input. Try again...")
        continue
    if int(player_input) == computer_number:
        print("You guess it!")
        break
    elif int(player_input) < computer_number:
        print("Too Low!")
    elif int(player_input) > computer_number:
        print("Too high!")

