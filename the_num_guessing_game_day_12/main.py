from random import randint


easy_mode = 10
hard_mode = 5

def start_game():
    def hints(guess, answer, lives):
        if guess < answer:
            print("Your guess is too low.")
            return lives - 1
        elif guess > answer:
            print("Your guess is too high.")
            return lives - 1
        else:
            print("You guessed correctly. Congratulations!")


    def mode_selector():
        mode = input("Would you like to play this round on 'hard' or 'easy'?: ")
        if mode == 'easy':
            return easy_mode
        else:
            return hard_mode


    def game():
            print("Welcome to the number guessing game!")
            print("Please guess the number that was choosen, it is between 1 and 100.")
            answer = randint(1,101)


            lives = mode_selector()

            guess = 0

            while guess != answer:
                print(f"You have {lives} attempts, guess wisely.")
                guess = int(input("Please make your guess: "))

                lives = hints(guess,answer,lives)

                if lives == 0:
                    print("You ran out of lives.")
                    play_again = input("Would you like to play again? 'y' or 'n': ")
                    if play_again == 'y':
                        start_game()
                    else:
                        print("Thank you for playing")
                    break
                elif guess != answer:
                    print("Try again")
                

    game()
start_game()