#empleado
SELECT CREAR_EMPLEADO("S0mbr4","isaiassosa100@gmail.com","12345678","Isaias","Sosa","madariaga 511","3777432243")

#canchas y otros
SELECT INSERTAR_CLIENTE_GYM(1,'Isaias','sosa','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Arun','Play','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Ronnie','Coleman','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Daddy','Yankee','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Jay','Cutler','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Lebron','James','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Angel','Di Maria','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Dwayne','Jhonson','gym','2020-11-23',10);
SELECT INSERTAR_CLIENTE_GYM(1,'Vin','Diesel','gym','2020-11-23',15);
SELECT INSERTAR_CLIENTE_GYM(1,'Peter','Parquer','gym','2020-11-23',16);

SELECT INSERTAR_CLIENTE_PILETA(1,'Michael','Felps','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Michael','Jordan Jr','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Isaias','Saucedo','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Jesica','Alba','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Ema','Whatson','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Scarlet','Jhojanson','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Cristina','Olson','pileta','2020-11-23',21);
SELECT INSERTAR_CLIENTE_PILETA(1,'Jhon','Whick','pileta','2020-11-22',20);
SELECT INSERTAR_CLIENTE_PILETA(1,'Jason','Stahan','pileta','2020-11-22',21);

SELECT INSERTAR_CLIENTE_FUTBOL(1,'Lionel','Messi','fútbol','2020-11-24',10); 
SELECT INSERTAR_CLIENTE_FUTBOL(1,'Diego','Maradona','fútbol','2020-11-24',14); 
SELECT INSERTAR_CLIENTE_FUTBOL(1,'Diego','Maradona','fútbol','2020-11-24',14); 

SELECT INSERTAR_CLIENTE_PADDLE(1,'Novack','Yocobich','paddle','2020-11-25',20); 
SELECT INSERTAR_CLIENTE_PADDLE(1,'Rafael','Nadal','paddle','2020-11-26',20); 
SELECT INSERTAR_CLIENTE_PADDLE(1,'Novack','Yocobich','paddle','2020-11-25',20); 
SELECT INSERTAR_CLIENTE_PADDLE(1,'Rafael','Nadal','paddle','2020-11-26',20); 

#productos
INSERT INTO productos SET productos.nombre = "Pepsi",productos.cantidad = 50,productos.precioUnidad=130;
INSERT INTO productos SET productos.nombre = "Agua Mineral",productos.cantidad = 10,productos.precioUnidad=80;
INSERT INTO productos SET productos.nombre = "Acuarius",productos.cantidad = 40,productos.precioUnidad=65;
INSERT INTO productos SET productos.nombre = "Gatorade",productos.cantidad = 100,productos.precioUnidad=130;
INSERT INTO productos SET productos.nombre = "Fanta",productos.cantidad = 25,productos.precioUnidad=160;
INSERT INTO productos SET productos.nombre = "Coca-cola",productos.cantidad = 15,productos.precioUnidad=110;
INSERT INTO productos SET productos.nombre = "Citrus",productos.cantidad = 10,productos.precioUnidad=90;
INSERT INTO productos SET productos.nombre = "Agua saborizada",productos.cantidad = 10,productos.precioUnidad=50;
INSERT INTO productos SET productos.nombre = "Speed",productos.cantidad = 18,productos.precioUnidad=35;
INSERT INTO productos SET productos.nombre = "Soda",productos.cantidad = 15,productos.precioUnidad=80;
INSERT INTO productos SET productos.nombre = "Pepsi en lata",productos.cantidad = 10,productos.precioUnidad= 50;
INSERT INTO productos SET productos.nombre = "Coca-cola en lata",productos.cantidad = 10,productos.precioUnidad=55;
INSERT INTO productos SET productos.nombre = "Sprite",productos.cantidad = 60,productos.precioUnidad=125;

