from PyQt5.QtWidgets import QApplication, QMainWindow

from Assignment_PyQT5 import *

app = QApplication([])

w = QMainWindow()
w.setWindowTitle('SoundsFine Music Application')

ex = Ui_MainWindow()
ex.setupUi(w)

w.setGeometry(350, 140, 800, 740)
w.show()

app.exec_()
