#V1 : Everything in global scope

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys #command line options

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow app!")

button = QPushButton()
button.selfText("Push me!")

window.setCentralWidget(button)

window.show()
app.exec() #Start the event loop (responsible for reactivity)


