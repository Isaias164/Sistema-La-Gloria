# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from sys import exit,argv
from Logica.Logicalogging import RecuperacionCorreo
from unicodedata import normalize

class RecuperacionCorreoUsusario(QtWidgets.QMainWindow):

    def enviar(self):
        if(self.correo.text() != ""):
            self.barraEstado.show()
            self.barraEstado.setValue(25)
            conf = RecuperacionCorreo()
            self.barraEstado.setValue(50)
            resp = conf.recuCorreo(self.correo.text())
            #resp = str(normalize('NFD', resp).encode('utf-8', 'ignore'))
            #resp = decode(resp,encoding="utf-8")
            self.barraEstado.setValue(75)
            if(resp[0] == "N" ):
                QtWidgets.QMessageBox.about(self,"Mensaje",resp)
                self.barraEstado.hide()
            else:
                self.barraEstado.setValue(100)
                QtWidgets.QMessageBox.about(self,"Mensaje",resp)
                from time import sleep
                sleep(1.1)
                self.barraEstado.hide()
                self.close()
        else:
            QtWidgets.QMessageBox.about(self,"Error","hay campos sin completar")


    def setupUi(self, recuCorreo):
        recuCorreo.setObjectName("recuCorreo")
        recuCorreo.resize(640, 163)
        recuCorreo.setMinimumSize(QtCore.QSize(640, 163))
        recuCorreo.setMaximumSize(QtCore.QSize(640, 163))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/pwd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        recuCorreo.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(recuCorreo)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 611, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.splitter = QtWidgets.QSplitter(recuCorreo)
        self.splitter.setGeometry(QtCore.QRect(10, 120, 621, 33))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.correo = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.correo.setFont(font)
        self.correo.setObjectName("correo")
        self.boton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boton.setFont(font)
        self.boton.setObjectName("boton")
        self.barraEstado = QtWidgets.QProgressBar(self)
        self.barraEstado.setGeometry(180, 70, 300, 25)
        self.barraEstado.setMaximum(100)
        self.barraEstado.hide()
        #self.barraEstado.show()

        self.retranslateUi(recuCorreo)
        QtCore.QMetaObject.connectSlotsByName(recuCorreo)

        self.boton.clicked.connect(self.enviar)

    def retranslateUi(self, recuCorreo):
        _translate = QtCore.QCoreApplication.translate
        recuCorreo.setWindowTitle(_translate("recuCorreo", "Recuperación de contraseña"))
        self.textBrowser.setHtml(_translate("recuCorreo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap;}\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;font-weight:400; font-style:normal;\">\n"
"<p style=\"color:green;margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#515151;\">Para recuperar su contraseña debe ingresar el correo que utilizo para crear su usuario. La nueva contraseña se le enviara a ese correo.</span></p></body></html>"))
        self.correo.setPlaceholderText(_translate("recuCorreo", "Ingrese su correo"))
        self.boton.setText(_translate("recuCorreo", "¡Listo!"))

# app = QtWidgets.QApplication(argv)
# mp = RecuperacionCorreoUsusario()
# mp.setupUi(mp)
# mp.show()
# exit(app.exec_()) 