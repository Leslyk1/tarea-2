def cargar():
    agenda = {}
    continual = "s"
    while continual == "s":
        fecha = input("Ingrese la fecha con formato dd/mm/aa: ")
        continua2 = "s"
        lista = []
        while continua2 == "s":
            hora = input("Ingrese la hora de la actividad con formato hh:mm: ")
            actividad = input("Ingrese la descripción de la actividad: ")
            lista.append((hora, actividad))
            continua2 = input("¿Ingresar otra actividad para la misma fecha [s/n]? ").lower()
        agenda[fecha] = lista
        continual = input("¿Ingresar otra fecha [s/n]? ").lower()
    return agenda


def imprimir(agenda):
    print("Listado completo de la agenda:")
    for fecha in agenda:
        print(f"Para la fecha: {fecha}")
        for hora, actividad in agenda[fecha]:
            print(f"Hora: {hora}, Actividad: {actividad}")


def consulta_fecha(agenda):
    fecha = input("Ingrese la fecha que desea consultar: ")
    if fecha in agenda:
        print(f"Actividades para la fecha {fecha}:")
        for hora, actividad in agenda[fecha]:
            print(f"Hora: {hora}, Actividad: {actividad}")
    else:
        print("No hay actividades agendadas para dicha fecha.")


# Bloque principal
agenda = cargar()
imprimir(agenda)
consulta_fecha(agenda)
