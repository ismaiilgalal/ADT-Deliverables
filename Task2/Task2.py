import sys
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QComboBox

app = QApplication([])

window = QWidget()
window.setWindowTitle("Task 2")
window.setGeometry(100, 50, 1750, 900)
window.setFixedSize(1750, 900)
# window.setMaximumWidth(1700)
# # window.setMaximumHeight(900)
# window.setMinimumWidth(1500)
# window.setMinimumHeight(900)

serifFont = QFont("Times", 12, QFont.Bold)

functionlabel = QLabel(window)
functionlabel.setText("Please Select The Transistor You Want Highlighted")
functionlabel.setFont(serifFont)
functionlabel.move(640, 30)

transistorlist = QComboBox(window)
transistorlist.move(800, 70)
transistorlist.addItem("None")
transistorlist.addItem("M1")
transistorlist.addItem("M2")
transistorlist.addItem("M3")
transistorlist.addItem("M4")
transistorlist.addItem("M5")
transistorlist.addItem("M6")

lbl = QLabel(window)
lbl.setGeometry(100, 120, 1536, 761)


def showimage():
    # lbl.clear()
    selectedtran = transistorlist.currentText()
    selectedtran = selectedtran + '.png'
    image = QtGui.QImage(selectedtran)
    pixmap = QtGui.QPixmap(image)
    lbl.setPixmap(pixmap.scaled(lbl.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))


while 1:
    if transistorlist.currentText() == 'None.png':
        lbl.clear()
        image = QtGui.QImage('None.png')
        pixmap = QtGui.QPixmap(image)
        lbl.setPixmap(pixmap.scaled(lbl.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        window.show()
        app.exec_()
    elif transistorlist.currentIndexChanged != -1:
        lbl.clear()
        transistorlist.currentIndexChanged.connect(showimage())
        window.show()
        app.exec_()
    else:
        break

# window.show()
# app.exec_()

# window.show()
# app.exec_()

# while(1):
#     selectedtran = transistorlist.currentText()
#     selectedtran = selectedtran + '.png'
#     image = QtGui.QImage(selectedtran)
#     pixmap = QtGui.QPixmap(image)
#     lbl.setPixmap(pixmap.scaled(lbl.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
#     window.show()
#     app.exec_()
# if transistorlist.activated['None'] == True:
#     image = QtGui.QImage('None.png')
#     pixmap = QtGui.QPixmap(image)
#     lbl.setPixmap(pixmap.scaled(lbl.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
