#V1 : Plain response

from PySide6.QtWidgets import QApplication, QPushButton

#The slot (like a controller function)

def button_clicked(data): #Because the clicked signal sends the parameter
    print("You clicked the button! checked : ", data)

app = QApplication()
button = QPushButton("Push me!")
button.setCheckable(True) #Checkable button now

button.clicked.connect(button_clicked)
# Clicked is like a button action, onClick and connect tells what to do after click

button.show()
app.exec()