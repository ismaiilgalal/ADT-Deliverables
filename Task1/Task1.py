from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPlainTextEdit, QDoubleSpinBox, QPushButton, QMessageBox
from PySide2.QtGui import QIcon

import re
import numpy as np
import matplotlib.pyplot as plt

app = QApplication([])
window = QWidget()
window.setWindowTitle("Equation Plotter")
window.setGeometry(400, 400, 700, 600)
window.setMaximumWidth(700)
window.setMaximumHeight(600)


formatlabel = QLabel(window)
formatlabel.setText("Please Enter the Polynomial in the following format: \n                        a*x^2-b/x-c ")
formatlabel.move(220, 40)

equationlabel = QLabel(window)
equationlabel.setText("Enter Polynomial Equation:")
equationlabel.move(0, 105)

equationinput = QPlainTextEdit(window)
equationinput.setGeometry(170, 100, 400, 30)

# equationbutton = QPushButton("Set Equation",window)
# equationbutton.setGeometry(575,100,100,30)

#### Minimum #########
minlabel = QLabel(window)
minlabel.setText("Enter Minimum Value for x:")
minlabel.move(0, 205)

# mininput = QPlainTextEdit(window)
# mininput.setGeometry(170,200,400,30)
mininput = QDoubleSpinBox(window)
mininput.setGeometry(170, 200, 60, 30)

# minbutton = QPushButton("Set Minimum",window)
# minbutton.setGeometry(575,200,100,30)


######### Maximum ###########
maxlabel = QLabel(window)
maxlabel.setText("Enter Maximum Value for x:")
maxlabel.move(0, 305)

# maxinput = QPlainTextEdit(window)
# maxinput.setGeometry(170,300,400,30)
maxinput = QDoubleSpinBox(window)
maxinput.setGeometry(170, 300, 60, 30)

# maxbutton = QPushButton("Set Maximum",window)
# maxbutton.setGeometry(575,300,100,30)

########## Step ############

steplabel = QLabel(window)
steplabel.setText("Enter Step for Function Plot:")
steplabel.move(0, 405)

# stepinput = QPlainTextEdit(window)
# stepinput.setGeometry(170,400,400,30)
stepinput = QDoubleSpinBox(window)
stepinput.setGeometry(170, 400, 60, 30)

# stepbutton = QPushButton("Set Step", window)
# stepbutton.setGeometry(575,400,100,30)

def plotfunction(xvar, yvar):
    plt.plot(xvar, yvar)
    plt.show()
    # return (0)

plotbutton = QPushButton("Plot", window)
plotbutton.setGeometry(250, 500, 100, 30)

quitbutton = QPushButton("Quit", window)
quitbutton.setGeometry(350, 500, 100, 30)
quitbutton.clicked.connect(quit)

window.show()
app.exec_()

####################################### EQUATION PLOTTER #############
count = 0
count2 = 0
coeffs = list()
degrees = list()
ylist = list()

# equation = input('Enter polynomial function:')
# equation = '3*x^2-2*x+10'
equation = equationinput.toPlainText()
print('equation is', equation)

# def getvalue(variablename, boxname):
# variablename = boxname.value()
# return (0)

# min = input ("Enter minimum value for x:")
# min = float(min)
# min = 0
# minbutton.clicked.connect(getvalue(min,mininput))
# minbutton.clicked.connect()
min = mininput.value()
print("minimum value is", min)

# max = input ("Enter maximum value for x:")
# max = float(max)
# max = 9
max = maxinput.value()
print("maximum value is", max)

# step = input ("Enter step for function:")
# step = float(step)
# step = 1
step = stepinput.value()
print("step value is", step)


def createList(min, max):
    return np.arange(min, max + step, step)




x = createList(min, max)
print('x is:', x)

try:
    parced = re.split('([-+])', equation)
    print('Parced items:', parced)
    if parced[0] == '':
        parced.remove(parced[0])

    for item in parced:
        # print("i is:", i)
        # print("parced item:", parced[i])
        # if item == '':
        #     parced.remove(item)
        #     if parced:
        #         parced.remove('-')
        #         parced[count] = '-' + parced[count]
        #         count = count + 1
        #     count += 1
        if item.find('-') != -1:
            parced.remove('-')
            parced[count] = '-' + parced[count]
            count = count + 1
        elif item.find('+') != -1:
            parced.remove('+')
            count = count + 1
        else:
            count += 1

    for item in parced:
        terms = re.split('([*/])', item)
        print("terms:", terms)
        coeffs.append(terms[0])
        try:
            if terms[1] == '/':
                if terms[2][2:] == '':
                    degrees.append('-1')
                else:
                    degrees.append('-' + terms[2][2:])
            elif terms[1] == '*':
                if terms[2][2:] == '':
                    degrees.append('1')
                else:
                    degrees.append(terms[2][2:])
        except:
            degrees.append('0')

    for i in range(len(coeffs)):
        coeffs[i] = int(coeffs[i])
        degrees[i] = int(degrees[i])

    for i in range(len(x)):
        y = 0
        for j in range(len(coeffs)):
            temp = coeffs[j] * x[i] ** degrees[j]
            y += temp
        ylist.append(y)

    print('ylist is:', ylist)
    print('Coefficients:', coeffs)
    print('Degrees:', degrees)
    plotbutton.clicked.connect(plotfunction(x,ylist))
    # plotbutton.clicked.connect(quit)
    # plotbutton.clicked.connect(quit)
    # plotbutton.clicked.disconnect()
    #plotbutton.clicked.connect(quit)
    # plt.plot(x,ylist)
    # plt.show()

# print("couldn't plot")
except:
    errormessage = QMessageBox()
    errormessage.setIcon(QMessageBox.Critical)
    errormessage.setWindowTitle("Plot Error")
    errormessage.setText("Function can't be plotted")
    errormessage.setInformativeText("Please enter the equation the correct format and try again.")
    errormessage.exec()

# plotbutton.clicked.connect(print("plotbutton clicked"))
# plotbutton.clicked.connect(plt.plot(x,ylist))
# plotbutton.clicked.connect(plt.show())
# plotbutton.clicked.connect(quit)
