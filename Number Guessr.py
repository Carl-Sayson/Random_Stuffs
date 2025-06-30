from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys


class Ui_Starting_Menu(object):
    def setupUi(self, Starting_Menu):
        self.form = Starting_Menu
        Starting_Menu.setObjectName("Starting_Menu")
        Starting_Menu.resize(1000, 700)
        Starting_Menu.setMinimumSize(QtCore.QSize(750, 500))
        Starting_Menu.setMaximumSize(QtCore.QSize(1000, 700))
        self.BG_Main = QtWidgets.QLabel(Starting_Menu)
        self.BG_Main.setEnabled(True)
        self.BG_Main.setGeometry(QtCore.QRect(1, 1, 998, 698))
        self.BG_Main.setMinimumSize(QtCore.QSize(750, 500))
        self.BG_Main.setMaximumSize(QtCore.QSize(1000, 700))
        self.BG_Main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BG_Main.setText("")
        self.BG_Main.setPixmap(QtGui.QPixmap("../Picture Assets/start_bg.png"))
        self.BG_Main.setScaledContents(True)
        self.BG_Main.setObjectName("BG_Main")
        self.exit_bt = QtWidgets.QPushButton(Starting_Menu)
        self.exit_bt.setGeometry(QtCore.QRect(329, 470, 354, 129))
        self.exit_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.exit_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Picture Assets/buttons_game_exit-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_bt.setIcon(icon)
        self.exit_bt.setIconSize(QtCore.QSize(350, 350))
        self.exit_bt.setDefault(True)
        self.exit_bt.setFlat(False)
        self.exit_bt.setObjectName("exit_bt")
        self.credits_bt = QtWidgets.QPushButton(Starting_Menu)
        self.credits_bt.setGeometry(QtCore.QRect(515, 332, 354, 129))
        self.credits_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.credits_bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Picture Assets/buttons_game_credits-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.credits_bt.setIcon(icon1)
        self.credits_bt.setIconSize(QtCore.QSize(350, 350))
        self.credits_bt.setDefault(True)
        self.credits_bt.setFlat(False)
        self.credits_bt.setObjectName("credits_bt")
        self.start_bt = QtWidgets.QPushButton(Starting_Menu)
        self.start_bt.setGeometry(QtCore.QRect(142, 332, 354, 129))
        self.start_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.start_bt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Picture Assets/buttons_game_start-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_bt.setIcon(icon2)
        self.start_bt.setIconSize(QtCore.QSize(350, 350))
        self.start_bt.setDefault(True)
        self.start_bt.setFlat(False)
        self.start_bt.setObjectName("start_bt")

        self.retranslateUi(Starting_Menu)
        QtCore.QMetaObject.connectSlotsByName(Starting_Menu)
        Starting_Menu.setTabOrder(self.start_bt, self.credits_bt)
        Starting_Menu.setTabOrder(self.credits_bt, self.exit_bt)

        # if button clicked, sent to its respective windows

        self.start_bt.clicked.connect(self.menu)
        self.credits_bt.clicked.connect(self.credits)
        self.exit_bt.clicked.connect(Starting_Menu.close)

    def menu(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def credits(self):
        pass


    def retranslateUi(self, Starting_Menu):
        _translate = QtCore.QCoreApplication.translate
        Starting_Menu.setWindowTitle(_translate("Starting_Menu", "Start"))
        self.exit_bt.setShortcut(_translate("Starting_Menu", "Return"))
        self.credits_bt.setShortcut(_translate("Starting_Menu", "Return"))
        self.start_bt.setShortcut(_translate("Starting_Menu", "Return"))


class Ui_Menu(object):
    def setupUi(self, Menu):
        self.form = Menu
        Menu.setObjectName("Menu")
        Menu.resize(1000, 700)
        Menu.setMinimumSize(QtCore.QSize(750, 500))
        Menu.setMaximumSize(QtCore.QSize(1000, 700))
        self.menu_bg_asset = QtWidgets.QLabel(Menu)
        self.menu_bg_asset.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.menu_bg_asset.setMinimumSize(QtCore.QSize(750, 500))
        self.menu_bg_asset.setMaximumSize(QtCore.QSize(1000, 700))
        self.menu_bg_asset.setText("")
        self.menu_bg_asset.setPixmap(QtGui.QPixmap("../Picture Assets/menu_bg.png"))
        self.menu_bg_asset.setScaledContents(True)
        self.menu_bg_asset.setObjectName("menu_bg_asset")
        self.back_bt = QtWidgets.QPushButton(Menu)
        self.back_bt.setGeometry(QtCore.QRect(30, 60, 141, 141))
        self.back_bt.setStyleSheet("QPushButton {border-radius: 70px;}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(125, 73, 229);\n"
"    }")
        self.back_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Picture Assets/back_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_bt.setIcon(icon)
        self.back_bt.setIconSize(QtCore.QSize(150, 165))
        self.back_bt.setFlat(True)
        self.back_bt.setObjectName("back_bt")
        self.challenge_bt = QtWidgets.QPushButton(Menu)
        self.challenge_bt.setGeometry(QtCore.QRect(92, 440, 402, 159))
        self.challenge_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.challenge_bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Picture Assets/challenge_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.challenge_bt.setIcon(icon1)
        self.challenge_bt.setIconSize(QtCore.QSize(400, 350))
        self.challenge_bt.setDefault(True)
        self.challenge_bt.setFlat(False)
        self.challenge_bt.setObjectName("challenge_bt")
        self.custom_bt = QtWidgets.QPushButton(Menu)
        self.custom_bt.setGeometry(QtCore.QRect(508, 440, 402, 159))
        self.custom_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.custom_bt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Picture Assets/custom_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.custom_bt.setIcon(icon2)
        self.custom_bt.setIconSize(QtCore.QSize(400, 350))
        self.custom_bt.setDefault(True)
        self.custom_bt.setFlat(False)
        self.custom_bt.setObjectName("custom_bt")
        self.arith_bt = QtWidgets.QPushButton(Menu)
        self.arith_bt.setGeometry(QtCore.QRect(92, 272, 402, 159))
        self.arith_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.arith_bt.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Picture Assets/arith_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arith_bt.setIcon(icon3)
        self.arith_bt.setIconSize(QtCore.QSize(400, 350))
        self.arith_bt.setDefault(True)
        self.arith_bt.setFlat(False)
        self.arith_bt.setObjectName("arith_bt")
        self.geo_bt = QtWidgets.QPushButton(Menu)
        self.geo_bt.setGeometry(QtCore.QRect(508, 272, 402, 159))
        self.geo_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.geo_bt.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Picture Assets/geo_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geo_bt.setIcon(icon4)
        self.geo_bt.setIconSize(QtCore.QSize(400, 350))
        self.geo_bt.setDefault(True)
        self.geo_bt.setFlat(False)
        self.geo_bt.setObjectName("geo_bt")
        self.audio_bt = QtWidgets.QPushButton(Menu)
        self.audio_bt.setGeometry(QtCore.QRect(820, 60, 151, 151))
        self.audio_bt.setStyleSheet("QPushButton {border-radius: 70px;}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(125, 73, 229);\n"
"    }")
        self.audio_bt.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Picture Assets/audio_on_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_bt.setIcon(icon5)
        self.audio_bt.setIconSize(QtCore.QSize(140, 140))
        self.audio_bt.setFlat(True)
        self.audio_bt.setObjectName("audio_bt")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        # goes back to start
        self.back_bt.clicked.connect(self.start)

        # if button clicked, sent to its respective windows for each gamemodes
        self.arith_bt.clicked.connect(self.arithmetic)
        self.geo_bt.clicked.connect(self.geometric)
        self.challenge_bt.clicked.connect(self.challenge)
        self.custom_bt.clicked.connect(self.custom)

    # the objects here are just basically how the game would work such as how many rounds
    def arithmetic(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("arithmetic", 20, 1, 10, 1, 5,
                               None, None, None, None,
                               None, None, None, None)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def geometric(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("geometric", 5, 1, 10, 1, 5,
                               None,None, None, None,
                               None, None, None, None)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def challenge(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("challenge", 5, 2, 10, 2, 10,
                               15, 6, 15, 6,
                               4, 3, 10, 5)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def custom(self):
        pass

    def start(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Starting_Menu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.back_bt.setShortcut(_translate("Menu", "Esc"))
        self.challenge_bt.setShortcut(_translate("Menu", "Return"))
        self.custom_bt.setShortcut(_translate("Menu", "Return"))
        self.arith_bt.setShortcut(_translate("Menu", "Return"))
        self.geo_bt.setShortcut(_translate("Menu", "Return"))


class Ui_Questions(object):
    def __init__(self, gamemodes, x_high, x_low, y_high, y_low, rounds, nth_terms_arith_high,
                 nth_terms_arith_low, nth_terms_geo_high, nth_terms_geo_low, ratio_high, ratio_low, diff_high, diff_low):
        # Indicator which gamemode would the questions be given to the players
        self.gamemode = gamemodes
        # Values to be used especially on custom mode
        self.round_num = 0
        self.lose = 0
        self.wins = 0
        self.x_high = x_high
        self.x_low = x_low
        self.y_high = y_high
        self.y_low = y_low
        self.custom_and_fixed_rd = rounds
        self.nth_term_arith_high = nth_terms_arith_high
        self.nth_term_arith_low = nth_terms_arith_low
        self.nth_term_geo_high = nth_terms_geo_high
        self.nth_term_geo_low = nth_terms_geo_low
        self.ratio_high = ratio_high
        self.ratio_low = ratio_low
        self.diff_high = diff_high
        self.diff_low = diff_low
        self.list_answer = []
        self.list_correct_answer = []


    # This form will contain all the gamemodes and questions, avoiding redundancy
    # including becoming more concise and clear for developers to read
    def setupUi(self, Questions):
        self.form = Questions
        Questions.setObjectName("Questions")
        Questions.resize(1000, 700)
        Questions.setMinimumSize(QtCore.QSize(750, 500))
        Questions.setMaximumSize(QtCore.QSize(1000, 700))
        Questions.setSizeIncrement(QtCore.QSize(0, 0))

        self.question_bg_asset = QtWidgets.QLabel(Questions)
        self.question_bg_asset.setGeometry(QtCore.QRect(1, 1, 998, 698))
        self.question_bg_asset.setMinimumSize(QtCore.QSize(750, 500))
        self.question_bg_asset.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.question_bg_asset.setFont(font)
        self.question_bg_asset.setText("")
        self.question_bg_asset.setPixmap(QtGui.QPixmap("../Picture Assets/game_bg.png"))
        self.question_bg_asset.setScaledContents(True)
        self.question_bg_asset.setObjectName("question_bg_asset")

        self.answer_user = QtWidgets.QLineEdit(Questions)
        self.answer_user.setGeometry(QtCore.QRect(170, 490, 531, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.answer_user.setFont(font)
        self.answer_user.setFrame(False)
        self.answer_user.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_user.setClearButtonEnabled(True)
        self.answer_user.setObjectName("answer_user")

        self.ans_bt = QtWidgets.QPushButton(Questions)
        self.ans_bt.setGeometry(QtCore.QRect(740, 480, 141, 141))
        self.ans_bt.setStyleSheet("QPushButton {border-radius: 70px;}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(125, 73, 229);\n}")
        self.ans_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Picture Assets/ans_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ans_bt.setIcon(icon)
        self.ans_bt.setIconSize(QtCore.QSize(150, 165))
        self.ans_bt.setFlat(True)
        self.ans_bt.setObjectName("ans_bt")

        self.back_bt = QtWidgets.QPushButton(Questions)
        self.back_bt.setGeometry(QtCore.QRect(70, 300, 101, 101))
        self.back_bt.setStyleSheet("QPushButton {border-radius: 50px;}\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(125, 73, 229);\n}")
        self.back_bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Picture Assets/back_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_bt.setIcon(icon1)
        self.back_bt.setIconSize(QtCore.QSize(100, 100))
        self.back_bt.setFlat(True)
        self.back_bt.setObjectName("back_bt")

        self.number_quest = QtWidgets.QPlainTextEdit(Questions)
        self.number_quest.setGeometry(QtCore.QRect(270, 240, 631, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.number_quest.setFont(font)
        self.number_quest.setTabletTracking(True)
        self.number_quest.setStyleSheet("color: rgb(85, 0, 255);")
        self.number_quest.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.number_quest.setFrameShadow(QtWidgets.QFrame.Plain)
        self.number_quest.setMidLineWidth(0)
        self.number_quest.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.number_quest.setReadOnly(True)
        self.number_quest.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.number_quest.setObjectName("number_quest")

        self.number_quest_2 = QtWidgets.QPlainTextEdit(Questions)
        self.number_quest_2.setGeometry(QtCore.QRect(230, 60, 701, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.number_quest_2.setFont(font)
        self.number_quest_2.setStyleSheet("color: rgb(85, 0, 127);")
        self.number_quest_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.number_quest_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.number_quest_2.setMidLineWidth(0)
        self.number_quest_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.number_quest_2.setReadOnly(True)
        self.number_quest_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.number_quest_2.setObjectName("number_quest_2")

        self.round = QtWidgets.QLineEdit(Questions)
        self.round.setGeometry(QtCore.QRect(50, 120, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.round.setFont(font)
        self.round.setAutoFillBackground(False)
        self.round.setStyleSheet("color: rgb(93, 23, 235);\nbackground-color: rgb(140, 82, 255);")
        self.round.setFrame(False)
        self.round.setAlignment(QtCore.Qt.AlignCenter)
        self.round.setReadOnly(True)
        self.round.setClearButtonEnabled(False)
        self.round.setObjectName("round")

        # Checks what gamemode to play
        self.mode_to_play()
        # Buttons for leaving and giving answers on the game
        self.ans_bt.clicked.connect(self.checker)
        self.back_bt.clicked.connect(self.back)

        self.retranslateUi(Questions)
        QtCore.QMetaObject.connectSlotsByName(Questions)

    def mode_to_play(self):
        # Outputs the round everytime it goes back here
        self.round_num += 1
        self.round.setText(str(self.round_num))
        # Used for deciding what gamemode to play based from the user
        if self.gamemode == "arithmetic":
            self.arithmetic()
        elif self.gamemode == "geometric":
            self.geometric()
        elif self.gamemode == "challenge":
            self.challenge()
        elif self.gamemode == "custom":
            self.custom()
        else:
            print("Invalid gamemode")

    def arithmetic(self):
        # randomizer for selecting values and placement of it
        self.placement = ["1st", "2nd", "3rd", "4th"]
        self.game_placement = random.choice(self.placement)
        try:
            adder = random.randint(self.x_low, self.x_high)
            self.x_1 = random.randint(self.y_low, self.y_high)
            self.x_2 = self.x_1 + adder
            self.x_3 = self.x_2 + adder
            self.x_4 = self.x_3 + adder

            # Just generates the question for players to answer
            if self.game_placement == "1st":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"?, {self.x_2}, {self.x_3}, {self.x_4}")

            elif self.game_placement == "2nd":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, ?, {self.x_3}, {self.x_4}")

            elif self.game_placement == "3rd":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, {self.x_2}, ?, {self.x_4}")

            elif self.game_placement == "4th":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, {self.x_2}, {self.x_3}, ?")

        except ValueError:
            pass

    def geometric(self):
        # Same technique above
        self.placement = ["1st", "2nd", "3rd", "4th"]
        self.game_placement = random.choice(self.placement)
        try:
            multiplier = random.randint(self.x_low, self.x_high)
            self.x_1 = random.randint(self.y_low, self.y_high)
            self.x_2 = self.x_1 * multiplier
            self.x_3 = self.x_2 * multiplier
            self.x_4 = self.x_3 * multiplier

            if self.game_placement == "1st":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"?, {self.x_2}, {self.x_3}, {self.x_4}")

            elif self.game_placement == "2nd":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, ?, {self.x_3}, {self.x_4}")

            elif self.game_placement == "3rd":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, {self.x_2}, ?, {self.x_4}")

            elif self.game_placement == "4th":
                self.number_quest_2.setPlainText(f"What is the {self.game_placement} term of the following sequence?")
                self.number_quest.setPlainText(f"{self.x_1}, {self.x_2}, {self.x_3}, ?")

        except ValueError:
            pass

    def permutation_guessr(self):
        try:
            self.first_term = random.randint(self.x_low, self.x_high)
            self.difference = random.randint(self.diff_low, self.diff_high)
            self.nth_term = random.randint(self.nth_term_arith_low, self.nth_term_arith_high)
            self.sequence = [self.first_term + (i * self.difference) for i in range(4)]
            self.equation = self.first_term + ((self.nth_term - 1) * self.difference)
            self.number_prefix_question()

        except ValueError:
            info = "Please, input a number for the following questions"
            QtWidgets.QMessageBox.information(None, "Information", info)

    def geometric_guessr(self):
        try:
            self.first_term = random.randint(self.x_low, self.x_high)
            self.ratio = random.randint(self.ratio_low, self.ratio_high)
            self.nth_term = random.randint(self.nth_term_geo_low, self.nth_term_geo_high)
            self.sequence = [self.first_term * (self.ratio ** i) for i in range(4)]
            self.equation = self.first_term * (self.ratio ** (self.nth_term - 1))
            self.number_prefix_question()

        except ValueError:
            info = "Please, input a number for the following questions"
            QtWidgets.QMessageBox.information(None, "Information", info)

    def number_prefix_question(self):
        # Determine the suffix for the nth term
        suffix = "th"
        if 10 <= self.nth_term % 100 <= 20:
            suffix = "th"
        else:
            if self.nth_term % 10 == 1:
                suffix = "st"
            elif self.nth_term % 10 == 2:
                suffix = "nd"
            elif self.nth_term % 10 == 3:
                suffix = "rd"

        self.number_quest_2.setPlainText(f"What is the {self.nth_term}{suffix} number of the following sequence:")
        self.number_quest.setPlainText(", ".join(map(str, self.sequence)))

    def challenge(self):
        # Used for randomizing gamemodes on which to play when playing challenge mode with an additional
        # two gamemodes for the "challenge"
        self.randomizer_list = [self.arithmetic, self.geometric, self.permutation_guessr, self.geometric_guessr]
        self.randomizer = random.choice(self.randomizer_list)

        if self.randomizer == self.arithmetic:
            self.arithmetic()
        elif self.randomizer == self.geometric:
            self.geometric()
        elif self.randomizer == self.permutation_guessr:
            self.permutation_guessr()
        elif self.randomizer == self.geometric_guessr:
            self.geometric_guessr()
        elif self.round_num > 5:
            self.result()

    def custom(self):
        pass

    def geometric_checker(self):
        try:
            # Functions the same as the other one with the arithmetic of checking whether it would be correct or not
            self.input_ans = int(self.answer_user.text())
            if self.game_placement == "1st" and self.input_ans == self.x_1:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "2nd" and self.input_ans == self.x_2:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "3rd" and self.input_ans == self.x_3:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "4th" and self.input_ans == self.x_4:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            else:
                self.lose_points_placement()
                if not self.lose > 2:
                    self.mode_to_play()
                else:
                    self.result()
        except ValueError:
            info = ("Please, input a number for the following questions")
            QtWidgets.QMessageBox.information(None, "Information", info)

    def arithmetic_checker(self):
        # for checking arithmetic operations
        try:
            self.input_ans = int(self.answer_user.text())
            if self.game_placement == "1st" and self.input_ans == self.x_1:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "2nd" and self.input_ans == self.x_2:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "3rd" and self.input_ans == self.x_3:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            elif self.game_placement == "4th" and self.input_ans == self.x_4:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            else:
                self.lose_points_placement()
                if not self.lose > 2:
                    self.mode_to_play()
                else:
                    self.result()
        except ValueError:
            info = ("Please, input a number for the following questions")
            QtWidgets.QMessageBox.information(None, "Information", info)

    def permutation_checker(self):
        try:
            self.input_ans = int(self.answer_user.text())
            if self.input_ans == self.equation:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            else:
                self.lose_points()
                if not self.lose > 2:
                    self.mode_to_play()
                else:
                    self.result()
        except ValueError:
            info = ("Please, input a number for the following questions")
            QtWidgets.QMessageBox.information(None, "Information", info)

    def geometric_guessr_checker(self):
        try:
            self.input_ans = int(self.answer_user.text())
            if self.input_ans == self.equation:
                self.win_points()
                if self.round_num < self.custom_and_fixed_rd:
                    self.mode_to_play()
                else:
                    self.result()
            else:
                self.lose_points()
                if not self.lose > 2:
                    self.mode_to_play()
                else:
                    self.result()
        except ValueError:
            info = ("Please, input a number for the following questions")
            QtWidgets.QMessageBox.information(None, "Information", info)

    def lose_points_placement(self):
        # for guessing the numbers on the placement

        # This lines of string will be responsible for the loop of the game
        # clearing all the texts and answers for the corresponding rounds

        self.lose += 1
        self.number_quest.clear()
        self.number_quest_2.clear()
        self.answer_user.clear()
        self.list_answer.append(self.input_ans)
        # List used for reviewing answers
        if self.game_placement == "1st":
            self.list_correct_answer.append(str(self.x_1))
        elif self.game_placement == "2nd":
            self.list_correct_answer.append(str(self.x_2))
        elif self.game_placement == "3rd":
            self.list_correct_answer.append(str(self.x_3))
        elif self.game_placement == "4th":
            self.list_correct_answer.append(str(self.x_4))

    def win_points(self):
        self.wins += 1
        self.number_quest.clear()
        self.number_quest_2.clear()
        self.answer_user.clear()
        self.list_answer.append(self.input_ans)
        self.list_correct_answer.append("Correct")

    def lose_points(self):
        self.lose += 1
        self.number_quest.clear()
        self.number_quest_2.clear()
        self.answer_user.clear()
        self.list_answer.append(self.input_ans)
        self.list_correct_answer.append(str(self.equation))

    def checker(self):
        # This will be the one responsible for checking all the user's answer
        # It includes all gamemodes, though will go to another method if challenge or custom
        if self.gamemode == "arithmetic":
            self.arithmetic_checker()
        elif self.gamemode == "geometric":
            self.geometric_checker()
        elif self.gamemode == "challenge":
            # nested if statements for checking whether the user is correct or nah based from the gamemode the
            # player is playing
            if self.randomizer == self.arithmetic:
                self.arithmetic_checker()
            elif self.randomizer == self.geometric:
                self.geometric_checker()
            elif self.randomizer == self.permutation_guessr:
                self.permutation_checker()
            elif self.randomizer == self.geometric_guessr:
                self.geometric_guessr_checker()
        elif self.gamemode == "custom":
            pass

    def audio_play(self):
        pass

    def result(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_after_result(self.wins, self.gamemode, self.round_num)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()
        print(self.list_correct_answer)
        print(self.list_answer)

    def back(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def retranslateUi(self, Questions):
        _translate = QtCore.QCoreApplication.translate
        Questions.setWindowTitle(_translate("Questions", "Question"))
        self.answer_user.setPlaceholderText(_translate("Questions", "Your Answer Here"))
        self.ans_bt.setShortcut(_translate("Questions", "Return"))
        self.back_bt.setShortcut(_translate("Questions", "Esc"))
        self.number_quest.setPlaceholderText(_translate("Questions", "Placeholder"))
        self.number_quest_2.setPlaceholderText(_translate("Questions", "Placeholder"))
        self.round.setPlaceholderText(_translate("Questions", "10"))


class Ui_after_result(object):
    def __init__(self, score, gamemode, round):
        self.score = score
        self.rounds = round
        self.gamemode = gamemode

    def setupUi(self, after_result):
        self.form = after_result
        after_result.setObjectName("after_result")
        after_result.resize(1000, 700)
        after_result.setMinimumSize(QtCore.QSize(750, 500))
        after_result.setMaximumSize(QtCore.QSize(1000, 700))
        after_result.setSizeIncrement(QtCore.QSize(0, 0))
        self.result_bg = QtWidgets.QLabel(after_result)
        self.result_bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.result_bg.setMinimumSize(QtCore.QSize(750, 500))
        self.result_bg.setMaximumSize(QtCore.QSize(1000, 700))
        self.result_bg.setText("")
        self.result_bg.setPixmap(QtGui.QPixmap("../Picture Assets/after_game_bg.png"))
        self.result_bg.setScaledContents(True)
        self.result_bg.setObjectName("result_bg")
        self.back_bt = QtWidgets.QPushButton(after_result)
        self.back_bt.setGeometry(QtCore.QRect(40, 60, 141, 141))
        self.back_bt.setStyleSheet("QPushButton {border-radius: 70px;}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(125, 73, 229);\n"
"    }")
        self.back_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Picture Assets/back_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_bt.setIcon(icon)
        self.back_bt.setIconSize(QtCore.QSize(150, 165))
        self.back_bt.setFlat(True)
        self.back_bt.setObjectName("back_bt")
        self.audio_bt = QtWidgets.QPushButton(after_result)
        self.audio_bt.setGeometry(QtCore.QRect(810, 50, 151, 151))
        self.audio_bt.setStyleSheet("QPushButton {border-radius: 70px;}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(125, 73, 229);\n"
"    }")
        self.audio_bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Picture Assets/audio_on_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio_bt.setIcon(icon1)
        self.audio_bt.setIconSize(QtCore.QSize(140, 140))
        self.audio_bt.setFlat(True)
        self.audio_bt.setObjectName("audio_bt")
        self.play_again_bt = QtWidgets.QPushButton(after_result)
        self.play_again_bt.setGeometry(QtCore.QRect(80, 490, 402, 159))
        self.play_again_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.play_again_bt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Picture Assets/pg_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_again_bt.setIcon(icon2)
        self.play_again_bt.setIconSize(QtCore.QSize(400, 350))
        self.play_again_bt.setDefault(True)
        self.play_again_bt.setFlat(False)
        self.play_again_bt.setObjectName("play_again_bt")
        self.review_bt = QtWidgets.QPushButton(after_result)
        self.review_bt.setGeometry(QtCore.QRect(520, 490, 402, 159))
        self.review_bt.setStyleSheet("QPushButton {border-radius: 20px;}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(198, 53, 104);\n"
"    }")
        self.review_bt.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Picture Assets/review_bt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.review_bt.setIcon(icon3)
        self.review_bt.setIconSize(QtCore.QSize(400, 350))
        self.review_bt.setDefault(True)
        self.review_bt.setFlat(False)
        self.review_bt.setObjectName("review_bt")
        self.round = QtWidgets.QLineEdit(after_result)
        self.round.setGeometry(QtCore.QRect(320, 220, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.round.setFont(font)
        self.round.setAutoFillBackground(False)
        self.round.setStyleSheet("color: rgb(85, 0, 255);")
        self.round.setFrame(False)
        self.round.setAlignment(QtCore.Qt.AlignCenter)
        self.round.setReadOnly(True)
        self.round.setClearButtonEnabled(False)
        self.round.setObjectName("round")
        self.label = QtWidgets.QLabel(after_result)
        self.label.setGeometry(QtCore.QRect(140, 380, 701, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(198, 125, 240);\n"
"color: rgb(128, 75, 234);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.back_bt.clicked.connect(self.back)
        # When pressed play_again, this method will be called on what gamemode
        # was played earlier, avoiding any hassle lol
        self.play_again_bt.clicked.connect(self.play_it_again)
        # Here, it displays the score of the users, and also their rating lol
        self.score_display()

        self.retranslateUi(after_result)
        QtCore.QMetaObject.connectSlotsByName(after_result)

    def back(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def score_display(self):
        self.round.setText(str(self.score))
        # Used for displaying texts regarding the users' performance towards the game
        try:
            self.performance = (self.score / self.rounds) * 100
            if self.performance <= 25.00:
                self.label.setText("You need more practice and review")
            elif self.performance <= 50.00:
                self.label.setText("Satisfactory but still needs improvement")
            elif self.performance <= 75.00:
                self.label.setText("Great job! Keep the good work!")
            elif self.performance <= 100:
                self.label.setText("Wow, that's awsome! Keep up the great work!")
        except ValueError:
            print("error")

    def play_it_again(self):
        if self.gamemode == "arithmetic":
            self.arithmetic()
        elif self.gamemode == "geometric":
            self.geometric()
        elif self.gamemode == "challenge":
            self.challenge()
        elif self.gamemode == "custom":
            self.custom()

    def arithmetic(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("arithmetic", 20, 1, 10, 1, 5,
                               None, None, None, None,
                               None, None, None, None)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def geometric(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("geometric", 5, 1, 10, 1, 5,
                               None, None, None, None,
                               None, None, None, None)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def challenge(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Questions("challenge", 5, 1, 10, 1, 10,
                               20, 1, 5, 2,
                               5, 2, 10, 5)
        self.ui.setupUi(self.window)
        self.window.show()
        self.form.close()

    def custom(self):
        pass

    def retranslateUi(self, after_result):
        _translate = QtCore.QCoreApplication.translate
        after_result.setWindowTitle(_translate("after_result", "After_game"))
        self.back_bt.setShortcut(_translate("after_result", "Esc"))
        self.play_again_bt.setShortcut(_translate("after_result", "Return"))
        self.review_bt.setShortcut(_translate("after_result", "Return"))
        self.round.setPlaceholderText(_translate("after_result", "10"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Starting_Menu = QtWidgets.QWidget()
    ui = Ui_Starting_Menu()
    ui.setupUi(Starting_Menu)
    Starting_Menu.show()
    sys.exit(app.exec_())
