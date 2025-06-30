import time
import random


def menu():
    time.sleep(1)
    print("Tic-Tac-Toe Game")
    print("Press 1 to play against players")
    print("Press 2 to play against AI")
    print("Press 3 to Exit")

    while True:
        menu_choice = input("Your choice: \n")
        if menu_choice == "1":
            player_vs_player.board_create()
        elif menu_choice == "2":
            player_vs_ai.board_create()
        elif menu_choice == "3":
            print("Thanks for Playing!")
            time.sleep(1)
            break
        else:
            print("Wrong input. Try again")


class Game:
    def __init__(self, gameplay):
        self.game_style = gameplay
        self.player_turn = True
        self.board = [["-" for x in range(3)] for y in range(3)]

    def board_create(self):
        for grid_board in self.board:
            print(grid_board)

        if self.game_style == "PVP":
            self.pvp()

        if self.game_style == "PVAI":
            self.pvai()

    def pvp(self):
        if self.player_turn is True:
            self.placement_putter("Player 1's turn")
        else:
            self.placement_putter("Player 2's turn")

    def placement_putter(self, player_turn):
        print(player_turn)
        self.row = input("Input what row to put: ")
        self.column = input("Input what column to put: ")
        try:
            if self.row.isdigit() and self.column.isdigit():
                if (self.board[int(self.row)][int(self.column)] == "O" or
                        self.board[int(self.row)][int(self.column)] == "X"):
                    print("Place on other tiles")
                    self.board_create()
                else:
                    row, col = int(self.row), int(self.column)
                    if 0 <= row < 3 and 0 <= col < 3:
                        if self.board[row][col] == "-":
                            self.board[row][col] = "O" if player_turn == "Player 1's turn" else "X"
                            self.player_turn = not self.player_turn
                            self.checker(player_turn)
            else:
                print("Value must be a number")
                self.board_create()
        except IndexError:
            print("Must be a number within 0 and 2")
            self.board_create()

    def pvai(self):
        if self.player_turn is True:
            self.placement_putter("Player 1's turn")
        else:
            while True:
                self.row = random.randrange(0, 3)
                self.column = random.randrange(0, 3)
                if self.board[self.row][self.column] == "-":
                    self.board[self.row][self.column] = "X"
                    self.player_turn = True
                    self.checker('AI')
                else:
                    continue

    def checker(self, player_turn):
        if "-" not in [column for row in self.board for column in row]:
            self.show_winner_board(player_turn, 'Draw')

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != "-":
                self.show_winner_board(player_turn, 'Win')

        for row in self.board:
            if row[0] == row[1] == row[2] != "-":
                self.show_winner_board(player_turn, 'Win')

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
            self.show_winner_board(player_turn, 'Win')
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != "-":
            self.show_winner_board(player_turn, 'Win')
        else:
            self.board_create()

    def show_winner_board(self, player_turn, win):
        for grid_board in self.board:
            print(grid_board)
        if win == "Win":
            print(f"{player_turn} wins the game! \n")
            self.board_reset()
        if win == "Draw":
            print(f"The game is a {win}! \n")
            self.board_reset()

    def board_reset(self):
        self.player_turn = True
        self.board = [["-" for x in range(3)] for y in range(3)]
        time.sleep(2)
        return menu()


player_vs_player = Game("PVP")

player_vs_ai = Game("PVAI")

if __name__ == "__main__":
    menu()
