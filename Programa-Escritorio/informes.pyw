# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv,exit
from Logica.Logicalogging import Montos

class Informe(QtWidgets.QMainWindow):

    def formatFecha(self,fecha1):
        from datetime import datetime
        una_fecha = fecha1
        fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
        fecha = str(fecha_dt)
        return fecha[0:10]

    def traerMonto(self):
        resumen = self.comboBoxeleguirResumen.currentText()
        self.textBrowserEscribirResumen.clear()
        fecha = self.formatFecha(self.dateEditFecha.text())
        #print(fecha)
        if(resumen == "Ver lo recaudado del Bar"):
            bar = Montos()
            mensaje = bar.monto("montoProducto",fecha)
            self.textBrowserEscribirResumen.append("<p>Fecha de resumen para el "+"<h3><i>Bar</i></h3>"+" el día "+ self.dateEditFecha.text() + " se obtuvo una recaudación en el bar de <p style=color:green>"+ str(mensaje)+"$</p></p>")
        else:
            bar = Montos()
            mensaje = bar.monto("montoReserba",fecha)
            self.textBrowserEscribirResumen.append("<p>Fecha de resumen para las "+"<h2><i>Reserbas</i></h2>"+ self.dateEditFecha.text() +" se obtuvo una recaudación en el bar de <p style=color:green>"+str(mensaje) +"$</p></p>")

    def setupUi(self, resumenes):
        resumenes.setObjectName("resumenes")
        resumenes.resize(745, 470)
        resumenes.setMinimumSize(QtCore.QSize(745, 470))
        resumenes.setMaximumSize(QtCore.QSize(745, 470))
        #resumenes.setWindowTitle()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/smiley-dolar_icon-icons.com_48451.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resumenes.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(resumenes)
        self.widget.setGeometry(QtCore.QRect(0, 0, 744, 461))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxeleguirResumen = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxeleguirResumen.setFont(font)
        self.comboBoxeleguirResumen.setObjectName("comboBoxeleguirResumen")
        self.comboBoxeleguirResumen.addItem("")
        self.comboBoxeleguirResumen.addItem("")
        self.gridLayout.addWidget(self.comboBoxeleguirResumen, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dateEditFecha = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEditFecha.setFont(font)
        self.dateEditFecha.setCalendarPopup(True)
        self.dateEditFecha.setObjectName("dateEditFecha")
        self.gridLayout.addWidget(self.dateEditFecha, 1, 1, 1, 1)
        self.textBrowserEscribirResumen = QtWidgets.QTextBrowser(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowserEscribirResumen.setFont(font)
        self.textBrowserEscribirResumen.setObjectName("textBrowserEscribirResumen")
        self.gridLayout.addWidget(self.textBrowserEscribirResumen, 2, 0, 1, 2)

        self.comboBoxeleguirResumen.currentTextChanged.connect(self.traerMonto)
        self.dateEditFecha.dateChanged.connect(self.traerMonto)
        self.retranslateUi(resumenes)
        QtCore.QMetaObject.connectSlotsByName(resumenes)

    def retranslateUi(self, resumenes):
        _translate = QtCore.QCoreApplication.translate
        resumenes.setWindowTitle(_translate("resumenes", "Dialog"))
        self.comboBoxeleguirResumen.setItemText(0, _translate("resumenes", "Ver lo recaudado de la venta de las Reserbas"))
        self.comboBoxeleguirResumen.setItemText(1, _translate("resumenes", "Ver lo recaudado del Bar"))
        self.label.setText(_translate("resumenes", "Fecha del resumen"))


# app = QtWidgets.QApplication(argv)
# mp = Informe()
# mp.setupUi(mp)
# mp.showMaximized()
# exit(app.exec_()) 

   