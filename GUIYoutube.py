#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
from urllib.request import urlretrieve

# Importando clases propias

from videoWidget import *
from BYT import *


class Ventana(QtGui.QMainWindow):

    def __init__(self):
        super(Ventana, self).__init__()
        self.ver = "0.1 Alpha"
        self.setWindowTitle("GUIYoutube - "+self.ver)
        self.setGeometry(100, 100, 800, 500)
        self.cantidad = 5
        self.reproductorPreferido = "VLC"

        self.páginaPrincipal()
        #self.poblarLista()

    def páginaPrincipal(self):

        # Widget y Layout para el centro de la ventana.

        self.widgetPrincipal = QtGui.QWidget(self)
        self.layoutPrincipal = QtGui.QGridLayout()
        self.widgetPrincipal.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.widgetPrincipal)

        # Scrolled area para la lista de videos.

        self.scroll = QtGui.QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setMinimumSize(550, 300)
        self.layoutPrincipal.addWidget(self.scroll, 0, 0, 6, 4)

        # LineEdit para el término de búsqueda.Ventana

        self.términoDeBúsqueda = QtGui.QLineEdit("Término de búsqueda", self)

        #usar Intro en el line edit por alguna razón no actualiza el label. Comentado por ahora.
        #self.términoDeBúsqueda.returnPressed.connect(self.consulta)

        self.layoutPrincipal.addWidget(self.términoDeBúsqueda, 0, 4, 1, 2)

        # Botón Buscar para búsqueda.

        self.buscarBtn = QtGui.QPushButton("Buscar en YT", self)
        self.layoutPrincipal.addWidget(self.buscarBtn, 1, 5, 1, -1)
        self.buscarBtn.pressed.connect(self.consulta)

        # Lista de opciones para número de búsquedas.

        self.listaDeOpciones = QtGui.QGroupBox("Selecciona la cantidad de videos a buscar:", self)
        self.listaLayout = QtGui.QVBoxLayout(self)

        self.layoutPrincipal.addWidget(self.listaDeOpciones, 3, 4, 1, 2)

        self.opción1 = QtGui.QRadioButton("1 video (primer resultado, más rápido)", self)
        self.opción2 = QtGui.QRadioButton("5 videos (primeros 5 resultados)", self)
        self.opción3 = QtGui.QRadioButton("10 videos (primeros 10 resultados. Lento)", self)

        self.listaLayout.addWidget(self.opción1)
        self.listaLayout.addWidget(self.opción2)
        self.listaLayout.addWidget(self.opción3)

        self.listaDeOpciones.setLayout(self.listaLayout)

        # ComboBox para elegir reproductor.

        #self.reproductorLista = QtGui.QComboBox(self)
        #self.reproductorLabel = QtGui.QLabel("Elegir reproductor:", self)

        #self.reproductorLista.addItem("VLC Media Player")
        #self.reproductorLista.addItem("MPV Media Player")

        #self.reproductorLista.activated[str].connect(self.playerSwitch)

        #self.layoutPrincipal.addWidget(self.reproductorLabel, 5, 4, 1, 1)
        #self.layoutPrincipal.addWidget(self.reproductorLista, 5, 5, 1, 1)

        # Label para mostrar el progreso de las operaciones
        self.aviso = QtGui.QLabel(self)
        self.aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.layoutPrincipal.addWidget(self.aviso, 2, 4, 1, 2)

        # Pop-up para elegir reproductor.
        self.popup = QtGui.QMessageBox(self)
        self.popup.setText("Es necesario elegir un reproductor instalado antes de proceder.")
        self.VLCPlayer = self.popup.addButton("VLC Media Player", QtGui.QMessageBox.ActionRole)
        self.MPVPlayer = self.popup.addButton("MPV Media Player", QtGui.QMessageBox.ActionRole)
        self.popup.exec()
        if "VLC" in self.popup.clickedButton().text():
            self.reproductorPreferido = "VLC"
        if "MPV" in self.popup.clickedButton().text():
            self.reproductorPreferido = "MPV"

        self.show()

    # Función de prueba para poblar el scroll principal. Eliminar/comentar para
    # publicar la aplicación o antes del merge con master!

    #def playerSwitch(self, text):
        #if "VLC" in self.popup.clickedButton().text():
            #self.reproductorPreferido = "VLC"
        #if "MPV" in self.popup.clickedButton().text():
            #self.reproductorPreferido = "MPV"

    def consulta(self):

        self.aviso.setText("Buscando videos en YouTube. \n Sólo tomará unos sengundos.")
        QtGui.QApplication.processEvents()

        if self.opción1.isChecked() == True:
            self.cantidad = 1
        if self.opción2.isChecked() == True:
            self.cantidad = 5
        if self.opción3.isChecked() == True:
            self.cantidad = 10

        término = self.términoDeBúsqueda.text()
        objetoBúsqueda = BYT(término, self.cantidad)
        self.resultados = objetoBúsqueda.obtenerDatos()

        self.poblarLista(self.resultados, self.cantidad)

    def poblarLista(self, resultados, cantidad):

        tempWidget = QtGui.QWidget(self)
        tempLayout = QtGui.QVBoxLayout(self)
        tempWidget.setLayout(tempLayout)

        for i in range(0, cantidad):
            videoBlock = VideoWidget(resultados["Título" + str(i)], i,
                                    resultados["Duración" + str(i)],
                                    resultados["PlayVLC" + str(i)],
                                    resultados["PlayMPV" + str(i)],
                                    resultados["Descarga" + str(i)],
                                    self.reproductorPreferido)
            tempLayout.addWidget(videoBlock)
            self.aviso.setText("")
        self.scroll.setWidget(tempWidget)

app = QtGui.QApplication(sys.argv)
win = Ventana()
sys.exit(app.exec_())