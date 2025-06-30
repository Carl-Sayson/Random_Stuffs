# My version of this game; Practice lang
# Computer lang kalaban natin

import time # bigay ng reliever sa mga players
import random # chooses random number

def menu():
    print("Welcome to Mastermind Game: Python Edition!\n"
          "--- Choose your difficulty ---\n"
          "\n"
          "1 - Easy\n"
          "2 - Medium\n"
          "3 - Hard\n"
          "Type EXIT to quit the game\n")

    while True:
        players_choice = input("--> ")
    # Declaration of instances for the object
        mind_game_easy = Main_game(10, 100, 2)
        mind_game_medium = Main_game(100, 1000, 3)
        mind_game_hard = Main_game(1000, 10000, 4)
        # Difficulty choice for the players
        if players_choice == "1":
            mind_game_easy.game()
        elif players_choice.upper() == "2":
            mind_game_medium.game()
        elif players_choice == "3":
            mind_game_hard.game()
        elif players_choice == "EXIT":
            return False
        else:
            print('Please input the correct choice \n')


class Main_game:
    def __init__(self, lower_bound, upper_bound, length):
        self.lower = lower_bound
        self.upper = upper_bound
        self.tries = 0 # used for showing how many tries
        # used if the number guessed by the user is similar to the length of the actual answer
        self.length = length

    def game(self):
        self.num_guessr = str(random.randint(self.lower, self.upper))
        self.answer_user = input(f'Guess the number with {self.length} digits: ')
        time.sleep(1)

        # sees if the player gets it 1st time
        if self.num_guessr == self.answer_user:
            print("Correct! Got it first time! \n"
                  "You are a true Mastermind! \n")
            time.sleep(2)
            menu()
        else:
            self.continuation()

    def continuation(self):
        # used for checking the numbers guessed if it's in their or not
        while self.answer_user != self.num_guessr:
            self.tries += 1
            # used for showing the guessed numbers
            self.current_guessed_num = []

            if len(self.answer_user) != len(self.num_guessr):
                print(f"You must guess with {self.length} digit/s")
                time.sleep(2)
            else:
                for value in range(0, self.length):
                    if self.answer_user[value] != self.num_guessr[value]:
                        self.current_guessed_num.append('X')
                    else:
                        self.current_guessed_num.append(str(self.answer_user[value]))

            for num in self.current_guessed_num:
                print(num, end=" ")
            self.answer_user = input(f'\nGuess the number with {self.length} digits: '
                                     )

        if self.answer_user == self.num_guessr:
            self.tries += 1
            print(f"Congratulations! You have now become a Mastermind!\n"
                  f"It only took {self.tries} tries to guess."
                  f"")
            time.sleep(2)
            menu()

# For convention purposes and only runs this script
if __name__ == '__main__':
    menu()
