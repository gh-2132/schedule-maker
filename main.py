import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        self.setGeometry(0, 0, 1000, 700)
        self.initUI()

    def initUI(self):
        # Create the calendar
        calendar = QCalendarWidget(self)
        calendar.setGeometry(0, 0, 1000, 600)

        # Create the text at the bottom
        dateLabel = QLabel(self)
        dateLabel.setGeometry(0, 650, 1000, 50)
        dateLabel.setText("A")
        dateLabel.setFont(QFont('Arial', 20))

        date_button = QPushButton(self)
        date_button.setText("Get the date")
        date_button.setGeometry(0, 600, 100, 50)
        date_button.clicked.connect(self.getCurrentDate)

    def getCurrentDate(self):
        # Display the date
        date = QDate.currentDate()
        print(date.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())