<!DOCTYPE html>
<html>
    <head>
        <title>Sistemas de turnos la gloria</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.5 user-scalable = no minimum-scale = 100% maximum-scale = 110%">
    <link rel="stylesheet" href="styles/index.css">
    <link rel="stylesheet" href="styles/formularioContacto.css">
    </head>
    <body id="body">
        <div id="logoMyCompany">
            <div>
                <img src="imagenes/logo.png" id="logo">
                <p id="titulo">Complejo <br>Deportivo<br>La Gloria</p>
                <img src="imagenes/atletas.png" id="atletas">
            </div>
        </div>
        <div id="parentContainer">
            <div id="futbol">
                <img src="imagenes/futbol.png" title="Reserba para la cancha de fútbol">
                <a href="formularioInscripcion.php" id="linkF">¡Hacer recerba!</a>
            </div>
            <div id="gym">
                <img src="imagenes/gym.png" title="Reserba para el gimnacio">
                <a href="formularioInscripcion.php" id="linkG">¡Hacer recerba!</a>
            </div>
            <div id="sinkSwimming">
                <img src="imagenes/swimming.png" title="Reserba para la pileta">
                <a href="formularioInscripcion.php" id="linkN">¡Hacer recerba!</a>
            </div>
            <div id="paddle">
                <img src="imagenes/paddle.png" title="Reserba para la cancha de paddle">
                <a href="formularioInscripcion.php" id="linkP">¡Hacer recerba!</a>
            </div>
        </div>
        <div id="competitions">
            <p><h1 id="tituloTorneos">Torneos</h1></p>
            <img src= "imagenes/torneos/futbol/futbol1.PNG" id="compeFutbol">
            <img src="imagenes/torneos/gym/gym1.PNG" id="compeGym">
            <img src="imagenes/torneos/natación/natación1.PNG" id="compeNatacion">
            <img src="imagenes/torneos/paddle/paddle1.PNG" id="compePaddle">
        </div>
        <footer>
            <div id="whoWeAre">
                <header id="a">¿Quienes somos?</header><br>
                <p>Somos una empresa deportiva y social que lleva más de 20 años en el rubro organizando eventos deportivos y sociales.</p>
            </div>
            <div id="weOffer">
                <header>¿Que ofrecemos?</header><br>
                <p>Profesionalismo, execelente atención, instalaciones bien equipadas y en muy buen estado.<br>Además de la posibilidad de competir en torneos a nivel provincial y nacional</p>
            </div>
            <div id="whereWeAre">
                <header>Donde nos puedes encontrar</header><br>
                <p>Nos encontramos en Av.Neustadt 183</p>
            </div>
            <div id="information">
                <header>Horarios de atención</header><br>
                <p>Lunes a Sabado<br>De 8:00 hrs a 22:00 hrs</p>
            </div>
            <div id="consultations">
                <header>Consultas</header>
                <p>Puedes consultarnos por cualquier red social o mediante el formulario que esta en el apartado <strong>Formas de Contactos</strong></p>
            </div>
            <div id="contact">
                <header>Formas de contacto</header><br>
                <p>Envianos un correo a <a href="https://mail.google.com/mail">ComplejoDeportivoLaGloria02020@gmail.com</a></p>
                <p>Llamando al celular (3777)1234567890</p>
                <p><a href="#body" id="fc">Contactar por este medio</a></p>
            </div>
        </footer>
        <div id="form">
            <form name="formularioContacto" id="formContact">
                <a href="#contact" id="salirEnlace"><img src="imagenes/x.png" id="salir"></a>
                <label id="titulo">Formulario de contacto</label>
                <input type="text" name="nombre" value="" id ="nombre1" placeholder="Ingrese su nombre" autocomplete = "on" required/>
                <input type="text" name="apellido" value="" id ="apellido1" placeholder="Ingrese su apellido" autocomplete = "on" required/>
                <input type="email" name="correo" value="" id ="correo1"placeholder="Ingrese su correo" autocomplete="on" required/>
                <br>
                <label>Motivo de contacto
                    <select name="motivo" id ="motivo1">
                    <option value="Inscrpciones">Inscripciones</option>
                    <option value="Torneos">Torneos</option>
                </select>
                </label>
                <textarea name="mensaje" rows="10" cols="20" placeholder="Escriba su mensaje" id ="mensaje1" required></textarea>
                <input type="button" name="boton" value="Enviar" id="enviarFormContac"/>
            </form>
        </div>
        <script type="text/javascript" src="scripts/jquery.js"></script>
        <script type="text/javascript" src="scripts/index.js"></script>
        <script type="text/javascript" src="scripts/seccionInformacion.js"></script>
        <script type="text/javascript" src="scripts/envioDatos.js"></script>
    </body>
</html>
