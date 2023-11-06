import pytest
from src.Enfermero import cEnfermero
from src.Paciente import cPaciente
from src.Color import cColor, Colores

# Test para ver si asigna correctamente los colores según la patología declarada

def testEnfermero1():
    persona1= cPaciente(1234, "clarita", "lops", "politraumatismo grave", 23, True)
    enfermero1= cEnfermero(12345, "juan", "massa", "MANIANA", True)
    enfermero1.catalogarPaciente(persona1)
    assert persona1.color == Colores.ROJO

 
