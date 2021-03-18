$(function(){
   $("#botonEnviar").on("click", function () {
       $("form").css("display","none");
    const deporte = localStorage.getItem("deporte");
    var h = $("#hora").val();
    localStorage.removeItem('deporte');
    //alert(JSON.stringify({nombreCliente:$("#nombre").val(),apellidoCliente:$("#apellido").val(),deporte:deporte,fecha:$("#fecha").val(),hora:parseInt(h,10),codigo:20}));
    //prompt("ds",JSON.stringify({nombreCliente:$("#nombre").val(),apellidoCliente:$("#apellido").val(),deporte:deporte,fecha:$("#fecha").val(),hora:parseInt(h,10),codigo:20}));
    $.ajax({
        type: "post",
        url: 'http://localhost:8080/LA_GLORIA1/rest/restfull.php',
        dataType: "json",
        data:JSON.stringify({nombreCliente:$("#nombre").val(),apellidoCliente:$("#apellido").val(),deporte:deporte,fecha:$("#fecha").val(),hora:parseInt(h,10),codigo:20})}).
        done(function(datos) {
            var cadena = datos.mensaje;
            var palabra = "SU";
            var posiscion = cadena.indexOf(palabra);
            if(posiscion !== -1){
                $("#divServidor").css("display","block");
                $("#pServidor").append(datos.mensaje);
            }
            else{
                $("#divServidor").css("display","block");
                $("#divServidor").css("background-color","red");
                $("#pServidor").append(datos.mensaje);
                $("#cara").attr("src","imagenes/cara triste.png");
            
            }
        }).
        fail(function (xhr, textStatus, error) {
            alert("algo salio mal");
            //alert(xhr);
            //alert(textStatus);
            //alert(error);
        });
    });
    
    $("#enviarFormContac").on("click",function() {
       //alert($("#formContact").serialize());
       $.ajax({
       type:"post",
       dataType:"json",
       url:"http://localhost:8080/LA_GLORIA1/rest/PhpMailer/Conexion.php",
       data:JSON.stringify({correo:$("#correo1").val(),motivo:$("#motivo1").val(),mensaje:$("#mensaje1").val(),nombre:$("#nombre1").val(),apellido:$("#apellido1").val()})
    }).done(function(datos1){
       $("#formContact").css("display","none");
       alert(datos1.mensaje);
    }).
    fail(function(xhr, textStatus, error) {
        alert("Ocurrio un error");
        alert(xhr);
        alert(textStatus);
        alert(error);
    }); 
});
});