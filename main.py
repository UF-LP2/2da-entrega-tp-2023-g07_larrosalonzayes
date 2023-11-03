import csv

# COSAS PARA HACER Y CONSULTAS #

# - Metodo de acomodamiento de pacientes usando triage, ya esta hecha la asigancion de colores,
# pero no sabemos donde poner el metodo de insercion a la lista de pacientes segun su prioridad y tiempo esperado
# NOSOTROS LO DECIDIMOS

# - Agregar caso particular de pacientes ingresados por ambulancia

# - COMO PASAR COMO PARAMETRO A UN CONSTRUCTOR UNA LISTA, ACLARANDO QUE ES UNA LISTA (valga la redundancia)
# No es necesario

# - Consultar si lo del enum de colores esta bien implementado
# No sabemos si esta bien implementado

# - Como utilizar arboles para el acomodamiento de pacientes? Hay otra forna? (ojala que si)
# Usmos divide and conquer, nada que ver

# - Como organizar el tema de los cambios de turnos, medicos y enfermeros y como usar tiempo en python

# - Hacer getters y setters donde sea necesario

# - Chequear el tema del seguro de los pacientes (si no poseen uno, al publico)

# - Que pasa si un paciente muere?
# Lo decidimos nosotros

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
	print()

if __name__ == "__main__":
	main()