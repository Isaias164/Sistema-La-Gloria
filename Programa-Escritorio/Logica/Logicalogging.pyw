from PyQt5 import QtWidgets,QtCore, QtGui
from pickle import load
from hashlib import sha224
import re

try:
    from Logica.conexionAPI import ConsultasApi
    #print("modulo importado")
except Exception as ff:
    #print(f"El modulo no se puede importar{f}")
    pass


class LogicaLog(QtWidgets.QMainWindow):
    #ventana del formulario logging
    ventanaPadre = None
    #mi ventana principal
    menuPrincipal = None
    tabla = None
    deporte = None
    labelReserba = None

    @staticmethod
    def ocultarLabel():
        LogicaLog.labelReserba.hide()

    @staticmethod
    def mostrarLabel(mensaje):
        LogicaLog.labelReserba.setText(mensaje)
        LogicaLog.labelReserba.show()

    @staticmethod
    def cargarDatos():
        reserba = LogicaLog.deporte
        if(reserba == "Fútbol"):
            reserba = "f"
        elif(reserba == "Natación"):
            reserba = "p"
        elif(reserba == "Gimnasio"):
            reserba = "g"        
        else:
            reserba = "pdl"

        datos = ConsultasApi(parametrosConsulta={"codigo":reserba})
        reserbas = datos.obtenerCanchas()
        if(reserbas[0] in ("N","n")):
            LogicaLog.tabla.clearContents()
            LogicaLog.tabla.setRowCount(0)
            #LogicaLog.labelReserba.setText("No hay reserbas realizadas")
            LogicaLog.mostrarLabel(reserbas)
            #QtWidgets.QMessageBox.about(LogicaLog.menuPrincipal,"Notificación",reserbas)
        else:
            LogicaLog.ocultarLabel()
            LogicaLog.tabla.clearContents()
            filas = (len(reserbas)//5)
            LogicaLog.tabla.setRowCount(filas)
            LogicaLog.tabla.setColumnCount(5)
            dato = 0
            for i in range(filas):
                for col in range(5):
                    datos = QtWidgets.QTableWidgetItem(str(reserbas[dato]))
                    datos.setTextAlignment(QtCore.Qt.AlignHCenter)
                    datos.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    LogicaLog.tabla.setItem(i,col,datos)
                    dato += 1

    def verificarUC(self,usuario,contrasena):
        valido = ConsultasApi(parametrosConsulta = {"usuario":sha224(bytes(usuario,encoding="utf-8")).hexdigest(),"pwd":sha224(bytes(contrasena,encoding="utf-8")).hexdigest()})
        if(valido.validarUsuario()):
            LogicaLog.ventanaPadre.close()
            #aca iria el futbol,gym,pileta,paddle
            LogicaLog.menuPrincipal.showMaximized()
            LogicaLog.cargarDatos()
        else:
           QtWidgets.QMessageBox.about(LogicaLog.ventanaPadre,"Advertencia","Usuario y/o Contraseña incorrectos")
    
    def mostrarContras(self,pwd,check):
        if(check.isChecked() == True):
            pwd.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            pwd.setEchoMode(QtWidgets.QLineEdit.Password)

class Verificaciones:
    def verificarTextoVacio(self,argv,limpiar=False):
        if(limpiar):
            for objetoLine in range(len(argv)):
                argv[objetoLine].clear()
        else:
            for objetoLine in range(len(argv)):
                if argv[objetoLine].text() == "":
                    return False
            return True

    def verificarNumero(self,numero):
        try:
            int(numero)
            return True
        except:
            return False

    def correoValido(self,correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if(re.match(expresion_regular, correo) is not None):
            r = r"@"
            cantArroba = re.findall(r,correo)
            return len(cantArroba) == 1
        return False

    def verificarCampoNumerico(self,cantidad,precio,precioTotal):
        try:
            int(cantidad)
            float(precio)
            float(precioTotal)
            return True
        except:
            return False#cantidad + " no es un valor numerico"

class MetodosPost():
    def crearEmpleado(self,datos):
        obj = ConsultasApi(parametrosConsulta = datos)
        msg = obj.crearEmp()
        return msg
    
    def hacerReserba(self,nombre,apellido,fecha,hora,deporte):
        emp = None
        with open("Logica\idEmpleado","rb") as r:
            emp = load(r)
        datos=ConsultasApi(parametrosConsulta={"nombreCliente":nombre,"apellidoCliente":apellido,"fecha":fecha,"hora":int(hora),"deporte":deporte,"idEmp":emp,"codigo":20})
        mensaje = datos.reserbas()
        return mensaje
    

    #el precio total es precio por unitario del producto * la cantidad que lleva de ese producto
    def insertarProduct(self,nombre,precio,pTotal,cant):
        obj = ConsultasApi(parametrosConsulta={"nombre":nombre,"precio":precio,"precioTotal":pTotal,"cantidad":cant,"codigo":30})
        msg = obj.insertarProducto()
        return msg
    
    def insertarVentaRealizada(self,nombre,cantidadVendida,preciounidad,precioTotal):
        with open("Logica\idEmpleado","rb") as r:
            emp = load(r)
        consulta = ConsultasApi(parametrosConsulta={"nombre":nombre,"precio":float(preciounidad),"precioTotal":precioTotal,"cantidadVendida":cantidadVendida,"idEmp":emp,"codigo":30})
        mensaje = consulta.registrarVenta()
        return mensaje
        

class Grillas:
    label1 = None
    mensajeLabel = ""
    
    @staticmethod
    def ocultarLabel():
        Grillas.label1.hide()

    @staticmethod
    def mostrarLabel():
        Grillas.label1.setText(Grillas.mensajeLabel)
        Grillas.label1.show()

    def traerProductos(self,tabla,conLike = False,palabra = None):
        if(conLike):
            consulta = ConsultasApi(parametrosConsulta={"producto":38,"prodNombre":palabra})
        else:
            consulta = ConsultasApi(parametrosConsulta={"producto":39})
        datos = consulta.obtenerProductos()
        if(datos == 1):
            Grillas.mostrarLabel()
            tabla.setHorizontalHeaderLabels(("Articulo","Cantidad","Precio por unidad","Cantidad que va a llevar","Opción"))
            tabla.setRowCount(0)
        else:
            Grillas.ocultarLabel()
            filas = len(datos)//3
            tabla.setRowCount(filas)
            tabla.setColumnCount(5)
            tabla.setHorizontalHeaderLabels(("Articulo","Cantidad","Precio por unidad","Cantidad que va a llevar","Opción"))
            col1 = 0
            for i in range(filas):
                for col in range(3):
                    datos1 = QtWidgets.QTableWidgetItem(str(datos[col1]))
                    datos1.setTextAlignment(QtCore.Qt.AlignHCenter)
                    datos1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    tabla.setItem(i,col,datos1)
                    col1 +=1
                datos1 = QtWidgets.QTableWidgetItem("1")
                datos1.setTextAlignment(QtCore.Qt.AlignHCenter)
                datos1.setTextAlignment(QtCore.Qt.AlignHCenter)
                datos2 = QtWidgets.QTableWidgetItem("Vender este producto")
                datos2.setTextAlignment(QtCore.Qt.AlignHCenter)
                datos2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                tabla.setItem(i,3,datos1)
                tabla.setItem(i,4,datos2)

    def traerVentasRealizadasDelDia(self,tabla):
        consulta = ConsultasApi(parametrosConsulta={"producto":44})
        #Lo que en realidad estoy obteniendo es los productos vendidos
        datos = consulta.obtenerProductos()
        if(datos == 1):
            tabla.setHorizontalHeaderLabels(("Nombre del Producto","Cantidad Vendida","Empleado que Vendio el producto"))
            tabla.setRowCount(0)
            Grillas.mostrarLabel()
        else:
            filas = len(datos)//3
            tabla.setRowCount(filas)
            tabla.setColumnCount(3)
            tabla.setHorizontalHeaderLabels(("Nombre del Producto","Cantidad Vendida","Empleado que Vendio el producto"))
            col1 = 0
            for i in range(filas):
                for col in range(3):
                    datos1 = QtWidgets.QTableWidgetItem(str(datos[col1]))
                    datos1.setTextAlignment(QtCore.Qt.AlignHCenter)
                    datos1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    tabla.setItem(i,col,datos1)
                    col1 += 1


class Montos:
    def monto(self,produc_reserba,fecha):
        consulta = ConsultasApi(parametrosConsulta={"monto":produc_reserba,"fecha":fecha})
        mensaje = consulta.montos()
        return mensaje


class MetodosPut:
    def actualizarPrecio(self,nombre,precio):
        actualizar = ConsultasApi()
        msg = actualizar.actualizarPrecio(nombre,precio)
        return msg

class MetodosDelete:
    def eliminarProducto(self,producto):
        eliminar = ConsultasApi()
        msg = eliminar.eliminarProducto(producto)
        return msg

class RecuperacionCorreo:
    def recuCorreo(self,correo):
        confirmacion = ConsultasApi(parametrosConsulta={"recuCorreo":correo})
        resp = confirmacion.recuperarCuenta()
        return resp