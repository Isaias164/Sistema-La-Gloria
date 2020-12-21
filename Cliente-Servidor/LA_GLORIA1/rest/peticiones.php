<?php
include 'conex_bd.php';
include 'querys.php';
include 'RecuperacionCuenta.php';
include './PHPMailer/Serializacion.php';
/*
  0-9 = logging
  10-19 = empleado
  20-29 = cliente
  30-39 = producto
 */
class Consultas {
    private $idEmpleado = 1;
    //private $fecha = date('Y-m-d');
    public function __construct($parametrs = array()) {
        $this->parametro = $parametrs;
        if(isset($parametrs["idEmp"])){
           //print_r($this->parametro);
          $this->idEmpleado = $parametrs["idEmp"];
        }
        //print_r($this->parametro);
        //echo "dsdsdsds" . $this->parametro["codigo"] . "\n";
        //echo "sasasasa" . $this->parametro["fecha"];
    }
    public function insertar() {
        global $conn;
        $statement;
        //representa de que tipo son los valores del bindeo
        $param;
        //se almacena la consulta
        $q;
        //defino la query
        switch ($this->parametro["codigo"]) {
            case 0:
                $insertar = new Logging();
                $q = $insertar->loging;
                $param = $insertar->parametros;
                //$insertar1 = new Empleado();
                //$q1 = $insertar1->empleado;
                //$param1 = $insertar1->parametros;
                break;
            case 20:
                $insertar = new Cliente();
                //selecciona query
                switch ($this->parametro["deporte"]) {
                    case "gym":
                        #tomo la consulta
                        $q = $insertar->gym;
                        break;
                    case "pileta":
                        $q = $insertar->pileta;
                        break;
                    case "futbol":
                        $q = $insertar->futbol;
                        break;
                    case "paddle":
                        $q = $insertar->paddle;
                        break;
                }
                $param = $insertar->parametros;
                break;
            case 30:
                $insertar = new Producto();
                //si quiero insertar un producto
                if(!isset($this->parametro["idEmp"])){
                    $q = $insertar->producto;
                    $param = $insertar->parametrosProd;
                    //echo $q,$param . "<br>" . $this->parametro["nombre"],$this->parametro["cantidad"],$this->parametro["precio"], $this->parametro["precioTotal"];
                }
                //voy a insertar la venta de un producto
                else{
                    $q = $insertar->productoVendido;
                    $param = $insertar->paramProdVendido;
                }
                break;
        }   
        switch ($this->parametro["codigo"]) {
            case 0:
                $statement = $conn->prepare($q);
                $statement->bind_param($param,$this->parametro["usuario"], $this->parametro["gmail"], $this->parametro["pwd"],$this->parametro["nombre"], $this->parametro["apellido"], $this->parametro["direccion"], $this->parametro["telefono"]);
                break;
            case 20:
                $statement = $conn->prepare($q);
                $statement->bind_param($param,$this->idEmpleado,$this->parametro["nombreCliente"], $this->parametro["apellidoCliente"], $this->parametro["deporte"], $this->parametro["fecha"], $this->parametro["hora"]);
                break;
            case 30:
                if(!isset($this->parametro["idEmp"])){
                    $statement = $conn->prepare($q);
                    $statement->bind_param($param,$this->parametro["nombre"],$this->parametro["cantidad"],$this->parametro["precio"], $this->parametro["precioTotal"]);  
                }
                //voy a insertar la venta de un producto
                else{
                    $statement = $conn->prepare($q);
                    $statement->bind_param($param, $this->idEmpleado, $this->parametro["cantidadVendida"],$this->parametro["nombre"],$this->parametro["precio"], $this->parametro["precioTotal"]);
                }
                break;
        }
        //echo $this->idEmpleado;
        //echo $q,$param;
        $mensaje_bd;
        //intento conectarme a la bd
        if(mysqli_connect_errno() == 0){
            if($statement->execute()){
                $statement->bind_result($mensaje);
                while($statement->fetch()){
                    $mensaje_bd = $mensaje;
                    $statement->close();
                    mysqli_close($conn);
                    return $mensaje_bd;
                }
            }
        } 
    }
    
    public function obtenerIdEmpleado(){
        global $conn;
        $mensajeBD;
        $log = new Logging();
        $q = $log->user;
        $param = $log->paramUserLogeo;
        $statement = $conn->prepare($q);
        $statement->bind_param($param, $this->parametro["usuario"], $this->parametro["pwd"]);
        if(mysqli_connect_errno() == 0){
            if($statement->execute()){
                $statement->bind_result($idReserba);
                if($statement->fetch()){
                   $mensajeBD = $idReserba;
                   $statement->close();
                   mysqli_close($conn);
                   return $mensajeBD;
                }
                else{
                    return "Usuario y/o contraseña incorrecta";
                }
            }
            else{
                echo 'no se pudo ejecutar la consulta';
            }
        }
        else {
            echo 'no se pudo conectar con la bd';
        }
    }
    
