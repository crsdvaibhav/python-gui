#V2 : In classes but still in single file

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys #command line options

class ButtonHolder(QMainWindow):

    #Constructor function, self is a window object as it inherits from QMainWindow
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder app!")
        button = QPushButton("Push me!")

        #Setting the button as central widget

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()

