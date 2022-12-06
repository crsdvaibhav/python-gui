#V3 : Slider

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot (like a controller function)

def respond_to_slider(data): #Because the clicked signal sends the parameter
    print("Slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)

slider.show()
app.exec()