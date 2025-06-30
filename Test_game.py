# import sys
# import random
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# from PyQt5.QtCore import QTimer, Qt
#
# class PatternGame(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Pattern Game")
#         self.setGeometry(100, 100, 300, 200)
#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)
#
#         # Initialize buttons (example setup, adjust as necessary)
#         self.Left_up = QPushButton("Left_up")
#         self.Left_up_mid = QPushButton("Left_up_mid")
#         self.left_mid_down = QPushButton("left_mid_down")
#         self.Left_down = QPushButton("Left_down")
#         self.Left_mid_mid_up = QPushButton("Left_mid_mid_up")
#         self.Left_mid_1 = QPushButton("Left_mid_1")
#         self.Left_mid_2 = QPushButton("Left_mid_2")
#         self.Left_mid_mid_down = QPushButton("Left_mid_mid_down")
#         self.right_mid_mid_up = QPushButton("right_mid_mid_up")
#         self.right_mid_1 = QPushButton("right_mid_1")
#         self.right_mid_2 = QPushButton("right_mid_2")
#         self.Right_mid_mid_down = QPushButton("Right_mid_mid_down")
#         self.right_mid_down = QPushButton("right_mid_down")
#         self.right_up = QPushButton("right_up")
#         self.right_down = QPushButton("right_down")
#         self.right_up_mid = QPushButton("right_up_mid")
#
#         buttons = [
#             self.Left_up, self.Left_up_mid, self.left_mid_down, self.Left_down,
#             self.Left_mid_mid_up, self.Left_mid_1, self.Left_mid_2, self.Left_mid_mid_down,
#             self.right_mid_mid_up, self.right_mid_1, self.right_mid_2, self.Right_mid_mid_down,
#             self.right_mid_down, self.right_up, self.right_down, self.right_up_mid
#         ]
#
#         for button in buttons:
#             self.layout.addWidget(button)
#
#         # Set up the timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.pattern_game)
#         self.timer.start(2000)  # 2 seconds interval
#
#         self.sequences_game = []
#
#     def pattern_game(self):
#         self.choices_list = [
#             self.Left_up, self.Left_up_mid, self.left_mid_down, self.Left_down,
#             self.Left_mid_mid_up, self.Left_mid_1, self.Left_mid_2, self.Left_mid_mid_down,
#             self.right_mid_mid_up, self.right_mid_1, self.right_mid_2, self.Right_mid_mid_down,
#             self.right_mid_down, self.right_up, self.right_down, self.right_up_mid
#         ]
#
#         self.randomizer = random.choice(self.choices_list)
#
#         # Reset previous button's color if any
#         for button in self.choices_list:
#             button.setStyleSheet('background-color: rgb(85, 170, 255);')
#
#         # Change the selected button's color
#         self.randomizer.setStyleSheet('background-color: blue;')
#         self.sequences_game.append(self.randomizer.text())
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PatternGame()
#     window.show()
#     sys.exit(app.exec_())

x = eval(5)
print(x)
