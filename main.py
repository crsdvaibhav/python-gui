#V3 : In classes and seperate files 

from PySide6.QtWidgets import QApplication
import sys #command line options
from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()