#productos vendidos
PRODUCTOVENDIDO(1,1,1);
PRODUCTOVENDIDO(1,2,5);
PRODUCTOVENDIDO(1,2,6);
PRODUCTOVENDIDO(1,3,7);
PRODUCTOVENDIDO(1,4,2);
PRODUCTOVENDIDO(1,5,3);
PRODUCTOVENDIDO(1,12,3);
PRODUCTOVENDIDO(1,11,4);
PRODUCTOVENDIDO(1,13,5);
PRODUCTOVENDIDO(1,6,5);
PRODUCTOVENDIDO(1,7,1);
PRODUCTOVENDIDO(1,8,6);
PRODUCTOVENDIDO(1,9,1);
PRODUCTOVENDIDO(1,10,2);
PRODUCTOVENDIDO(1,11,2);
PRODUCTOVENDIDO(1,2,3);
PRODUCTOVENDIDO(1,9,1);
PRODUCTOVENDIDO(1,2,1);
PRODUCTOVENDIDO(1,4,4);
PRODUCTOVENDIDO(1,4,2);
PRODUCTOVENDIDO(1,3,1);
PRODUCTOVENDIDO(1,13,5);
PRODUCTOVENDIDO(1,11,2);
PRODUCTOVENDIDO(1,10,3);
PRODUCTOVENDIDO(1,10,2);
PRODUCTOVENDIDO(1,1,1);
PRODUCTOVENDIDO(1,2,5);
PRODUCTOVENDIDO(1,2,6);
PRODUCTOVENDIDO(1,3,7);
PRODUCTOVENDIDO(1,4,2);
PRODUCTOVENDIDO(1,5,3);
PRODUCTOVENDIDO(1,12,3);
PRODUCTOVENDIDO(1,11,4);
PRODUCTOVENDIDO(1,13,5);
PRODUCTOVENDIDO(1,6,5);
PRODUCTOVENDIDO(1,7,1);
PRODUCTOVENDIDO(1,8,6);
PRODUCTOVENDIDO(1,9,1);
PRODUCTOVENDIDO(1,10,2);
PRODUCTOVENDIDO(1,11,2);
PRODUCTOVENDIDO(1,2,3);
PRODUCTOVENDIDO(1,9,1);
PRODUCTOVENDIDO(1,2,1);
PRODUCTOVENDIDO(1,4,4);
PRODUCTOVENDIDO(1,4,2);
PRODUCTOVENDIDO(1,3,1);
PRODUCTOVENDIDO(1,13,5);
PRODUCTOVENDIDO(1,11,2);
PRODUCTOVENDIDO(1,10,3);
PRODUCTOVENDIDO(1,10,2);

#DEBE MODIFICAR LAS FECHAS 
#TRAIGO LAS RESERVAS DEL DIA DE GYM
SELECT clientes.nombre,clientes.apellido,clientes.totalPagar,gruposreserba.hora,gruposreserba.contador FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
WHERE gruposreserba.fecha = CURDATE() AND empleados.idEmpleado = 1 AND gruposreserba.deporte = "gym"
#TRAIGO LAS RESERVAS DEL DIA DE LA PILETA
SELECT clientes.nombre,clientes.apellido,clientes.totalPagar,gruposreserba.hora,gruposreserba.contador FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
WHERE gruposreserba.fecha = CURDATE() AND empleados.idEmpleado = 1 AND gruposreserba.deporte = "pileta"
#TRAIGO LAS RESERVAS DEL DIA DE LAS CANCHAS DE FUTBOL
SELECT clientes.nombre,clientes.apellido,clientes.totalPagar,canchasfutbol.idfutbol,gruposreserba.hora FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
JOIN canchasfutbol ON canchasfutbol.idfutbol = clientes.futbol
WHERE gruposreserba.fecha = CURDATE() AND empleados.idEmpleado = 1 AND gruposreserba.deporte = "futbol"
#TRAIGO LAS RESERVAS DEL DIA DE LAS CANCHAS DE PADDLE
SELECT clientes.nombre,clientes.apellido,clientes.totalPagar,canchaspaddle.idPaddle,gruposreserba.hora FROM clientes
JOIN gruposreserba ON clientes.grupo = gruposreserba.idGrupo
JOIN empleados ON clientes.empleado = empleados.idEmpleado
JOIN canchaspaddle ON canchaspaddle.idPaddle = clientes.paddle
WHERE gruposreserba.fecha = CURDATE() AND empleados.idEmpleado = 1 AND gruposreserba.deporte = "paddle"

#OBTIENE TODOS LOS PRODUCTOS VENDIDOS DEL DIA POR EL EMPLEADO DE TURNO
SELECT productos.nombre,productos.cantidad,productos.precioUnidad,empleados.nombre,empleados.apellido FROM productos
JOIN empleados ON productos.emp = empleados.idEmpleado
WHERE productos.fechaVenta = CURDATE() AND empleados.idEmpleado = 1

#TARIGO LAS VENTAS DEL BAR VENDIDAS POR EL EMPLEADO DE TURNO
SELECT empleados.nombre,empleados.apellido,productos.nombre,productos.precioUnidad,productosvendidos.cantidadVendida FROM empleados
JOIN productosvendidos ON productosvendidos.empleado = empleados.idEmpleado 
JOIN productos ON productosvendidos.produc = productos.idProducto
WHERE productosvendidos.fechaVenta = curdate() AND empleados.idEmpleado = 1
