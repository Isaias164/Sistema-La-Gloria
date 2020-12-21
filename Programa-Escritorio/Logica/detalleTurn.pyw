# -*- coding: utf-8 -*-

class detalleTurno:
    ventana = None

    @staticmethod
    def mostrarVentana(self):
        detalleTurno.ventana.setupUi(detalleTurno.ventana)
        detalleTurno.ventana.show()
