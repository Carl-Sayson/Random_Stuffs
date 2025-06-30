from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        self.form = Menu
        Menu.resize(351, 197)
        Menu.setMinimumSize(QtCore.QSize(351, 197))
        Menu.setMaximumSize(QtCore.QSize(351, 197))
        Menu.setStyleSheet("background-color: rgb(217, 215, 149);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Menu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Menu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Submit_2 = QtWidgets.QPushButton(Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Submit_2.setFont(font)
        self.Submit_2.setStyleSheet("background-color: rgb(110, 255, 85);")
        self.Submit_2.setObjectName("Submit_2")
        self.gridLayout.addWidget(self.Submit_2, 1, 0, 1, 1)
        self.Exit = QtWidgets.QPushButton(Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("background-color: rgb(255, 155, 125);")
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        self.Submit_2.clicked.connect(self.game)
        self.Exit.clicked.connect(self.form.close)

    def game(self):
        self.window = QtWidgets.QWidget()
        self.ui = Game()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "Pattern Sequence Game!"))
        self.Submit_2.setText(_translate("Menu", "Play"))
        self.Exit.setText(_translate("Menu", "Exit"))


class Game(object):
    def __init__(self):
        # will be used for the sequences of the game whether they pair or not
        self.sequences_game = []
        self.user_answers = []
        # score to show
        self.score = 0
        # how many games to play
        self.rounds = 1
        # Welp you are back again
        self.rounds_to_get_to = 0

    def setupUi(self, Game):
        Game.setObjectName("Game")
        self.form = Game
        Game.resize(350, 500)
        Game.setMinimumSize(QtCore.QSize(350, 500))
        Game.setMaximumSize(QtCore.QSize(350, 500))
        Game.setAutoFillBackground(False)
        Game.setStyleSheet("background-color: rgb(217, 215, 149);")
        self.gridLayout_5 = QtWidgets.QGridLayout(Game)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Exit = QtWidgets.QPushButton(Game)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("background-color: rgb(255, 155, 125);\n"
"\n"
"")
        self.Exit.setObjectName("Exit")
        self.gridLayout_3.addWidget(self.Exit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.Current_Score = QtWidgets.QLabel(Game)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Current_Score.setFont(font)
        self.Current_Score.setObjectName("Current_Score")
        self.gridLayout_3.addWidget(self.Current_Score, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.Correct_or_Wrong = QtWidgets.QLabel(Game)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Correct_or_Wrong.setFont(font)
        self.Correct_or_Wrong.setText("")
        self.Correct_or_Wrong.setAlignment(QtCore.Qt.AlignCenter)
        self.Correct_or_Wrong.setObjectName("Correct_or_Wrong")
        self.gridLayout_2.addWidget(self.Correct_or_Wrong, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Left_up_mid = QtWidgets.QPushButton(Game)
        self.Left_up_mid.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_up_mid.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_up_mid.setText("")
        self.Left_up_mid.setObjectName("Left_up_mid")
        self.gridLayout.addWidget(self.Left_up_mid, 0, 1, 1, 1)
        self.Left_up = QtWidgets.QPushButton(Game)
        self.Left_up.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_up.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_up.setText("")
        self.Left_up.setObjectName("Left_up")
        self.gridLayout.addWidget(self.Left_up, 0, 0, 1, 1)
        self.right_mid_1 = QtWidgets.QPushButton(Game)
        self.right_mid_1.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_1.setMaximumSize(QtCore.QSize(70, 70))

        self.right_mid_1.setText("")
        self.right_mid_1.setObjectName("right_mid_1")
        self.gridLayout.addWidget(self.right_mid_1, 1, 3, 1, 1)
        self.Right_mid_mid_down = QtWidgets.QPushButton(Game)
        self.Right_mid_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Right_mid_mid_down.setMaximumSize(QtCore.QSize(70, 70))

        self.Right_mid_mid_down.setText("")
        self.Right_mid_mid_down.setObjectName("Right_mid_mid_down")
        self.gridLayout.addWidget(self.Right_mid_mid_down, 2, 2, 1, 1)
        self.Left_mid_2 = QtWidgets.QPushButton(Game)
        self.Left_mid_2.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_2.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_mid_2.setText("")
        self.Left_mid_2.setObjectName("Left_mid_2")
        self.gridLayout.addWidget(self.Left_mid_2, 2, 0, 1, 1)
        self.Left_mid_mid_down = QtWidgets.QPushButton(Game)
        self.Left_mid_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_down.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_mid_mid_down.setText("")
        self.Left_mid_mid_down.setObjectName("Left_mid_mid_down")
        self.gridLayout.addWidget(self.Left_mid_mid_down, 2, 1, 1, 1)
        self.Left_down = QtWidgets.QPushButton(Game)
        self.Left_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_down.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_down.setText("")
        self.Left_down.setObjectName("Left_down")
        self.gridLayout.addWidget(self.Left_down, 3, 0, 1, 1)
        self.right_mid_mid_up = QtWidgets.QPushButton(Game)
        self.right_mid_mid_up.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_mid_up.setMaximumSize(QtCore.QSize(70, 70))

        self.right_mid_mid_up.setText("")
        self.right_mid_mid_up.setObjectName("right_mid_mid_up")
        self.gridLayout.addWidget(self.right_mid_mid_up, 1, 2, 1, 1)
        self.Left_mid_1 = QtWidgets.QPushButton(Game)
        self.Left_mid_1.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_1.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_mid_1.setText("")
        self.Left_mid_1.setObjectName("Left_mid_1")
        self.gridLayout.addWidget(self.Left_mid_1, 1, 0, 1, 1)
        self.right_up = QtWidgets.QPushButton(Game)
        self.right_up.setMinimumSize(QtCore.QSize(70, 70))
        self.right_up.setMaximumSize(QtCore.QSize(70, 70))

        self.right_up.setText("")
        self.right_up.setAutoDefault(False)
        self.right_up.setFlat(False)
        self.right_up.setObjectName("right_up")
        self.gridLayout.addWidget(self.right_up, 0, 3, 1, 1)
        self.right_mid_2 = QtWidgets.QPushButton(Game)
        self.right_mid_2.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_2.setMaximumSize(QtCore.QSize(70, 70))

        self.right_mid_2.setText("")
        self.right_mid_2.setObjectName("right_mid_2")
        self.gridLayout.addWidget(self.right_mid_2, 2, 3, 1, 1)
        self.right_down = QtWidgets.QPushButton(Game)
        self.right_down.setMinimumSize(QtCore.QSize(70, 70))
        self.right_down.setMaximumSize(QtCore.QSize(70, 70))

        self.right_down.setText("")
        self.right_down.setObjectName("right_down")
        self.gridLayout.addWidget(self.right_down, 3, 3, 1, 1)
        self.left_mid_down = QtWidgets.QPushButton(Game)
        self.left_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.left_mid_down.setMaximumSize(QtCore.QSize(70, 70))

        self.left_mid_down.setText("")
        self.left_mid_down.setObjectName("left_mid_down")
        self.gridLayout.addWidget(self.left_mid_down, 3, 1, 1, 1)
        self.right_mid_down = QtWidgets.QPushButton(Game)
        self.right_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_down.setMaximumSize(QtCore.QSize(70, 70))

        self.right_mid_down.setText("")
        self.right_mid_down.setObjectName("right_mid_down")
        self.gridLayout.addWidget(self.right_mid_down, 3, 2, 1, 1)
        self.Left_mid_mid_up = QtWidgets.QPushButton(Game)
        self.Left_mid_mid_up.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_up.setMaximumSize(QtCore.QSize(70, 70))

        self.Left_mid_mid_up.setText("")
        self.Left_mid_mid_up.setObjectName("Left_mid_mid_up")
        self.gridLayout.addWidget(self.Left_mid_mid_up, 1, 1, 1, 1)
        self.right_up_mid = QtWidgets.QPushButton(Game)
        self.right_up_mid.setMinimumSize(QtCore.QSize(70, 70))
        self.right_up_mid.setMaximumSize(QtCore.QSize(70, 70))

        self.right_up_mid.setText("")
        self.right_up_mid.setObjectName("right_up_mid")
        self.gridLayout.addWidget(self.right_up_mid, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.Submit = QtWidgets.QPushButton(Game)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("background-color: rgb(138, 255, 152);\n"
"")
        self.Submit.setFlat(False)
        self.Submit.setObjectName("Submit")
        self.gridLayout_4.addWidget(self.Submit, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

        # Go back to menu
        self.Exit.clicked.connect(self.back)

        # The users answer per button pressed
        self.Left_up.clicked.connect(lambda: self.user_answers.append(self.Left_up.objectName))
        self.Left_down.clicked.connect(lambda: self.user_answers.append(self.Left_down.objectName))
        self.Left_mid_1.clicked.connect(lambda: self.user_answers.append(self.Left_mid_1.objectName))
        self.Left_mid_2.clicked.connect(lambda: self.user_answers.append(self.Left_mid_2.objectName))
        self.Left_up_mid.clicked.connect(lambda: self.user_answers.append(self.Left_up_mid.objectName))
        self.Left_mid_mid_up.clicked.connect(lambda: self.user_answers.append(self.Left_mid_mid_up.objectName))
        self.left_mid_down.clicked.connect(lambda: self.user_answers.append(self.left_mid_down.objectName))
        self.Left_mid_mid_down.clicked.connect(lambda: self.user_answers.append(self.Left_mid_mid_down.objectName))
        self.right_mid_mid_up.clicked.connect(lambda: self.user_answers.append(self.right_mid_mid_up.objectName))
        self.right_mid_1.clicked.connect(lambda: self.user_answers.append(self.right_mid_1.objectName))
        self.right_mid_2.clicked.connect(lambda: self.user_answers.append(self.right_mid_2.objectName))
        self.Right_mid_mid_down.clicked.connect(lambda: self.user_answers.append(self.Right_mid_mid_down.objectName))
        self.right_mid_down.clicked.connect(lambda: self.user_answers.append(self.right_mid_down.objectName))
        self.right_up.clicked.connect(lambda: self.user_answers.append(self.right_up.objectName))
        self.right_down.clicked.connect(lambda: self.user_answers.append(self.right_down.objectName))
        self.right_up_mid.clicked.connect(lambda: self.user_answers.append(self.right_up_mid.objectName))

        # checks whether the users' answer is correct or not
        self.Submit.clicked.connect(self.submitted_answers)

        # displays user's score
        self.Current_Score.setText(f"Score: {str(self.score)}")

        # calls the start of the pattern
        self.game_loop()

    def game_loop(self):
        # used for looping how many times in the game
        if self.rounds == self.rounds_to_get_to:
            # this thing should hopefully work as the main looping system
            self.rounds_to_get_to -= self.rounds_to_get_to
            self.reset_tiles()
        else:
            self.pattern_game()

    def pattern_game(self):
        # Randomly choose a button to change its color
        self.choices_list = [self.Left_up, self.Left_up_mid, self.left_mid_down, self.Left_down,
                           self.Left_mid_mid_up, self.Left_mid_1, self.Left_mid_2, self.Left_mid_mid_down,
                           self.right_mid_mid_up, self.right_mid_1, self.right_mid_2, self.Right_mid_mid_down,
                           self.right_mid_down, self.right_up, self.right_down, self.right_up_mid]

        for color_buttons in self.choices_list:
            color_buttons.setStyleSheet("background-color: rgb(85, 170, 255);")

        # starting of the timer for interval
        QTimer.singleShot(800, self.tile_colored)

    def tile_colored(self):
        # chooses a random tile for the color to change and memorize
        self.randomizer = random.choice(self.choices_list)
        self.randomizer.setStyleSheet("background-color: red")
        # Add one new random tile to the sequence
        self.sequences_game.append(self.randomizer.objectName)
        QTimer.singleShot(500, self.reset_tiles_and_show_nxt)

    def reset_tiles_and_show_nxt(self):
        # resetting all tiles to normal then going back to show the other sequence
        for tiles in self.choices_list:
            tiles.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rounds_to_get_to += 1
        self.game_loop()

    def reset_tiles(self):
        # resetting all tiles to normal
        for tiles in self.choices_list:
            tiles.setStyleSheet("background-color: rgb(85, 170, 255);")

    def submitted_answers(self):
        if self.user_answers != self.sequences_game:
            info = "Game Over"
            QtWidgets.QMessageBox.information(None, "Game Over", info)
            self.reset_game()
        else:
            self.user_answers.clear()
            self.sequences_game.clear()
            self.rounds += 1 # updates the round
            self.score += 1
            self.Current_Score.setText(f"Score: {str(self.score)}") # updates hopefully the score
            self.game_loop()

    def reset_game(self):
        # resets the game
        self.score = 0
        self.rounds = 1
        self.user_answers.clear()
        self.sequences_game.clear()
        self.Current_Score.setText(f"Score: {str(self.score)}")
        self.game_loop()

    def back(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Pattern Sequence"))
        self.Exit.setText(_translate("Game", "<---"))
        self.Current_Score.setText(_translate("Game", "Score:"))
        self.Submit.setText(_translate("Game", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
