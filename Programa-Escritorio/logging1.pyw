# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from vistaRecuperacionUser import RecuperacionCorreoUsusario
from sys import argv,exit
from Logica.Logicalogging import LogicaLog
from Creacion_del_usuario import CuentaUsuario

class FormularioLogeo(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.cuentaUsuario = CuentaUsuario()
        CuentaUsuario.ventanaCuentaUsuario = self.cuentaUsuario
        self.cuentaUsuario.setupUi(self.cuentaUsuario)
        self.rcu = RecuperacionCorreoUsusario()
        self.rcu.setupUi(self.rcu)

    def verificar(self):
        l = LogicaLog()
        l.verificarUC(self.lineEditUsuario.text(), self.lineEditContrasena.text())
        
    def mostrarContrasena(self):
        obj = LogicaLog()
        obj.mostrarContras(self.lineEditContrasena,self.checkBoxMostrarContrasea)
    
    def ocultarLogeo(self):
        try:
            LogicaLog.ventanaPadre.hide()
        except:
            pass

    def setupUi(self, FormularioLogeo):
        FormularioLogeo.setObjectName("FormularioLogeo")
        FormularioLogeo.setWindowModality(QtCore.Qt.WindowModal)
        FormularioLogeo.resize(736, 480)
        FormularioLogeo.setMinimumSize(QtCore.QSize(736, 480))
        FormularioLogeo.setMaximumSize(QtCore.QSize(736, 480))
        FormularioLogeo.setLayoutDirection(QtCore.Qt.LeftToRight)
        FormularioLogeo.setStyleSheet("background-color: rgb(221, 221, 221);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormularioLogeo.setWindowIcon(icon)
        self.lineEditContrasena = QtWidgets.QLineEdit(FormularioLogeo)
        self.lineEditContrasena.setGeometry(QtCore.QRect(200, 90, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditContrasena.setFont(font)
        self.lineEditContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditContrasena.setClearButtonEnabled(True)
        self.lineEditContrasena.setObjectName("lineEditContrasena")
        self.label_2 = QtWidgets.QLabel(FormularioLogeo)
        self.label_2.setGeometry(QtCore.QRect(14, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditUsuario = QtWidgets.QLineEdit(FormularioLogeo)
        self.lineEditUsuario.setGeometry(QtCore.QRect(200, 20, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditUsuario.setFont(font)
        self.lineEditUsuario.setClearButtonEnabled(True)
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.label = QtWidgets.QLabel(FormularioLogeo)
        self.label.setGeometry(QtCore.QRect(19, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelOlvideContrasena = QtWidgets.QLabel(FormularioLogeo)
        self.labelOlvideContrasena.setGeometry(QtCore.QRect(200, 340, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelOlvideContrasena.setFont(font)
        self.labelOlvideContrasena.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelOlvideContrasena.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelOlvideContrasena.setAlignment(QtCore.Qt.AlignLeft)
        self.labelOlvideContrasena.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.labelOlvideContrasena.setObjectName("labelOlvideContrasena")
        self.botonIngresar = QtWidgets.QPushButton(FormularioLogeo)
        self.botonIngresar.setGeometry(QtCore.QRect(360, 180, 161, 51))
        self.botonIngresar.setStyleSheet("background:green;color:white;")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonIngresar.setFont(font)
        self.botonIngresar.setFont(font)
        self.botonIngresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonIngresar.setObjectName("botonIngresar")
        self.labelCrearCuenta = QtWidgets.QLabel(FormularioLogeo)
        self.labelCrearCuenta.setGeometry(QtCore.QRect(200, 420, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCrearCuenta.setFont(font)
        self.labelCrearCuenta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelCrearCuenta.setAlignment(QtCore.Qt.AlignLeft)
        self.labelCrearCuenta.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.labelCrearCuenta.setObjectName("labelCrearCuenta")
        self.checkBoxMostrarContrasea = QtWidgets.QCheckBox(FormularioLogeo)
        self.checkBoxMostrarContrasea.setGeometry(QtCore.QRect(200, 280, 361, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxMostrarContrasea.setFont(font)
        self.checkBoxMostrarContrasea.setObjectName("checkBoxMostrarContrasea")
        self.retranslateUi(FormularioLogeo)
        QtCore.QMetaObject.connectSlotsByName(FormularioLogeo)
        FormularioLogeo.setTabOrder(self.lineEditUsuario, self.lineEditContrasena)
        FormularioLogeo.setTabOrder(self.lineEditContrasena, self.botonIngresar)
        FormularioLogeo.setTabOrder(self.botonIngresar, self.checkBoxMostrarContrasea)
        
        #eventos
        self.botonIngresar.clicked.connect(self.verificar)
        self.checkBoxMostrarContrasea.clicked.connect(self.mostrarContrasena)
        #LogicaLog.ventanaPadre.triggered.connect(LogicaLog.ventanaPadre.close)       
        self.labelCrearCuenta.linkActivated.connect(self.cuentaUsuario.show)
        #self.labelCrearCuenta.linkActivated.connect(self.ocultarLogeo)
        self.labelOlvideContrasena.linkActivated.connect(self.rcu.show)
        
    def retranslateUi(self, FormularioLogeo):
        _translate = QtCore.QCoreApplication.translate
        FormularioLogeo.setWindowTitle(_translate("FormularioLogeo", "Login"))
        self.lineEditContrasena.setPlaceholderText(_translate("FormularioLogeo", "Ingrese su contraseña"))
        self.label_2.setText(_translate("FormularioLogeo", "Contraseña"))
        self.lineEditUsuario.setPlaceholderText(_translate("FormularioLogeo", "Ingrese su usuario"))
        self.label.setText(_translate("FormularioLogeo", "Usuario"))
        self.labelOlvideContrasena.setText(_translate("FormularioLogeo", "<html><head/><body><p><a href=\"ccs\"><span style=\" text-decoration: underline; color:green;\">Olvide mi contraseña</span></a></p></body></html>"))
        self.botonIngresar.setText(_translate("FormularioLogeo", "Ingresar"))
        self.labelCrearCuenta.setText(_translate("FormularioLogeo", "<html><head/><body><p><a href=\"ss\"><span style=\" text-decoration: underline; color:green;\">Crear cuenta</span></a><a href=\"ss\"><span style=\" color:#00aa00;\"/></a></p></body></html>"))
        self.checkBoxMostrarContrasea.setText(_translate("FormularioLogeo", "Mostrar constraseña"))
    
# app = QtWidgets.QApplication(argv)
# log = FormularioLogeo()
# log.setupUi(log)
# log.show()
# exit(app.exec_()) 