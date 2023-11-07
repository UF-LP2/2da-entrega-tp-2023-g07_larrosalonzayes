import pytest

from src.Enfermero import cEnfermero
from src.Paciente import cPaciente
from src.Color import cColor, Colores

# Test para ver si asigna correctamente los colores según la patología declarada

class TestEnfermero(unittest.TestCase):

    def test_catalogarPaciente(self):
        # Crea una instancia de cEnfermero y cPaciente
        enfermero = cEnfermero(12345, "Juan", "Massa", "MANIANA", True)
        paciente = cPaciente(1234, "Clarita", "Lops", "politraumatismo grave", 23, True)

        # Llama al método catalogarPaciente
        enfermero.catalogarPaciente(paciente)

        # Comprueba si el color del paciente se ha asignado correctamente
        self.assertEqual(paciente.getColor().coloracion, Colores.ROJO)

if __name__ == '__main__':
    unittest.main()
 
