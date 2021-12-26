import random
from game_data import data

def random_choices():
    return random.choice(data)

def account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},a {description}, from {country}"

def answer(chosen_a, chosen_b, guess):
    if chosen_a > chosen_b:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print("Welcome to higher or lower, please guess if A is higher or lower than B.")
    score = 0
    game_stop = False 
    chosen_a = random_choices()
    chosen_b = random_choices()

    while not game_stop:
        chosen_a = chosen_b 
        chosen_b = random_choices()

        while chosen_a == chosen_b:
            chosen_b = random_choices()

        print(f"Does A: {account_info(chosen_a)}, have more followers?")
        print("OR")
        print(f"Does B: {account_info(chosen_b)}, have more followers?")

        guess = input("Does 'A' or 'B' have more followers?: ").lower()
        follower_a = chosen_a["follower_count"]
        follower_b = chosen_b["follower_count"]
        correct_answer = answer(follower_a, follower_b, guess)

        if correct_answer:
            score += 1
            print(f"Correct! Your score is currently at {score}")
        else:
            print(f"You got it wrong. Your end score is {score}")
            game_continue = input("Would you like to play again? 'y' or 'n': ")
            if game_continue == 'y':
                play_game()
            else:
                game_stop = True
                print("Thank you for playing!")
play_game()