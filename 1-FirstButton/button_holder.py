from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):

    #Constructor function, self is a window object as it inherits from QMainWindow
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder app!")
        button = QPushButton("Push me!")

        #Setting the button as central widget

        self.setCentralWidget(button)