# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from abmProductos import VentanaABM
from sys import argv,exit
from Logica.Logicalogging import Grillas,MetodosPost
from threading import Timer

class VentanaProductos(QtWidgets.QMainWindow):

    def __init__(self, parent=None): 
        QtWidgets.QMainWindow.__init__(self, parent) 
        self.productosABM = VentanaABM()
        self.productosABM.setupUi(self.productosABM)    

    def mostrarDatosLike(self):
        producto = self.comboBoxProductos.currentText()
        if(producto == "Productos"):
            self.tablaProductos.clear()
            self.labelProductos.hide()
            datos = Grillas()
            datos.traerProductos(self.tablaProductos,conLike=True,palabra=self.lineEditBuscar.text())

    def mostrarProductos(self):
        self.lineEditBuscar.setEnabled(True)
        Grillas.label1 = self.labelProductos
        opcion = self.comboBoxProductos.currentText()
        if(opcion == "Productos"):
            Grillas.mensajeLabel = "No hay productos insertados para mostrar"
            datos = Grillas()
            datos.traerProductos(self.tablaProductos)
        else:
            self.tablaProductos.clear()
            Grillas.mensajeLabel = "No hay ventas realizadas para mostrar"
            datos = Grillas()
            #self.labelProductos.hide()
            datos.traerVentasRealizadasDelDia(self.tablaProductos)
            self.lineEditBuscar.setEnabled(False)

    def registrarVenta(self):
        columna = self.tablaProductos.currentColumn()
        if(columna == 4):
            fila = self.tablaProductos.currentRow()
            items = []
            for col in range(4):
                if(col == 3):
                    try:
                        int(self.tablaProductos.item(fila,col).text())
                        items.append(self.tablaProductos.item(fila,col).text())
                    except:
                        QtWidgets.QMessageBox.about(self,"Error","La cantidad que ingresaste no es un valor numerico entero")
                        datos1 = QtWidgets.QTableWidgetItem("1")
                        self.tablaProductos.setItem(fila,3,datos1)
                else:
                    if(not col == 1):
                        items.append(self.tablaProductos.item(fila,col).text())

            precioT = float(items[1]) * int(items[2])
            obj = MetodosPost()
            nombre = items[0]
            precioUnidad = items[1]
            cantidadVend = items[2]
            mensaje = obj.insertarVentaRealizada(nombre,cantidadVend,precioUnidad,precioT)
            QtWidgets.QMessageBox.about(self,"Mensaje","Usted debe abonar " + str(precioT)+"$")
            QtWidgets.QMessageBox.about(self,"Mensaje ",mensaje)
            self.mostrarProductos()

    def setupUi1(self, ventanaProductos):
        ventanaProductos.setObjectName("ventanaProductos")
        ventanaProductos.resize(708, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/aa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventanaProductos.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ventanaProductos)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxProductos = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxProductos.setFont(font)
        self.comboBoxProductos.setTabletTracking(False)
        self.comboBoxProductos.setObjectName("comboBoxProductos")
        self.comboBoxProductos.addItem("")
        self.comboBoxProductos.addItem("")
        self.gridLayout.addWidget(self.comboBoxProductos, 0, 0, 1, 1)
        self.lineEditBuscar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditBuscar.setFont(font)
        self.lineEditBuscar.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.lineEditBuscar.setClearButtonEnabled(True)
        self.lineEditBuscar.setObjectName("lineEditBuscar")
        self.gridLayout.addWidget(self.lineEditBuscar, 1, 0, 1, 1)
        self.tablaProductos = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaProductos.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.tablaProductos.setAlternatingRowColors(True)
        self.tablaProductos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablaProductos.setObjectName("tablaProductos")
        self.tablaProductos.setColumnCount(5)
        #########################
        self.labelProductos = QtWidgets.QLabel(self.tablaProductos)
        font1 = QtGui.QFont()
        font1.setPointSize(14)
        self.labelProductos.setFont(font1)
        self.labelProductos.setGeometry(QtCore.QRect(470, 150, 401, 25))
        self.labelProductos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductos.setObjectName("labelProductos")       
    
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablaProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablaProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablaProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablaProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablaProductos.setHorizontalHeaderItem(4, item)
        self.tablaProductos.horizontalHeader().setDefaultSectionSize(400)
        self.tablaProductos.horizontalHeader().setMinimumSectionSize(400)
        self.gridLayout.addWidget(self.tablaProductos, 2, 0, 1, 1)
        ventanaProductos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventanaProductos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 37))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuOperacionesProducto = QtWidgets.QMenu(self.menubar)
        self.menuOperacionesProducto.setObjectName("menuOperacionesProducto")
        ventanaProductos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventanaProductos)
        self.statusbar.setObjectName("statusbar")
        ventanaProductos.setStatusBar(self.statusbar)
        self.actionInsertar = QtWidgets.QAction(ventanaProductos)
        self.actionInsertar.setObjectName("actionInsertar")
        self.actionActualizar = QtWidgets.QAction(ventanaProductos)
        self.actionActualizar.setObjectName("actionActualizar")
        self.actionSalir = QtWidgets.QAction(ventanaProductos)
        self.actionSalir.setObjectName("actionSalir")
        self.actionABM = QtWidgets.QAction(ventanaProductos)
        self.actionABM.setObjectName("actionABM")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuOperacionesProducto.addAction(self.actionABM)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOperacionesProducto.menuAction())

        self.comboBoxProductos.currentTextChanged.connect(self.mostrarProductos)

        self.retranslateUi(ventanaProductos)
        self.actionSalir.destroyed.connect(ventanaProductos.close)
        QtCore.QMetaObject.connectSlotsByName(ventanaProductos)

        #EVENTOS
        self.actionABM.triggered.connect(self.productosABM.show)
        self.comboBoxProductos.currentTextChanged.connect(self.mostrarProductos)
        self.actionSalir.triggered.connect(self.close)
        #self.comboBoxProductos.currentText.connect(self.mostrarProductos)
        self.lineEditBuscar.textChanged.connect(self.mostrarDatosLike)
        self.tablaProductos.itemClicked.connect(self.registrarVenta)
        #self.comboBoxProductos.currentText.connect(self.mostrarProductos)
        VentanaABM.tabla = self.tablaProductos

    def retranslateUi(self, ventanaProductos):
        _translate = QtCore.QCoreApplication.translate
        ventanaProductos.setWindowTitle(_translate("ventanaProductos", "Productos"))
        self.comboBoxProductos.setItemText(0, _translate("ventanaProductos", "Productos"))
        self.comboBoxProductos.setItemText(1, _translate("ventanaProductos", "Ventas"))
        self.lineEditBuscar.setPlaceholderText(_translate("ventanaProductos", "Buscar producto por nombre  del producto"))
        item = self.tablaProductos.horizontalHeaderItem(0)
        item.setText(_translate("ventanaProductos", "Articulo"))
        item = self.tablaProductos.horizontalHeaderItem(1)
        item.setText(_translate("ventanaProductos", "Cantidad del producto en stock"))
        item = self.tablaProductos.horizontalHeaderItem(2)
        item.setText(_translate("ventanaProductos", "Precio por unidad"))
        item = self.tablaProductos.horizontalHeaderItem(3)
        item.setText(_translate("ventanaProductos", "Cantidad que va a llevar"))
        item = self.tablaProductos.horizontalHeaderItem(4)
        item.setText(_translate("ventanaProductos", "Opción"))
        self.menuArchivo.setTitle(_translate("ventanaProductos", "Archivo"))
        self.menuOperacionesProducto.setTitle(_translate("ventanaProductos", "Operaciones"))
        self.actionInsertar.setText(_translate("ventanaProductos", "Insertar"))
        self.actionActualizar.setText(_translate("ventanaProductos", "Actualizar"))
        self.actionSalir.setText(_translate("ventanaProductos", "Salir"))
        self.actionABM.setText(_translate("ventanaProductos", "ABM"))

# app = QtWidgets.QApplication(argv)
# mp = VentanaProductos()
# VentanaABM.v = mp
# mp.setupUi1(mp)
# mp.showMaximized()
# exit(app.exec_()) 

        