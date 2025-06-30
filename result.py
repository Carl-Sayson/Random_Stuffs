import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a list using a for loop
        my_list = []
        for i in range(1, 11):
            my_list.append(f"Item {i}")

        # Convert the list to a bulleted string using HTML
        list_str = "<ul>"  # Start of unordered list
        for item in my_list:
            list_str += f"<li>{item}</li>"  # Each item is a list item
        # list_str += "</ul>"  # End of unordered list

        # Create a QLabel and set the list as its text
        self.label = QLabel(list_str)

        # # Enable rich text to interpret HTML
        # self.label.setTextFormat(Qt.RichText)

        # Layout to hold the label
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Set the layout for the window
        self.setLayout(layout)
        self.setWindowTitle("Bulleted List in QLabel")

# Run the application
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())