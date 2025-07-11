# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
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
        self.Left_up_mid.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_up_mid.setText("")
        self.Left_up_mid.setObjectName("Left_up_mid")
        self.gridLayout.addWidget(self.Left_up_mid, 0, 1, 1, 1)
        self.Left_up = QtWidgets.QPushButton(Game)
        self.Left_up.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_up.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_up.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_up.setText("")
        self.Left_up.setObjectName("Left_up")
        self.gridLayout.addWidget(self.Left_up, 0, 0, 1, 1)
        self.right_mid_1 = QtWidgets.QPushButton(Game)
        self.right_mid_1.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_1.setMaximumSize(QtCore.QSize(70, 70))
        self.right_mid_1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_mid_1.setText("")
        self.right_mid_1.setObjectName("right_mid_1")
        self.gridLayout.addWidget(self.right_mid_1, 1, 3, 1, 1)
        self.Right_mid_mid_down = QtWidgets.QPushButton(Game)
        self.Right_mid_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Right_mid_mid_down.setMaximumSize(QtCore.QSize(70, 70))
        self.Right_mid_mid_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Right_mid_mid_down.setText("")
        self.Right_mid_mid_down.setObjectName("Right_mid_mid_down")
        self.gridLayout.addWidget(self.Right_mid_mid_down, 2, 2, 1, 1)
        self.Left_mid_2 = QtWidgets.QPushButton(Game)
        self.Left_mid_2.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_2.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_mid_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_mid_2.setText("")
        self.Left_mid_2.setObjectName("Left_mid_2")
        self.gridLayout.addWidget(self.Left_mid_2, 2, 0, 1, 1)
        self.Left_mid_mid_down = QtWidgets.QPushButton(Game)
        self.Left_mid_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_down.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_mid_mid_down.setText("")
        self.Left_mid_mid_down.setObjectName("Left_mid_mid_down")
        self.gridLayout.addWidget(self.Left_mid_mid_down, 2, 1, 1, 1)
        self.Left_down = QtWidgets.QPushButton(Game)
        self.Left_down.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_down.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_down.setText("")
        self.Left_down.setObjectName("Left_down")
        self.gridLayout.addWidget(self.Left_down, 3, 0, 1, 1)
        self.right_mid_mid_up = QtWidgets.QPushButton(Game)
        self.right_mid_mid_up.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_mid_up.setMaximumSize(QtCore.QSize(70, 70))
        self.right_mid_mid_up.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_mid_mid_up.setText("")
        self.right_mid_mid_up.setObjectName("right_mid_mid_up")
        self.gridLayout.addWidget(self.right_mid_mid_up, 1, 2, 1, 1)
        self.Left_mid_1 = QtWidgets.QPushButton(Game)
        self.Left_mid_1.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_1.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_mid_1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_mid_1.setText("")
        self.Left_mid_1.setObjectName("Left_mid_1")
        self.gridLayout.addWidget(self.Left_mid_1, 1, 0, 1, 1)
        self.right_up = QtWidgets.QPushButton(Game)
        self.right_up.setMinimumSize(QtCore.QSize(70, 70))
        self.right_up.setMaximumSize(QtCore.QSize(70, 70))
        self.right_up.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_up.setText("")
        self.right_up.setAutoDefault(False)
        self.right_up.setFlat(False)
        self.right_up.setObjectName("right_up")
        self.gridLayout.addWidget(self.right_up, 0, 3, 1, 1)
        self.right_mid_2 = QtWidgets.QPushButton(Game)
        self.right_mid_2.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_2.setMaximumSize(QtCore.QSize(70, 70))
        self.right_mid_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_mid_2.setText("")
        self.right_mid_2.setObjectName("right_mid_2")
        self.gridLayout.addWidget(self.right_mid_2, 2, 3, 1, 1)
        self.right_down = QtWidgets.QPushButton(Game)
        self.right_down.setMinimumSize(QtCore.QSize(70, 70))
        self.right_down.setMaximumSize(QtCore.QSize(70, 70))
        self.right_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_down.setText("")
        self.right_down.setObjectName("right_down")
        self.gridLayout.addWidget(self.right_down, 3, 3, 1, 1)
        self.left_mid_down = QtWidgets.QPushButton(Game)
        self.left_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.left_mid_down.setMaximumSize(QtCore.QSize(70, 70))
        self.left_mid_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.left_mid_down.setText("")
        self.left_mid_down.setObjectName("left_mid_down")
        self.gridLayout.addWidget(self.left_mid_down, 3, 1, 1, 1)
        self.right_mid_down = QtWidgets.QPushButton(Game)
        self.right_mid_down.setMinimumSize(QtCore.QSize(70, 70))
        self.right_mid_down.setMaximumSize(QtCore.QSize(70, 70))
        self.right_mid_down.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.right_mid_down.setText("")
        self.right_mid_down.setObjectName("right_mid_down")
        self.gridLayout.addWidget(self.right_mid_down, 3, 2, 1, 1)
        self.Left_mid_mid_up = QtWidgets.QPushButton(Game)
        self.Left_mid_mid_up.setMinimumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_up.setMaximumSize(QtCore.QSize(70, 70))
        self.Left_mid_mid_up.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Left_mid_mid_up.setText("")
        self.Left_mid_mid_up.setObjectName("Left_mid_mid_up")
        self.gridLayout.addWidget(self.Left_mid_mid_up, 1, 1, 1, 1)
        self.right_up_mid = QtWidgets.QPushButton(Game)
        self.right_up_mid.setMinimumSize(QtCore.QSize(70, 70))
        self.right_up_mid.setMaximumSize(QtCore.QSize(70, 70))
        self.right_up_mid.setStyleSheet("background-color: rgb(85, 170, 255);")
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

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Pattern Sequence"))
        self.Exit.setText(_translate("Game", "<---"))
        self.Current_Score.setText(_translate("Game", "Score:"))
        self.Submit.setText(_translate("Game", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QWidget()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
