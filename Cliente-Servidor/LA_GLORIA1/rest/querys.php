<?php
class Cliente{
    //("idempleado",'DADDY','YANKEE','gym','2020-11-16',21) 
    public $gym = "SELECT INSERTAR_CLIENTE_GYM(?,?,?,?,?,?);";
    public $pileta = "SELECT INSERTAR_CLIENTE_PILETA(?,?,?,?,?,?);";
    public $futbol = "SELECT INSERTAR_CLIENTE_FUTBOL(?,?,?,?,?,?);";
    public $paddle = "SELECT INSERTAR_CLIENTE_PADDLE(?,?,?,?,?,?);";
    public $parametros = "issssi";
}
class Empleado{
    //SELECT CREAR_EMPLEADO("diablito","isaiassosa250@gmail.com","1234564","Isaias","Sosa","madariaga 511","3777586321")
    public $empleado = "SELECT loggingempleados.idLogEmpleado FROM loggingempleados WHERE loggingempleados.user1 = ? AND loggingempleados.pasword = ?";
    //public $parametros = "";
    //public $seleccionar = "SELECT * FROM empleado";
}
class Logging{
    public $loging = "SELECT CREAR_EMPLEADO(?,?,?,?,?,?,?);";
    public $parametros = "sssssss";
    public $user = "SELECT loggingempleados.idLogEmpleado FROM loggingempleados WHERE loggingempleados.user1 = ? AND loggingempleados.pasword = ?;";
    public $paramUserLogeo = "ss";
    public $recuperacionContrasena = "SELECT CUENTA_RECUPERACION(?,?);";
}
class Producto{
    //inserto el producto INSERTAR_PRODUCTO("COCA COLA",2,130.00,4000)
    public $producto = "SELECT INSERTAR_PRODUCTO(?,?,?,?);";
    public $parametrosProd = "sidi";
    //ID_EMPLEADO INT(2),CANTIDAD INT(2),NOMBREP CHAR(20),PRECIOP FLOAT(4,2),PRECIOTOTALP INT(9)
    public $productoVendido = "SELECT PRODUCTO_VENDIDO(?,?,?,?,?);";
    public $paramProdVendido = "iisdi";
    public $seleccionar = "SELECT productos.nombre,productos.cantidad,productos.precioUnidad FROM productos";//,productos.precioTotal
    public $seleccionarConLike = "SELECT productos.nombre,productos.cantidad,productos.precioUnidad,productos.precioTotal FROM productos WHERE  productos.nombre LIKE ?";
    public $productosVendidos = "SELECT productos.nombre,SUM(productosvendidos.cantidadVendida),CONCAT(empleados.nombre,\" \",empleados.apellido) FROM productosvendidos JOIN productos ON productosvendidos.produc = productos.idProducto JOIN empleados ON productosvendidos.empleado = empleados.idEmpleado WHERE productosvendidos.fechaVenta = CURDATE() GROUP BY productos.nombre";
    public $eliminarProducto = "DELETE FROM productos WHERE productos.nombre = ?";
    public $actualizarPrecio = "UPDATE productos SET productos.precioUnidad = ? WHERE productos.nombre = ?";
}
class Reserbas{
    public $gym_pileta = "SELECT CONCAT(clientes.nombre,\" \",clientes.apellido) AS cliente,clientes.totalPagar,gruposreserba.hora,gruposreserba.contador,CONCAT(\"ATENDIDO POR  \",\" \",empleados.nombre,\" \",empleados.apellido) AS AtendidoPor FROM clientes 
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo 
JOIN empleados ON clientes.empleado = empleados.idEmpleado 
WHERE gruposreserba.fecha = CURDATE() AND gruposreserba.deporte = ?;";
    public $paramPiletaGym = "s";
    public $futbol = "SELECT CONCAT(clientes.nombre,\" \",clientes.apellido) AS cliente,clientes.totalPagar,canchasfutbol.idfutbol,gruposreserba.hora,CONCAT(\"ATENDIDO POR  \",\" \",empleados.nombre,\" \",empleados.apellido) AS AtendidoPor FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
JOIN canchasfutbol ON canchasfutbol.idfutbol = clientes.futbol
WHERE gruposreserba.fecha = CURDATE() AND gruposreserba.deporte = ?;";
    public $paddle = "SELECT CONCAT(clientes.nombre,\" \",clientes.apellido) AS cliente,clientes.totalPagar,canchaspaddle.idPaddle,gruposreserba.hora,CONCAT(\"ATENDIDO POR  \",\" \",empleados.nombre,\" \",empleados.apellido) AS AtendidoPor FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
JOIN canchaspaddle ON canchaspaddle.idPaddle = clientes.paddle
WHERE gruposreserba.fecha = CURDATE() AND gruposreserba.deporte = ?;";
}
class Recaudado{
    public $producto = "SELECT SUM(productos.precioUnidad) * productosvendidos.cantidadVendida FROM productosvendidos
JOIN productos on productosvendidos.produc = productos.idProducto
WHERE productosvendidos.fechaVenta = ?;";
    public $reserbas = "SELECT RECAUDADO_RESERBAS(?)";
    
}
/*
0-9 = logging
10-19 = empleado
20-29 = cliente
30-39 = producto
*/
?>








