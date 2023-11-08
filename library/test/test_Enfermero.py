import pytest

from Enfermero import cEnfermero
from Paciente import cPaciente
from Color import cColor, Colores

#/////////////////////////////////////// TESTEO DE PRUEBA ////////////////////////////////////////////////////// 

def test1():
	suma = cEnfermero.suma_numeros(100,4)
	# 2000 - 1000*1.5 - 100*2 es igual a 300
	assert(cEnfermero.suma_numeros(100,4) == 104) 


# Test para ver si asigna correctamente los colores según la patología declarada 

def test1_catalogarPaciente():
    # Crea una instancia de cEnfermero y cPaciente
    enfermero = cEnfermero(12345, "Juan", "Parker", "MANIANA", True)
    paciente = cPaciente(1234, "Clarita", "Lops", "politraumatismo grave", 23, True)

    # Llama al método catalogarPaciente
    paciente = cEnfermero.catalogarPaciente(paciente)

    # Comprueba si el color del paciente se ha asignado correctamente
    assert paciente.getColor.Color()== Colores.ROJO









        
