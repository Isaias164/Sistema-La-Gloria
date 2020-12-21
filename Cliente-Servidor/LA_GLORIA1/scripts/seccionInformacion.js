$("#fc").on("click", mostrarForm);

function mostrarForm() {
    $("#formContact").css("display", "block");
}
var divs = $("footer > div");
var headers = $("footer > div > header");
var ps = $("footer > div > p");
var pContact = $("#contact > p");
var pconsultas = $("#consultations > p");

$(divs[0]).on("mouseover", function () {
    mover(0);
});
$(divs[0]).on("mouseout", function () {
    volverLugar(0);
});

$(divs[1]).on("mouseover", function () {
    mover(1);
});
$(divs[1]).on("mouseout", function () {
    volverLugar(1);
});

$(divs[2]).on("mouseover", function () {
    mover(2);
});
$(divs[2]).on("mouseout", function () {
    volverLugar(2);
});

$(divs[3]).on("mouseover", function () {
    mover(3);
});
$(divs[3]).on("mouseout", function () {
    volverLugar(3);
});

$(divs[4]).on("mouseover", function () {
    mover(4);
});
$(divs[4]).on("mouseout", function () {
    volverLugar(4);
});

$(divs[5]).on("mouseover", function () {
    mover(5);
});
$(divs[5]).on("mouseout", function () {
    volverLugar(5);
});


function mover(op) {
    if (op == 0) {
        $(headers[0]).css("fontSize","20px");
        $(headers[0]).css("color","white");
        $(headers[0]).css("top","4px");
        $(ps[0]).css("display","block");
    }
    else if (op == 1) {
        $(headers[1]).css("fontSize","20px");
        $(headers[1]).css("color","white");
        $(headers[1]).css("top","4px");
        $(ps[1]).css("display","block");
    }
    else if (op == 2) {
        $(headers[2]).css("fontSize","20px");
        $(headers[2]).css("color","white");
        $(headers[2]).css("top","4px");
        $(ps[2]).css("display","block");
    }
    else if (op == 3) {
        $(headers[3]).css("fontSize","20px");
        $(headers[3]).css("color","white");
        $(headers[3]).css("top","4px");
        $(ps[3]).css("display","block");
    }
    else if (op == 4) {
        $(headers[4]).css("fontSize","20px");
        $(headers[4]).css("color","white");
        $(headers[4]).css("top","4px");
        $(ps[4]).css("display","block");
    }
    else {
        $(headers[5]).css("fontSize","20px");
        $(headers[5]).css("color","white");
        $(headers[5]).css("top","4px");
        for (var item = 0; item < pContact.length; item++) {
            $(pContact[item]).css("display","block");
        }
    }
}
function volverLugar(op) {
    if (op == 0) {
        $(headers[0]).css("fontSize","40px");
        $(headers[0]).css("color","green");
        $(headers[0]).css("top","50px");
        $(ps[0]).css("display","none");
    }
    else if (op == 1) {
        $(headers[1]).css("fontSize","40px");
        $(headers[1]).css("color","green");
        $(headers[1]).css("top","50px");
        $(ps[1]).css("display","none");
    }
    else if (op == 2) {
        $(headers[2]).css("fontSize","40px");
        $(headers[2]).css("color","green");
        $(headers[2]).css("top","50px");
        $(ps[2]).css("display","none");
    }
    else if (op == 3) {
        $(headers[3]).css("fontSize","40px");
        $(headers[3]).css("color","green");
        $(headers[3]).css("top","50px");
        $(ps[3]).css("display","none");
    }
    else if (op == 4) {
        $(headers[4]).css("fontSize","40px");
        $(headers[4]).css("color","green");
        $(headers[4]).css("top","50px");
        $(ps[4]).css("display","none");
    }
    else {
        $(headers[5]).css("fontSize","40px");
        $(headers[5]).css("color","green");
        $(headers[5]).css("top","50px");
        for (var item = 0; item < pContact.length; item++) {
            $(pContact[item]).css("display","none");
        }
    }
}

