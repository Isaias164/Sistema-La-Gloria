<?php
//header('Access-Control-Allow-Origin: *');
//header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method");
//header("Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, DELETE");
//header("Allow: GET, POST, OPTIONS, PUT, DELETE");
include "peticiones.php";
switch ($_SERVER['REQUEST_METHOD']) {
    case "GET":
        if(isset($_GET["usuario"])){
            $u = $_GET["usuario"];
            $p = $_GET["pwd"];
            $d = new Consultas(array("usuario"=>$u,"pwd"=>$p));
            $mensaje = $d->obtenerIdEmpleado();
            //echo $mensaje;
            $mensaje1 = array("mensaje" => utf8_encode($mensaje)); 
            header('Content-type: application/json');
            echo json_encode($mensaje1);
        }
        //trae los deportes
        if(isset($_GET["codigo"])){
            $mensaje;
            $deporte = $_GET["codigo"];
            
            $c = new Consultas(array("codigo"=>$deporte));
            if($deporte == "p" or $deporte == "g"){
                //echo "entre en las ´piletas y el gym";
                $mensaje = $c->obtenerPiletaGym();
            }
            else {
                //echo 'fui por paddle o futbol';
                $mensaje = $c->obtenerPaddleFurbol();
            }
            //$mensaje1 = array("mensaje" => $mensaje); 
            header('Content-type: application/json');
            echo json_encode($mensaje);
            //echo json_last_error() . "<----";
        }
        if(isset($_GET["producto"])){
            if(isset($_GET["prodNombre"])){
                $nomP = $_GET["prodNombre"];
                $c = new Consultas(array("prodNombre"=>$nomP));
                $mensaje = $c->obtenerProductosConLike();
                header('Content-type: application/json');
                echo json_encode($mensaje);
            }
            else {
                $vp = $_GET["producto"];
                if($vp == "39"){
                    $mensaje = Consultas::obtenerTodosProductos();
                    //$mensaje = array("mensaje"=>$mensaje)
                    header('Content-type: application/json');
                    echo json_encode($mensaje);
                }
                else{
                    $mensaje = Consultas::obtenerProductosVendidos();
                    //$mensaje = array("mensaje"=>$mensaje)
                    header('Content-type: application/json');
                    echo json_encode($mensaje);
                }
            }
        }
        
        if(isset($_GET["recuCorreo"])){
            $correo = $_GET["recuCorreo"];
            //echo "estoy para la recuperación de la cuenta";
            $mensaje = Consultas::recuperarCuenta($correo);
            $mensaje1 = utf8_encode($mensaje);
            header('Content-type: application/json');
            echo json_encode($mensaje1);
        }
        
        if(isset($_GET["monto"])){
            $recaudado = $_GET["monto"];
            $mensaje;
            $fecha = $_GET["fecha"];
            if($recaudado == "montoProducto"){
                $mensaje = Consultas::montosRecaudados($recaudado,$fecha);
                
            }
            else {
                $mensaje = Consultas::montosRecaudados($recaudado,$fecha);
            }
            header('Content-type: application/json');
            echo json_encode($mensaje);
        }
        break;
    case "POST":
        $datos = file_get_contents('php://input');
        $solicitud = json_decode($datos, true);
        $cod1 = $solicitud["codigo"];
        //print_r($solicitud);
        //echo $cod1;
        switch ($cod1){
            case 0:
                $nomUser= $solicitud["usuario"];
                $passwUser= $solicitud["pwd"];
                $correoUser = $solicitud["gmail"];
                $nombre = $solicitud["nombre"];
                $apellido = $solicitud["apellido"];
                $direccion = $solicitud["direccion"];
                $telefono = $solicitud["telefono"];
                //echo $nomUser . " " . $passwUser . " " .$correoUser;
                $insert = new Consultas(array("usuario"=>$nomUser,"pwd"=>$passwUser,"gmail"=>$correoUser,"codigo"=>$cod1,"nombre"=>$nombre,"apellido"=>$apellido,"direccion"=>$direccion,"telefono"=>$telefono));
                $mensaje = $insert->insertar();
                $mensaje1 = array("mensaje" => utf8_encode($mensaje)); 
                header('Content-type: application/json');
                echo json_encode($mensaje1);
                break;
            case 20:
                $nom = $solicitud["nombreCliente"];
                $ape = $solicitud["apellidoCliente"];
                $deport = $solicitud["deporte"];
                $fecha = $solicitud["fecha"];
                $hora = $solicitud["hora"];
                
                if(isset($solicitud["idEmp"])){
                    $idEmp = $solicitud["idEmp"];
                    $insert = new Consultas(array("nombreCliente"=>$nom,"apellidoCliente"=>$ape,"deporte"=>$deport,"fecha"=>$fecha,"hora"=>$hora,"codigo"=>$cod1,"idEmp"=> $idEmp));
                }
                else{
                    $insert = new Consultas(array("nombreCliente"=>$nom,"apellidoCliente"=>$ape,"deporte"=>$deport,"fecha"=>$fecha,"hora"=>$hora,"codigo"=>$cod1));
                }
                
                $mensaje = $insert->insertar();
                $mensaje1 = array("mensaje" => utf8_encode($mensaje)); 
                header('Content-Type: application/json');
                echo json_encode($mensaje1);
            break;
            case 30:
                $nombre = $solicitud["nombre"];
                $precio = $solicitud["precio"];
                $precioTotal = $solicitud["precioTotal"];
                if(!isset($solicitud["idEmp"])){
                    $cant = $solicitud["cantidad"];
                    $insert = new Consultas(array("nombre"=>$nombre,"cantidad"=>$cant,"precio"=>$precio,"precioTotal"=>$precioTotal,"codigo"=>$cod1));
                    $mensaje = $insert->insertar();
                    $mensaje1 = array("mensaje" => utf8_encode($mensaje)); 
                    header('Content-type: application/json');
                    echo json_encode($mensaje1);
                }
                else{
                    $idEmpleado = $solicitud["idEmp"];
                    $cantPorEmpleado = $solicitud["cantidadVendida"];
                    $insert = new Consultas(array("idEmp"=>$idEmpleado,"cantidadVendida"=>$cantPorEmpleado,"nombre"=>$nombre,"precio"=>$precio,"precioTotal"=>$precioTotal,"codigo"=>$cod1));
                    $mensaje = $insert->insertar();
                    $mensaje1 = array("mensaje" => utf8_encode($mensaje)); 
                    header('Content-type: application/json');
                    echo json_encode($mensaje1);
                }
            break;
        }
        break;
    case "DELETE":
        $datos = file_get_contents('php://input');
        $solicitud = json_decode($datos, true);
        $nombreproducto = $_GET["nombreProducto"];
        //echo $nombreproducto;
        $c = new Consultas();
        $mensaje = $c::eliminarProducto($nombreproducto);
        header('Content-type: application/json');
        echo json_encode($mensaje);
        break;
    case "PUT":
        $datos = file_get_contents('php://input');
        $solicitud = json_decode($datos, true);
        $nombreproducto = $_GET["nombreProducto"];
        $precio = $_GET["precio"];
        //print_r($_GET);
        $c = new Consultas();
        $mensaje = $c::actualizarPrecio($nombreproducto,$precio);
        header('Content-type: application/json');
        echo json_encode($mensaje);
        break;
}
?>