#V1 : Plain response

from PySide6.QtWidgets import QApplication, QPushButton

#The slot (like a controller function)
def button_clicked():
    print("You clicked the button!")

app = QApplication()
button = QPushButton("Push me!")

button.clicked.connect(button_clicked)
# Clicked is like a button action, onClick and connect tells what to do after click

button.show()
app.exec()