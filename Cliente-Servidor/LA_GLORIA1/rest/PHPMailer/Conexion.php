<?php
include './Serializacion.php';
class FormularioContacto {
    function __construct($nombre, $apellido, $correo, $motivo, $mensaje) {
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->correo = $correo;
        $this->motivo = $motivo;
        $this->mensaje = $mensaje;
    }
}

//$enviarDatos = new FormularioContacto($_POST["nombre"], $_POST["apellido"], $_POST["correo"], $_POST["motivo"], $_POST["mensaje"]);
//print $enviarDatos->nombre . ' ' . $enviarDatos->apellido . ' quiere contactar contigo  por un motivo ' . $enviarDatos->motivo . ' </br>';
//print 'El mensaje es el siguiente: </br> <h3>' . $enviarDatos->mensaje . '</h3></br>';
//print '</br>Puedes contactarlo con el siguiente correo <a href = "https://mail.google.com/mail/">' . $enviarDatos->correo . '</a>';
//$obj1 = new Serializacion($_POST["nombre"] . $_POST["apellido"]);
//$obj1->serializar($enviarDatos);
//$obj1->deserializar();

$datos1 = file_get_contents('php://input');
$solicitud = json_decode($datos1, true);
//print_r($solicitud);
$e = new Email();
$rep = $e->envio($solicitud["correo"],$solicitud["motivo"],$solicitud["mensaje"],$solicitud["nombre"],$solicitud["apellido"]);
$a = array("mensaje"=> Email::$resultado);
header('Content-Type: application/json');
echo json_encode($a);
//echo json_last_error();
?>