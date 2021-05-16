# -*- coding: utf-8 -*-
from requests import get,post,delete,put
from pickle import dump,load,loads
#from json import dumps

class ConsultasApi:
    path = "http://localhost:8080/LA_GLORIA1/rest/restfull.php"

    def __init__(self,parametrosConsulta = None):
        self.parametro = parametrosConsulta

    def postApi(self):
        r = post(ConsultasApi.path,json=self.parametro)
        datos = r.json()
        return datos["mensaje"]

    def getApi(self):
        r = get(ConsultasApi.path,params=self.parametro)
        datos = r.json()
        return datos


    def validarUsuario(self):
        r = get(ConsultasApi.path,params=self.parametro)
        datos = r.json()
        try:
            msj = int(datos["mensaje"])
            with open("Logica\idEmpleado","wb") as d:
                dump(msj,d)
            return True
        except Exception as d:
            #print(d)
            return False

    def crearEmp(self):
        resultado = self.postApi()
        return resultado
    
    def obtenerCanchas(self):
        resultado = self.getApi()
        return resultado
    
    def reserbas(self):
        resultado = self.postApi()
        return resultado

    def insertarProducto(self):
        resultado = self.postApi()
        return resultado
    
    def obtenerProductos(self):
        r = get(ConsultasApi.path,params=self.parametro)
        datos = r.json()
        return datos#["mensaje"]
    
    def registrarVenta(self):
        resultado = self.postApi()
        return resultado

    def montos(self):
        result = self.getApi()
        return result

    def actualizarPrecio(self,nombre,precio):
        result = put(ConsultasApi.path + "?"+"nombreProducto="+nombre+"&precio="+precio)
        resultado = result.json()
        return resultado
    
    def eliminarProducto(self,nombre):
        result = delete(ConsultasApi.path + "?"+"nombreProducto="+nombre)
        resultado = result.json()
        return resultado
    
    def recuperarCuenta(self):
        result = self.getApi()
        return result
