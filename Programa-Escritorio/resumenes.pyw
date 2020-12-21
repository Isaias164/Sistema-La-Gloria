# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resumenes(object):
    def setupUi(self, resumenes):
        resumenes.setObjectName("resumenes")
        resumenes.setWindowModality(QtCore.Qt.ApplicationModal)
        resumenes.resize(640, 480)
        resumenes.setMaximumSize(QtCore.QSize(640, 480))
        resumenes.setStyleSheet("background-color: rgb(70, 70, 70);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/t.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resumenes.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(resumenes)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(resumenes)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateEditFechaConsulta = QtWidgets.QDateEdit(resumenes)
        self.dateEditFechaConsulta.setCalendarPopup(True)
        self.dateEditFechaConsulta.setObjectName("dateEditFechaConsulta")
        self.horizontalLayout.addWidget(self.dateEditFechaConsulta)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tablaResumenes = QtWidgets.QTableView(resumenes)
        self.tablaResumenes.setStyleSheet("background-color: rgb(106, 106, 106);")
        self.tablaResumenes.setObjectName("tablaResumenes")
        self.gridLayout.addWidget(self.tablaResumenes, 1, 0, 1, 1)

        self.retranslateUi(resumenes)
        QtCore.QMetaObject.connectSlotsByName(resumenes)

    def retranslateUi(self, resumenes):
        _translate = QtCore.QCoreApplication.translate
        resumenes.setWindowTitle(_translate("resumenes", "resumenes"))
        self.label.setText(_translate("resumenes", "Fecha de consulta"))
