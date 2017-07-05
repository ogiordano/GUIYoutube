# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

class VideoWidget(QtGui.QWidget):

    def __init__(self, title, orden, duración):
        QtGui.QWidget.__init__(self)
        self.orden = orden
        self.title = title
        self.duración = duración
        self.setObjectName(("widget"))
        #self.resize(593, 176)
        self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(self.sizePolicy)
        self.setMaximumSize(QtCore.QSize(640, 180))
        #self.setMinimumSize(QtCore.QSize(450, 150))

        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(("gridLayout"))

        #Botón Play
        self.playBtn = QtGui.QPushButton("Play", self)
        self.playBtn.setObjectName(("playBtn"))
        self.gridLayout.addWidget(self.playBtn, 2, 2, 1, 1)

        #Label con título de video
        self.titleLabel = QtGui.QLabel(self.title, self)
        self.titleLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName(("titleLabel"))
        self.gridLayout.addWidget(self.titleLabel, 0, 2, 2, 4)

        #Botón Descarga
        self.downloadBtn = QtGui.QPushButton("Descargar", self)
        self.downloadBtn.setObjectName(("downloadBtn"))
        self.gridLayout.addWidget(self.downloadBtn, 2, 5, 1, 1)

        #Label del thumbnail
        self.thumbLabel = QtGui.QLabel(self)
        self.pic = QtGui.QPixmap("thumbs/" + str(self.orden) + ".jpg")
        self.thumbLabel.setPixmap(self.pic)
        self.thumbLabel.setScaledContents(True)
        self.thumbLabel.setMaximumWidth(220)
        self.thumbLabel.setMaximumHeight(120)
        self.gridLayout.addWidget(self.thumbLabel, 0, 0, 3, 2)

        #Label de duración
        self.durLabel = QtGui.QLabel("Time: " + str(self.duración), self)
        self.durLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.durLabel, 2, 3, 1, 2)