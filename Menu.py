# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
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
        font.setPointSize(18)
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

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "Patter Sequence Game!"))
        self.Submit_2.setText(_translate("Menu", "Play"))
        self.Exit.setText(_translate("Menu", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
