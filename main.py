from library.Consultorio import cConsultorio
from library.Hospital import cHospital
from library.SalaEspera import cSalaEspera

from library.funcionesCSV import cargarMedicosCSV, cargarEnfermerosCSV, cargarPacientesCSV

# 1 NOCTURNO = 23:00 a 06:00
# 2 MANIANA = 06:00 a 10:00
# 3 HORAPICO = 10:00 a 16:00
# 4 TARDENOCHE = 16:00 a 23:00

# 5 ROJO
# 4 NARANJA
# 3 AMARILLO
# 2 VERDE 

# COSAS PARA HACER
# 
# - Intefaz     (si o si)
# - Simulación  (si o si)
# - Función de paso de tiempo (ver si usamos time o como lo manejamos)
# - Función para los tiempos de espera (si un naranja supera el tiempo de espera maximo, hay que setearle el color a rojo para q lo atiendan) 
# - Asignar a los pacientes de la lista (ya ordenados) el consulorio (si o si) 

def main() -> None:
	# Inicio del main
	listaPacientes = cargarPacientesCSV("pacientes.csv")
	listaMedicos = cargarMedicosCSV("medicos.csv")
	listaEnfermeros = cargarEnfermerosCSV("enfermeros.csv")


	# Por la poca cantidad de datos, los inicializamos sin la necesidad de un .csv
	cons0 = cConsultorio(0, False)
	cons1 = cConsultorio(1, False)
	cons2 = cConsultorio(2, False)
	cons3 = cConsultorio(3, False)
	cons4 = cConsultorio(4, False)

	listaConsultorios = []
	listaConsultorios.append(cons0)
	listaConsultorios.append(cons2)
	listaConsultorios.append(cons3)
	listaConsultorios.append(cons4)

	# La sala de espera se inicializa con una lista vacia
	salaEspera = cSalaEspera( [] )
	hospital = cHospital("Favaloro", "ABC123", salaEspera, listaEnfermeros, listaConsultorios, listaMedicos)

	# En este metodo se cargan los pacientes iniciales en la sala de espera, se categorizan
	# segun el metodo usado por los enfermeros, y luego se ordenan usando merge-sort
	hospital.cargarPacientesIniciales(listaPacientes)


if __name__ == "__main__":
	main()