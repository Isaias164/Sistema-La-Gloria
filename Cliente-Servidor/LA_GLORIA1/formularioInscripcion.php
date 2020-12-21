<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Formulario de inscripción</title>
        <link rel="stylesheet" href="styles/formularioInscripción.css">
        <script src = "scripts/jquery.js"></script>
    </head>
    <body>
        <div id="divServidor">
            <a href="index.php"><img src="imagenes/x.png" id="salirServidor"></a>
            <p id="pServidor"></p>
            <img src="imagenes/cara feliz.png" id="cara">
        </div>
        <form id="formInscription">
            </br>
            <a href="index.php"><img src="imagenes/x.png" id="salir"></a>
            <input type="text" name="nombre" id="nombre" value="" placeholder="Ingrese su nombre" required title="Ingresa tu nombre"/>
            <input type="text" name="apellido" id="apellido" value="" placeholder="Ingrese su apellido" required title="Ingresa tu apellido"/><br>
            <input type="date" name="fecha" id="fecha" required title="Fecha de tu reserba"/>
            <input type="number" name="hora" id="hora" value="10" min="10" max="21" step="1" title="Hora de tu reserba"/><br>
            <label>Cantidad de horas de su reserva &nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="number" name="cantHora" value="1" min = "1" max="12" required readonly/><br>
            <label id="option">Voy a pagar</label>
            <select name="formPago">
                <option>Efectivo</option>
            </select>
            <input type="button" value="Listo" id="botonEnviar"/>
        </form>
        <script type="text/javascript" src="scripts/envioDatos.js"></script>
    </body>
</html>
