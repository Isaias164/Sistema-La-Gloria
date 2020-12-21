# -*- coding: utf-8 -*-
from sys import argv,exit
from PyQt5 import QtCore, QtGui, QtWidgets
from Logica.Logicalogging import Verificaciones,MetodosPost,LogicaLog
from hashlib import sha224

class CuentaUsuario(QtWidgets.QMainWindow):
        ventanaCuentaUsuario = None

        def verificarNumeroCelulalar(self):
                try:    
                        int(self.celular.text())
                except:
                        #QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Su número de celular no es valido.Por favor ingrese un número de celular valido")
                        self.celular.clear()

        def verificarUsuario(self):
                obj = Verificaciones()
                datosPersonales = (self.nombreP,self.apellidoP,self.celular,self.direccion)
                if(obj.verificarTextoVacio(datosPersonales)):
                        datosUsuario = (self.lineEdit_2,self.ingreseCorreoElectronico,self.ingresaContrasena)
                        if(obj.verificarTextoVacio(datosUsuario)):
                                bandera = obj.correoValido(self.ingreseCorreoElectronico.text())
                                if(not bandera):
                                        QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Su correo no es valido.Por favor ingrese un correo valido")
                                else:
                                        if(len(self.ingresaContrasena.text()) >= 8):
                                                if (self.ingresaContrasena.text() == self.repitaContrasena.text()):
                                                        mthPost = MetodosPost()
                                                        u = sha224(bytes(self.lineEdit_2.text(),encoding="utf-8")).hexdigest()
                                                        p = sha224(bytes(self.ingresaContrasena.text(),encoding="utf-8")).hexdigest()
                                                        msg = mthPost.crearEmpleado({"codigo":0,"usuario":u,"pwd":p,"gmail":self.ingreseCorreoElectronico.text(),"nombre":self.nombreP.text(),"apellido":self.apellidoP.text(),"direccion":self.direccion.text(),"telefono":self.celular.text()})
                                                        QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Felicidades",msg)
                                                        id = LogicaLog()
                                                        id.verificarUC(self.lineEdit_2.text(),self.ingresaContrasena.text())
                                                        #LogicaLog.menuPrincipal.showMaximized()
                                                        LogicaLog.ventanaPadre.close()
                                                        CuentaUsuario.ventanaCuentaUsuario.close()

                                                else:
                                                        QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Las constraseñas no coinciden")
                                        else:
                                                QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","La longitud de la constraseña debe ser igual o mayor a 8 caracteres")
                        else:
                                QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Hay datos de usuario sin completar")

                else:
                        QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Hay datos personales sin comletar")


        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(790, 565)
                Dialog.setMinimumSize(QtCore.QSize(790, 565))
                Dialog.setMaximumSize(QtCore.QSize(790, 565))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Imagenes/business_application_addmale_useradd_insert_add_user_client_2312.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Dialog.setWindowIcon(icon)
                Dialog.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.tablaDatos = QtWidgets.QTabWidget(Dialog)
                self.tablaDatos.setGeometry(QtCore.QRect(0, 0, 790, 571))
                self.tablaDatos.setMinimumSize(QtCore.QSize(790, 571))
                self.tablaDatos.setMaximumSize(QtCore.QSize(790, 571))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.tablaDatos.setFont(font)
                self.tablaDatos.setObjectName("tablaDatos")
                self.datosPersonales = QtWidgets.QWidget()
                self.datosPersonales.setStyleSheet("color: rgb(141, 141, 141);\n"
        "selection-background-color: rgb(91, 91, 91);")
                self.datosPersonales.setObjectName("datosPersonales")
                self.nombreP = QtWidgets.QLineEdit(self.datosPersonales)
                self.nombreP.setGeometry(QtCore.QRect(110, 30, 501, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.nombreP.setFont(font)
                self.nombreP.setStyleSheet("color: black;")
                self.nombreP.setObjectName("nombreP")
                self.celular = QtWidgets.QLineEdit(self.datosPersonales)
                self.celular.setGeometry(QtCore.QRect(110, 240, 501, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.celular.setFont(font)
                self.celular.setStyleSheet("color: black;")
                self.celular.setObjectName("celular")
                self.apellidoP = QtWidgets.QLineEdit(self.datosPersonales)
                self.apellidoP.setGeometry(QtCore.QRect(110, 100, 501, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.apellidoP.setFont(font)
                self.apellidoP.setStyleSheet("color: black;")
                self.apellidoP.setObjectName("apellidoP")
                self.direccion = QtWidgets.QLineEdit(self.datosPersonales)
                self.direccion.setGeometry(QtCore.QRect(110, 170, 501, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.direccion.setFont(font)
                self.direccion.setStyleSheet("color: black;")
                self.direccion.setObjectName("direccion")
                self.tablaDatos.addTab(self.datosPersonales, "")
                self.datosCuenta = QtWidgets.QWidget()
                self.datosCuenta.setStyleSheet("color: rgb(141, 141, 141);\n"
        "selection-background-color: rgb(91, 91, 91);")
                self.datosCuenta.setObjectName("datosCuenta")
                self.ingresaContrasena = QtWidgets.QLineEdit(self.datosCuenta)
                self.ingresaContrasena.setGeometry(QtCore.QRect(120, 190, 571, 61))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.ingresaContrasena.setFont(font)
                self.ingresaContrasena.setObjectName("ingresaContrasena")
                self.ingresaContrasena.setStyleSheet("color:black")
                self.ingreseCorreoElectronico = QtWidgets.QLineEdit(self.datosCuenta)
                self.ingreseCorreoElectronico.setGeometry(QtCore.QRect(120, 110, 571, 51))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.ingreseCorreoElectronico.setFont(font)
                self.ingreseCorreoElectronico.setObjectName("ingreseCorreoElectronico")
                self.ingreseCorreoElectronico.setStyleSheet("color:black")
                self.repitaContrasena = QtWidgets.QLineEdit(self.datosCuenta)
                self.repitaContrasena.setGeometry(QtCore.QRect(120, 280, 571, 51))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.repitaContrasena.setFont(font)
                self.repitaContrasena.setObjectName("repitaContrasena")
                self.repitaContrasena.setStyleSheet("color:black")
                self.pushButton = QtWidgets.QPushButton(self.datosCuenta)
                self.pushButton.setEnabled(True)
                self.pushButton.setGeometry(QtCore.QRect(270, 410, 271, 51))
                self.pushButton.setStyleSheet("background:green;color:white;")
                self.pushButton.setFont(font)
                self.pushButton.setObjectName("pushButton")
                self.tablaDatos.addTab(self.datosCuenta, "")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.datosCuenta)
                self.lineEdit_2.setStyleSheet("color:black")
                self.lineEdit_2.setGeometry(QtCore.QRect(120, 30, 571, 51))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setObjectName("lineEdit_2")
                

                self.retranslateUi(Dialog)
                self.tablaDatos.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

                self.celular.textChanged.connect(self.verificarNumeroCelulalar)
                self.pushButton.clicked.connect(self.verificarUsuario)

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Creación de usuario"))
                self.nombreP.setPlaceholderText(_translate("Dialog", "Ingrese su nombre"))
                self.celular.setPlaceholderText(_translate("Dialog", "Ingrese su número de celular"))
                self.apellidoP.setPlaceholderText(_translate("Dialog", "Ingrese su apellido"))
                self.direccion.setPlaceholderText(_translate("Dialog", "Ingrese su dirección"))
                self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.datosPersonales), _translate("Dialog", "Datos personales"))
                self.ingresaContrasena.setPlaceholderText(_translate("Dialog", "Ingrese su contraseña (min 8 caracteres)"))
                self.ingreseCorreoElectronico.setPlaceholderText(_translate("Dialog", "Ingrese su correo electronico"))
                self.repitaContrasena.setPlaceholderText(_translate("Dialog", "Repita la contraseña"))
                self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Ingrese su nomre de usuario"))
                self.pushButton.setText(_translate("Dialog", "Finalizado"))
                self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.datosCuenta), _translate("Dialog", "Datos de la cuenta"))


# app = QtWidgets.QApplication(argv)
# mp = CuentaUsuario()
# mp.setupUi(mp)
# mp.show()
# exit(app.exec_())