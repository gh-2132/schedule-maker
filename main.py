import sys
from PyQt5.QtWidgets import QApplication

class MainWindow(QApplication):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 500)
        self.initUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())