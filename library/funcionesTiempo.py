from datetime import datetime

hora_actual = datetime.now()

# Retorna la hora actual
def tiempoActual():
    return hora_actual

# Retorna en minutos el tiempo transcurrido desde que se comenzo
# a ejecutar el programa
def tiempoTranscurrido():
    segPasados = (datetime.now() - hora_actual).total_seconds()
    minutosPrograma = int(segPasados)
    return minutosPrograma
