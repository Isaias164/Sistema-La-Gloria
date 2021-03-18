<?php

class Serializacion {

    function __construct($path) {
        $this->path = $path . ".json";
    }

    public function serializar($objeto) {
        if (file_exists($this->path)) {
            $file = fopen($this->path, "a");
            fwrite($file, json_encode($objeto));
        } else {
            $file = fopen($this->path, "w");
            fwrite($file, json_encode($objeto));
        }
        fclose($file);
        //print "</br>archivo serializado con exito";
    }

    public function deserializar() {
        if (file_exists($this->path)) {
            $f = fopen($this->path, "r");
            $json = fread($f, filesize($this->path));
            $obj = json_decode($json);
            fclose($f);
            //print "archivo deserializado con exito";
            //print "</br></br>" . $json;
        }
    }

}

class Email {
    public  static $resultado;
    function envio($from1,$motivo,$mensaje,$nombre,$apellido,$bandera = false) {
//        $header = "MIME.Version:1.0" . "\r\n";
//        $header = "From:Isaias<sosaisaias250@gmail.com>"."\r\n";
//        $header = "Content-type:text/html;charset=iso-8859-1"."\r\n";
        require 'PHPMailerAutoload.php';

        $mail = new PHPMailer;
        $mail->SMTPDebug = 0;//2                                           /* Enable verbose debug output */

        $mail->isSMTP();                                                /* Set mailer to use SMTP */
        $mail->Host = 'smtp.gmail.com';                                 /* Specify main and backup SMTP servers */
        $mail->SMTPAuth = true;                                         /* Enable SMTP authentication */
        $mail->Username = 'ComplejoDeportivoLaGloria02020@gmail.com';//"La Gloria2020"                        /* SMTP username */
        $mail->Password = "1234567890ABCDEFG";                             /* SMTP password */
        $mail->SMTPSecure = 'tls';                                      /* Enable TLS encryption, 'ssl' also accepted */
        $mail->Port = 587;                                              /* TCP port to connect to */
        $mail->Helo = 'localhost';                                      /* Permite usar EHLO / HELO */
        $mail->Hostname = 'gmail.com';                                  /* Permite usar un hostname */
        
        $mail->setFrom("ComplejoDeportivoLaGloria02020@gmail.com",$nombre." " . $apellido);//$from1,$nombre." " . $apellido);
        //$mail->From = $from1;/"ComplejoDeportivoLaGloria02020@gmail.com";//$from; seria el correo de la otra persona                              /* Correo Gmail */
        //$mail->FromName = $nombre." " . $apellido;                               /* Nombre de usuario Gmail */
        if($bandera){
            $mail->addAddress($from1);
        }
        else{
            $mail->addAddress("ComplejoDeportivoLaGloria02020@gmail.com", 'Isaias Sosa');     /* Add a recipient / correo de destino */
        
        }
        // $mail->addAddress('ellen@example.com');                      /* Name is optional */
        // $mail->addCC('cc@example.com');
        // $mail->addBCC('bcc@example.com');

        // $mail->addAttachment('/var/tmp/file.tar.gz');                /* Add attachments / agregar un archivo*/
        // $mail->addAttachment('/tmp/image.jpg', 'new.jpg');           /* Optional name */
        //$mail->isHTML(true);         
        /* Set email format to HTML / Comentar para texto plano */
        $mail->Subject = $motivo;    /* Asunto */
        if($bandera){
            $mail->Body = "Esta es su nueva contraseña para recuperar su usuario en el sistema la gloria es: \n\n" . $mensaje;
        }
        else{
            $mail->Body = $mensaje . "\nMi correo de contacto es: " . $from1;      /* Lo que se mostrará en el mensaje */
        }
        if(!$mail->send()) {
          //echo 'Mailer Error: ' . $mail->ErrorInfo;
          Email::$resultado = "No se ha podido enviar el mail";
        } else {
          //echo 'Message has been sent';
          Email::$resultado = "El email se ha enviado correctamente";
        }
    }
}

?>