    public static function recuperarCuenta($correo){
        $pasw = New RecuperacionCuenta();
        $password = $pasw->generarPassword();
        global $conn;
        $statement;
        $recu = new Logging();
        $query = $recu->recuperacionContrasena;
        #echo $query." ".$correo." ".$pwd;
        $statement = $conn->prepare($query);
        $statement->bind_param("ss",$correo,$password);
        $mensaje_bd;
        if(mysqli_connect_errno() == 0){
            if($statement->execute()){
                $statement->bind_result($mensaje);
                if($statement->fetch()){
                    $mensaje_bd = $mensaje;
                    if($mensaje == 0){
                        $email = new Email();
                        $email->envio("sosaisaias250@gmail.com", "Recuperación de cuneta - [NO CONTESTAR]", $password, ".", ".", $bandera=true);
                        //$email->envio("Recuperación de cuenta", "recuperacipon de cuenta", $mensaje, $nombre, $apellido, $bandera=true);
                        $mensaje_bd = "Su contraseña ha sido actualizada con exito.Verifique su correo";
                    }
                    else{
                        $mensaje_bd = "No fue posible actualizar su contraeña debido a que usted no se encuenta en nuestras bases de datos";
                    }
                    //echo $mensaje_bd ."<-- mensajebd";
                }
                $statement->close();
                mysqli_close($conn);
                return $mensaje_bd;
            }
            else{
                echo "No se puede ejecutar la consulta";
            }
        }
        else{
            echo 'No se puede conectar a la bd';
        }
    }
    
    public static function obtenerTodosProductos() {
        $statement;
        $row1;
        global $conn;
        $p = new Producto();
        if($resultado = mysqli_query($conn, $p->seleccionar)){
            $filas = $resultado->num_rows;
            if($filas == null){
                return 1;
            }
            else{
                while ($fila = mysqli_fetch_row($resultado)) {
                    $row1[] = $fila[0];
                    $row1[] =$fila[1];
                    $row1[] = $fila[2];
                    //$row1[] =$fila[3];
                }
                mysqli_free_result($resultado);
                mysqli_close($conn);
                return $row1;
            }
        }
        //else {
        return 1;//"No hay ningun producto cargado";
        //}
    }
    
    public static function montosRecaudados($monto,$fecha) {
        global $conn;
        $statement;
        if($monto == "montoProducto"){
            $producto = new Recaudado();
            $query = $producto->producto;
            $statement = $conn->prepare($query);
            $statement->bind_param("s",$fecha);
        }
        else{
            $reserbas= new Recaudado();
            $query = $reserbas->reserbas;
            $statement = $conn->prepare($query);
            $statement->bind_param("s",$fecha);
        }
        $mensaje_bd;
        //intento conectarme a la bd
        if(mysqli_connect_errno() == 0){
            if($statement->execute()){
                $statement->bind_result($mensaje);
                while($statement->fetch()){
                    $mensaje_bd = $mensaje;
                    $statement->close();
                    mysqli_close($conn);
                    if($mensaje_bd == null){
                        $mensaje_bd = 0;
                    }
                    return $mensaje_bd;
                }
            }
        } 
    }

    public static function obtenerProductosVendidos(){
        $statement;
        $row1;
        global $conn;
        $p = new Producto();
        $resultado = mysqli_query($conn, $p->productosVendidos);
        $fila = mysqli_fetch_row($resultado);
        if($resultado == null or $fila == null){
            return 1;//"No hay ventas realizadas";
        }
        if($resultado = mysqli_query($conn, $p->productosVendidos)){
            while ($fila = mysqli_fetch_row($resultado)) {
               $row1[] = $fila[0];
               $row1[] =$fila[1];
               $row1[] = $fila[2];
            }
            mysqli_free_result($resultado);
            mysqli_close($conn);
            return $row1;
            
        }
        else {
            return "No hay ventas realizadas";
        }
    }

    public function obtenerProductosConLike() {
        global $conn;
        $q = new Producto();
        $query = $q->seleccionarConLike;
        $statement = $conn->prepare($query);
        $valor = $this->parametro["prodNombre"];
        $valor = $valor . "%";
        $statement->bind_param("s", $valor);
        $row;
        if(mysqli_connect_errno() == 0){
            $statement->execute();
            $result = $statement->get_result();
            if($result->num_rows === 0){//$statement->execute()
                return 1;//"No hay productos con este nombre";
              }
            while($row = $result->fetch_assoc()){
                $row1[] = $row["nombre"];
                $row1[]= $row["cantidad"];
                $row1[]= $row["precioUnidad"];
                //$row1[]= $row["precioTotal"];
            }
        }
        $statement->close();
        mysqli_close($conn);
        return $row1;
    }


