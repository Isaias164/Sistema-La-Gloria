# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMainWindow,QApplication
from sys import argv,exit
from Logica.Logicalogging import Verificaciones,ConsultasApi,MetodosPost,LogicaLog

class Turnos(QtWidgets.QMainWindow):
    nombreEtiqueta = "Futbol"
    depo = "gym"

    def formatFecha(self,fecha1):
        from datetime import datetime
        una_fecha = fecha1
        fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
        fecha = str(fecha_dt)
        return fecha[0:10]

    def enviarDatos(self):
        obj = Verificaciones()
        camposVacios = obj.verificarTextoVacio((self.lineEditApellido,self.lineEditNombre))
        if(camposVacios):
            f = self.formatFecha(self.dateEditFecha.text())
            obj1 = MetodosPost()
            mensaje = obj1.hacerReserba(self.lineEditNombre.text(),self.lineEditApellido.text(),f,self.comboBoxInicio.currentText(),Turnos.depo)
            QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Mensaje",mensaje)
            self.close()
        else:
             QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Error","Hay campos sin completar")

    def setupUi(self, turnos):
        turnos.setObjectName("turnos")
        turnos.resize(737, 544)
        turnos.setMaximumSize(QtCore.QSize(737, 544))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        turnos.setWindowIcon(icon)
        turnos.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButton = QtWidgets.QPushButton(turnos)
        self.pushButton.setGeometry(QtCore.QRect(280, 420, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background:green;color:white;font-size:16")
        """
        self.label_9 = QtWidgets.QLabel(turnos)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        """
        self.label_2 = QtWidgets.QLabel(turnos)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelDeportes = QtWidgets.QLabel(turnos)
        self.labelDeportes.setGeometry(QtCore.QRect(150, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelDeportes.setFont(font)
        self.labelDeportes.setObjectName("labelDeportes")
        self.label = QtWidgets.QLabel(turnos)
        self.label.setGeometry(QtCore.QRect(10, 70, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditNombre = QtWidgets.QLineEdit(turnos)
        self.lineEditNombre.setGeometry(QtCore.QRect(140, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditNombre.setFont(font)
        self.lineEditNombre.setClearButtonEnabled(True)
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.label_3 = QtWidgets.QLabel(turnos)
        self.label_3.setGeometry(QtCore.QRect(360, 70, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.lineEditApellido = QtWidgets.QLineEdit(turnos)
        self.lineEditApellido.setGeometry(QtCore.QRect(520, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditApellido.setFont(font)
        self.lineEditApellido.setClearButtonEnabled(True)
        self.lineEditApellido.setObjectName("lineEditApellido")
        self.dateEditFecha = QtWidgets.QDateEdit(turnos)
        self.dateEditFecha.setGeometry(QtCore.QRect(140, 120, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditFecha.setFont(font)
        self.dateEditFecha.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateEditFecha.setCalendarPopup(True)
        self.dateEditFecha.setObjectName("dateEditFecha")
        self.label_4 = QtWidgets.QLabel(turnos)
        self.label_4.setGeometry(QtCore.QRect(280, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBoxInicio = QtWidgets.QComboBox(turnos)
        self.comboBoxInicio.setGeometry(QtCore.QRect(410, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.comboBoxInicio.setFont(font)
        self.comboBoxInicio.setMouseTracking(True)
        self.comboBoxInicio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxInicio.setMaxVisibleItems(5)
        self.comboBoxInicio.setObjectName("comboBoxInicio")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        self.comboBoxInicio.addItem("")
        """
        self.comboBoxPago = QtWidgets.QComboBox(turnos)
        self.comboBoxPago.setGeometry(QtCore.QRect(140, 240, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxPago.setFont(font)
        self.comboBoxPago.setObjectName("comboBoxPago")
        self.comboBoxPago.addItem("")
        self.comboBoxPago.addItem("")
        """
        self.label_5 = QtWidgets.QLabel(turnos)
        self.label_5.setGeometry(QtCore.QRect(540, 130, 141, 25))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(turnos)
        self.lineEdit.setGeometry(QtCore.QRect(690, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(turnos)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(turnos)
        QtCore.QMetaObject.connectSlotsByName(turnos)
        
        self.labelDeportes.setText(Turnos.nombreEtiqueta)

        self.pushButton.clicked.connect(self.enviarDatos)
        
        
    def retranslateUi(self, turnos):
        _translate = QtCore.QCoreApplication.translate
        turnos.setWindowTitle(_translate("turnos", "Turnos"))
        self.pushButton.setText(_translate("turnos", "¡Listo!"))
        #self.label_9.setText(_translate("turnos", "Pago"))
        self.label_2.setText(_translate("turnos", "Fecha"))
        self.labelDeportes.setText(_translate("turnos", "xxx"))
        self.label.setText(_translate("turnos", "Nombre"))
        self.label_3.setText(_translate("turnos", "Apellido"))
        self.label_4.setText(_translate("turnos", "horario"))
        self.comboBoxInicio.setItemText(0, _translate("turnos", "10"))
        self.comboBoxInicio.setItemText(1, _translate("turnos", "11"))
        self.comboBoxInicio.setItemText(2, _translate("turnos", "12"))
        self.comboBoxInicio.setItemText(3, _translate("turnos", "13"))
        self.comboBoxInicio.setItemText(4, _translate("turnos", "14"))
        self.comboBoxInicio.setItemText(5, _translate("turnos", "15"))
        self.comboBoxInicio.setItemText(6, _translate("turnos", "16"))
        self.comboBoxInicio.setItemText(7, _translate("turnos", "17 "))
        self.comboBoxInicio.setItemText(8, _translate("turnos", "18"))
        self.comboBoxInicio.setItemText(9, _translate("turnos", "19 "))
        self.comboBoxInicio.setItemText(10, _translate("turnos", "20"))
        self.comboBoxInicio.setItemText(11, _translate("turnos", "21"))
        #self.comboBoxPago.setItemText(0, _translate("turnos", "No"))
        #self.comboBoxPago.setItemText(1, _translate("turnos", "Si"))
        self.label_5.setText(_translate("turnos", "Cantidad/hora"))
        self.lineEdit.setText(_translate("turnos", "1"))
        self.label_6.setText(_translate("turnos", "Deporte"))

# app = QtWidgets.QApplication(argv)
# vt = Turnos()
# vt.setupUi(vt)
# vt.show()
# exit(app.exec_())