import random  # In-built module that generates random stuff from list

while True:
    choices = ["r", "p", "s"]  # Definition of the list we are telling python to randomise

    cpu = random.choice(choices)  # choice function selects a random item from the list
    player = None

    while player not in choices:  # While loop is used here to iterate a line of code indefinitely until a certain
        # condition is met
        player = input("Choose one- Rock(R), Paper(P) or Scissors(S)?: ").lower()

        if player not in choices:
            print("Error! Try again")
        else:
            continue

    if player == cpu:
        print(f"Draw! Player({player}):CPU({cpu})")
        continue_game = input("Do you want to try again?: (y/n)").lower()
        if continue_game != "y":
            break
        else:
            continue

    elif player == "r":
        if cpu == "p":
            print(f"Player(Rock):CPU(Paper)")
            print("You lose!")
        if cpu == "s":
            print(f"Player(Rock):CPU(Scissors)")
            print("You win!")

    elif player == "p":
        if cpu == "s":
            print(f"Player(Paper):CPU(Scissors)")
            print("You lose!")
        if cpu == "r":
            print(f"Player(Paper):CPU(Rock)")
            print("You win!")

    elif player == "s":
        if cpu == "p":
            print(f"Player(Scissors):CPU(Paper)")
            print("You win!")
        if cpu == "r":
            print(f"Player(Scissors):CPU(Rock)")
            print("You lose!")

    play_again = input("Would you like to play again? (Y/N): ").lower()
    if play_again != "y":
        break
print("Thank you for playing!")
