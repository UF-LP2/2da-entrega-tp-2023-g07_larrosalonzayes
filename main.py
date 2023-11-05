import csv

# COSAS PARA HACER #

# - Metodo de acomodamiento de pacientes usando triage, ya esta hecha la asigancion de colores,
# pero no sabemos donde poner el metodo de insercion a la lista de pacientes segun su prioridad y tiempo esperado

# - Agregar caso particular de pacientes ingresados por ambulancia

# - Como organizar el tema de los cambios de turnos, medicos y enfermeros y como usar tiempo en python

# - Chequear el tema del seguro de los pacientes (si no poseen uno, al publico)

# - Agregar funciones para la lectura de archivos .csv

# - Desarrollar una interfaz (y consultar si es necesario)

from src.Ambulancia import cAmbulancia
from src.Color import cColor
from src.Color import Colores
from src.Consultorio import cConsultorio
from src.Enfermero import cEnfermero
from src.Hospital import cHospital
from src.Medico import cMedico
from src.Paciente import cPaciente
from src.SalaEspera import cSalaEspera

# def cargarPacientesCSV():

def main() -> None:
	# Inicio del main
	print("Programa ejecutado")

if __name__ == "__main__":
	main()