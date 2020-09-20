####### SCHEMDRAW IMPORTS ################
import schemdraw
import schemdraw.elements as elm
from schemdraw import Segment, SegmentArrow, SegmentCircle



############### GUI IMPORTS #################
import sys
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QComboBox


###### SCHEMATIC DRAWING ##########
fclen = 2
platedis = 0.5


class pmos(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ###SOURCE
        self.segments.append(Segment([[0, fclen / 16], [0, 0]]))
        self.segments.append(SegmentArrow([0, 0], [fclen / 8, 0], headwidth=0.1, headlength=0.1))

        ###DRAIN
        self.segments.append(Segment([[0, -platedis], [fclen / 8, -platedis]]))
        self.segments.append(Segment([[0, - (platedis + fclen / 16)], [0, -platedis]]))

        #GATE
        self.segments.append(Segment([[fclen / 8, fclen / 16], [fclen / 8, - (platedis + fclen / 16)]]))
        self.segments.append(Segment([[fclen / 8 + 0.06, 0], [fclen / 8 + 0.06, -platedis]]))
        self.segments.append(Segment([[fclen / 8 + 0.06, -platedis / 2], [fclen / 8 + 0.2, -platedis / 2]]))

        self.anchors['source'] = [0, 0]
        self.anchors['drain'] = [0, -platedis]
        self.anchors['gate'] = [fclen / 8 + 0.2, -platedis / 2]

class nmos(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #####DRAIN
        self.segments.append(Segment([[0, fclen/16], [0, 0]]))
        self.segments.append(Segment([[0, 0], [(fclen/8), 0]]))

        #####SOURCE
        self.segments.append(SegmentArrow([fclen/8, -platedis], [0, -platedis], headwidth=0.1, headlength=0.1))
        self.segments.append(Segment([[0, -platedis], [0, -(platedis+fclen/16)]]))

        #####GATE
        self.segments.append(Segment([[fclen/8, fclen/16], [fclen / 8,- (platedis + fclen / 16)]]))
        self.segments.append(Segment([[fclen/8 + 0.06, 0], [fclen/8 + 0.06, -platedis]]))
        self.segments.append(Segment([[fclen/8 + 0.06, -platedis/2], [fclen/8 + 0.2, -platedis/2]]))

        self.anchors['source'] = [0, 0]
        self.anchors['drain'] = [0, -(platedis+fclen/16)]
        self.anchors['gate'] = [fclen / 8 + 0.2, -platedis / 2]

class smallseg(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append(Segment([[0, 0], [0,-platedis ]]))
        self.anchors['start'] = [0,0]
        self.anchors['center'] = [0,-platedis/2]
        self.anchors['end'] = [0,-platedis ]

class midseg(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append(Segment([[0, 0], [0,-platedis * 2.9 ]]))
        self.anchors['start'] = [0,0]
        self.anchors['center'] = [0,-platedis*1.5]
        self.anchors['end'] = [0,-platedis * 2.9 ]

class blankcircle(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append((SegmentCircle([0,0],radius = 0.04,fill=False)))

class fullcircle(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append((SegmentCircle([0, 0], radius = 0.04, fill=True)))

class srccircle(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append((SegmentCircle([0,0],radius = 0.04,fill=False)))
        self.segments.append((Segment([[0.068,0.068],[-0.068,-0.068]])))


d = schemdraw.Drawing()

########### LEFT PART ######################


M5a = d.add(pmos( lftlabel = 'M5a', color = 'black'))
l54a = d.add(smallseg('right', at = M5a.drain))

smallseg1 = d.add(smallseg('left',at = [0,0.13]))

M4a = d.add(pmos('right', at = l54a.end, lftlabel = 'M4a', color = 'black'))
vcascp1 = d.add(srccircle(at = M4a.gate, rgtlabel='$V_{cascp}$', color = 'black'))
l43a = d.add(elm.Line('down', at = M4a.drain))
d.add(fullcircle(at = l43a.center))
vout1 = d.add(smallseg('down', at = l43a.center))
voutp = d.add(blankcircle(at = [-0.543,-3],rgtlabel='Vout+'))

#
M3a = d.add(nmos('right', at = l43a.end,  lftlabel = 'M3a', color = 'black'))
vcascn1 = d.add(srccircle(at = M3a.gate,flip=True, botlabel='$V_{cascn}$', color = 'black'))
l32a = d.add(smallseg('right', at = M3a.drain))

# d.add(elm.Dot(at = l32a.center))
d.add(fullcircle(at=l32a.center))
# d.add(elm.Line('right', at = l32a.center))

linetomid1 = d.add(midseg('up', at = l32a.center))

# d.add(elm.Line(to = M1a.gate))

M2a = d.add(nmos('right', at = l32a.end,  lftlabel = 'M2a', color = 'black'))
l2g = d.add (smallseg('right', at = M2a.drain))
d.add(elm.Ground('right', at = l2g.end))






###### MIDDLE PART #####
middleline = d.add(elm.Line('right', at = M5a.gate))
middleline2 = d.add(smallseg(at = middleline.center))
M6 = d.add(pmos('left', at = middleline2.end,anchor = 'source', flip = True, rgtlabel = 'M6', color = 'black'))
vcmfb = d.add(srccircle(at = M6.gate, lftlabel='$V_{cmfb}$', color = 'black'))
middleline3 = d.add(smallseg('right', at = M6.drain))

d.add(fullcircle(at=middleline3.end))
middleline4 = d.add(smallseg('up', at = middleline3.end))
middleline5 = d.add(smallseg('down', at = middleline3.end))

middleline6 = d.add(smallseg('right',at = middleline4.end))
# d.labelI_inline(middleline6, '$I_bias$', d='in')

middleline7 = d.add(smallseg('right', at = middleline5.end))
# d.labelI_inline(middleline7, '$I_bias$', d='in')
# d.labelI_inline(middleline7,label='Ibias', d = 'up')

M1a = d.add(pmos('left',at = middleline7.end, anchor = 'source', flip = True, rgtlabel = 'M1a', color = 'black'))
vinp = d.add(blankcircle(at = [1-0.04,-2.5], lftlabel='$V_{in+}$', color = 'black'))
# d.add(elm.Line('down', at = M1a.drain))


M1b = d.add(pmos('right', at = middleline6.end, anchor = 'source', lftlabel = 'M1b', color = 'black'))
vinn = d.add(blankcircle(at = [2.9+0.04,-2.5], rgtlabel='$V_{in-}$', color = 'black'))





##### RIGHT PART ######
M5b = d.add(pmos('left', at = middleline.end, anchor = 'gate', flip = True, rgtlabel = 'M5b', color = 'black'))
l54b = d.add(smallseg('right', at = M5b.drain))

smallseg2 = d.add(smallseg('left',at = [3.9,0.13]))

M4b = d.add(pmos('left', at = l54b.end, flip = True,rgtlabel = 'M4b', color = 'black'))
vcascp2 = d.add(srccircle(at = M4b.gate, lftlabel='$V_{cascp}$', color = 'black'))
l43b = d.add(elm.Line('down', at = M4b.drain))
d.add(fullcircle(at = l43b.center))
vout2 = d.add(smallseg('up', at = l43b.center))
voutn = d.add(blankcircle(at = [4.44,-3],lftlabel='Vout-'))

#
M3b = d.add(nmos('left', at = l43b.end, flip=True,rgtlabel = 'M3b', color = 'black'))
vcascn2 = d.add(srccircle(at = M3b.gate,flip=True, label='$V_{cascn}$', color = 'black'))
l32b = d.add(smallseg('right', at = M3b.drain))
#

d.add(fullcircle(at=l32b.center))
# # d.add(elm.Line('right', at = l32a.center))
linetomid2 = d.add(midseg('down', at = l32b.center))


M2b = d.add(nmos('left', at = l32b.end, flip = True,rgtlabel = 'M2b', color = 'black'))
l2gb = d.add (smallseg('right', at = M2b.drain))
d.add(elm.Ground('right', at = l2gb.end))









##### extra lines in the middle #####
extraline1 = d.add(elm.Line(endpts=[M2a.gate, M2b.gate]))
vbiasn=d.add(fullcircle(at=extraline1.center))
extrasmallseg1 = d.add(smallseg('left', at = extraline1.center))
vbiasn1= d.add(srccircle(at=extrasmallseg1.end, label = '$V_{biasn}$', reverse = True))



d.add(elm.Line('up',at = linetomid1.end,toy=-2.89))
d.add(elm.Line('up',at = linetomid2.end,toy=-2.89))


d.add(elm.Vdd(at=smallseg1.end, label = '$V_{DD}$'))
d.add(elm.Vdd(at=smallseg2.end, label = '$V_{DD}$'))
d.add(elm.Vdd(at=[1.95,-0.25], label='$V_{DD}$'))


# d.draw()




# endpts=[Q.end, R.start]
# d.pop()
# d.add(pmos)
# d.add(nmos)
# d.save('None.png')





############### GUI #####################


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
