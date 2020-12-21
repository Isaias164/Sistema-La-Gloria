var seleccion = document.querySelector("select");
var form = document.getElementById("formInscription");
var banco = document.getElementById("cuentaBancaria");

setTimeout(mostrarMensaje,"3000");
seleccion.addEventListener("change",obtenerOpcion);

function mostrarMensaje(){
    alert("En la casilla fecha debe ingresar el día que quiere hacer una reserva \ny en la casilla horario debe ingresar el horario en el que podra disponer de la canchas,gimnasios o piletas.");
}

function obtenerOpcion(){
    if(seleccion.value == "Efectivo( en recepción)"){
        banco.style.display = "none";
        form.style.height = "270px";
    }
    else{
        banco.style.display = "block";
        form.style.height = "400px";
    }
}