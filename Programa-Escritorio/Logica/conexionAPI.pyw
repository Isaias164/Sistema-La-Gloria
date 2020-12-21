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
        #r = get(ConsultasApi.path,params=self.parametro)
        #datos = r.json()
        #print(datos)
        #return datos["mensaje"]
    
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


#a = ConsultasApi(parametrosConsulta={"codigo":"f"})
#b = a.obtenerCanchas()
#print(b)


#a = ConsultasApi(parametrosConsulta={"recuCorreo":"sosaisaias250@gmail.com"})
#b = a.recuperarCuenta()
#print(b.decode("utf-8"))

#a = ConsultasApi()
#b = a.eliminarProducto("Dirubin")
#print(b)



#a = ConsultasApi(parametrosConsulta ={"monto":"montoProductor","fecha":"12-12-2020"})
#b = a.montos()
#print(b)

#a = ConsultasApi(parametrosConsulta ={"nombre":"Coquito","precio":22,"precioTotal":222,"cantidad":33,"codigo":30})
#b = a.insertarProducto()
#print(b)

#a = ConsultasApi(parametrosConsulta = {"usuario":"ISAIAS","pwd":"12345678"})
#print(a.validarUsuario())
#with open("idEmpleado","rb") as f:
#    a = load(f)
#    print(a)
#a = ConsultasApi(parametrosConsulta = {"codigo":0,"usuario":"Lebron","pwd":"1234567aa","gmail":"sosaisaihghs@gmail.com","nombre":"Stanislao","apellido":"Sosanb","direccion":"colon 511","telefono":"37775869321"})
#a.crearEmp()


#a = ConsultasApi(parametrosConsulta = {"producto":39})
#b = a.obtenerProductos()
#print(b)


# c = 0
# for i in b:
#     print(i,"\r")
#     c += 1
#     if(c == 5):
#         print("======================================")
#         c = 0
#for i in range(len(b)):
#   print(b[i])
#a = ConsultasApi(parametrosConsulta={"nombreCliente":"isaisas","apellidoCliente":"sosaosa","deporte":"gym","fecha":"2020-12-11","hora":20,"idEmp":1,"codigo":20})
#print(a.reserbas())