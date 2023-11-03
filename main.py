import csv

# COSAS PARA HACER Y CONSULTAS #

# - Metodo de acomodamiento de pacientes usando triage, ya esta hecha la asigancion de colores,
# pero no sabemos donde poner el metodo de insercion a la lista de pacientes segun su prioridad y tiempo esperado
# NOSOTROS LO DECIDIMOS

# - Agregar caso particular de pacientes ingresados por ambulancia

# - COMO PASAR COMO PARAMETRO A UN CONSTRUCTOR UNA LISTA, ACLARANDO QUE ES UNA LISTA (valga la redundancia)
# No es necesario, arreglar todos los imports

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

# - Desarrollar una interfaz medianamente fea (y consultar si es necesario)

from Ambulancia import cAmbulancia
from Color import cColor
from Consultorio import cConsultorio
from Enfermero import cEnfermero
from Hospital import cHospital
from Medico import cMedico
from Paciente import cPaciente
from SalaEspera import cSalaEspera

def main() -> None:
	# Inicio del main
	print()

if __name__ == "__main__":
	main()