    public function obtenerPaddleFurbol() {
        global $conn;
        $query = new Reserbas();
        $q;
        $paddle1 = "paddle";
        $futbol1 = "futbol";
        switch ($this->parametro["codigo"]) {
            case "f":
                $q = $query->futbol;
                $statement = $conn->prepare($q);
                $statement->bind_param("s",$futbol1);
                break;
            case "pdl":
                $q = $query->paddle;
                $statement = $conn->prepare($q);
                $statement->bind_param("s",$paddle1);
                break;
        }
        $row1;// = array("mensaje"=>"");
        //$obj = new ReserbasDatos();
        if(mysqli_connect_errno() == 0){
            $statement->execute();
            $result = $statement->get_result();
            if($result->num_rows === 0){//$statement->execute()
                return "No hay reserbas hechas";
              }
            while($row = $result->fetch_assoc()){
                $row1[] = $row["cliente"];
                $row1[]= $row["totalPagar"];
                switch ($this->parametro["codigo"]) {
                    case "f":
                        $row1[] = $row["idFutbol"];
                        break;
                    case "pdl":
                        $row1[] = $row["idPaddle"];
                        break;
                }
                $row1[] = $row["hora"];
                $row1[]= $row["AtendidoPor"];
            }
            //print_r($row1);
            $statement->close();
            mysqli_close($conn);
            return $row1;
        }
        else {
             echo "ubo un error";// . $statement->errno . $statement->error;
           }    
    }

    public function obtenerPiletaGym(){
        global $conn;
        $statement;
        $query = new Reserbas();
        $q = $query->gym_pileta;
        $param = $query->paramPiletaGym;
        $statement = $conn->prepare($q); //$conn->prepare($q);
        //echo $this->idEmpleado;
        $gym = "gym";
        $pileta = "pileta";
        switch ($this->parametro["codigo"]) {
            case "g":
                $statement->bind_param($param, $gym);
                break;
            case "p":
                $statement->bind_param($param, $pileta);
                break;
        }
        $row1;// = array("mensaje"=>"");
        //$obj = new ReserbasDatos();
        if(mysqli_connect_errno() == 0){
            $statement->execute();
            $result = $statement->get_result();
            if($result->num_rows === 0){//$statement->execute()
                return "No hay reserbas hechas";
              }
            while($row = $result->fetch_assoc()){
                $row1[] = $row["cliente"];
                $row1[]= $row["totalPagar"];
                $row1[] = $row["hora"];
                $row1[] = $row["contador"];
                $row1[]= $row["AtendidoPor"];
            }
            //print_r($row1);
            $statement->close();
            mysqli_close($conn);
            return $row1;
        }
        else {
             echo "ubo un error";// . $statement->errno . $statement->error;
           }    
        }
        
        public static function eliminarProducto($nombre){
            global $conn;
            $mensaje;
            $q = new Producto();
            $query = $q->eliminarProducto;
            $statement = $conn->prepare($query);
            $statement->bind_param("s", $nombre);
            if(mysqli_connect_errno() == 0){
                if($statement->execute()){
                    $filasAfectadas = $statement->affected_rows;
                    //echo $filasAfectadas ."----";
                    if($filasAfectadas >= 1){
                        $mensaje = "El producto ".$nombre." se ha eliminado satisfactoriamente";
                    }
                    else{
                        $mensaje = "El producto ".$nombre." no pudo eliminarse, porque no exite en la Base de Datos";
                    }
                }
            }
            $statement->close();
            mysqli_close($conn);
            return $mensaje;
        }
        public static function actualizarPrecio($nombre,$precio) {
            global $conn;
            $mensaje;
            $q = new Producto();
            $query = $q->actualizarPrecio;
            $statement = $conn->prepare($query);
            $statement->bind_param("is",$precio,$nombre);
            if(mysqli_connect_errno() == 0){
                if($statement->execute()){
                    $filasAfectadas = $statement->affected_rows;
                    //echo $filasAfectadas ."----";
                    if($filasAfectadas >= 1){
                        $mensaje = "Ha actualizado el precio del producto ".$nombre;
                    }
                    else{
                        $mensaje = "No se ha podido actualizar el precio del producto ".$nombre." ,porque no exite en la Base de Datos";
                    }
                }
            }
            $statement->close();
            mysqli_close($conn);
            return $mensaje;
        }
} 
    
?>
