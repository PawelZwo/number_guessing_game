from random import randint


def get_number():
    while True:
        try:
            user_pick = int(input("Guess the number: "))
            return user_pick
        except ValueError:
            print("It's not a number! Pick a number.")
    return user_pick


def guess_game():
    pc_pick = randint(1, 100)
    user_pick = get_number()
    while pc_pick != user_pick:
        if user_pick < pc_pick:
            print("Too small! Try again.")
        else:
            print("Too big! Try again.")
        user_pick = get_number()
    print(f"You Win! The number was {pc_pick}.")


print("Guess a number from 1 to 100! \n")

guess_game()
