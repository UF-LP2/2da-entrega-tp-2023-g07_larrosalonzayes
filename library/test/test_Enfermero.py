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

    # Crea una instancia de cEnfermero y cPaciente
def test1_catalogarPaciente():

    enfermero = cEnfermero(12345, "Juan", "Parker", "MANIANA", True)
    paciente1 = cPaciente(1234, "Clarita", "Lops", "politraumatismo grave", 23, True)

    # Llama al método catalogarPaciente en la instancia de cPaciente
    paciente1_mod = cEnfermero.catalogarPaciente(paciente1)
	 # Comprueba si el color del paciente se ha asignado correctamente
    assert (paciente1_mod.getColor().getColoracion()== Colores.ROJO) 
    


    










        
