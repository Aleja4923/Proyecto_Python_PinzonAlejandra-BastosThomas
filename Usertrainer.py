import json 
def abrirJSON():
    try:
        with open("./estudiantes.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = []  # Si el archivo no existe, se crea una lista vacía
    return estudiantes
# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./estudiantes.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible

    while True:
        print(" Menu del Trainer ")
        print("1. Registrar Notas")
        print("2. Consultar Campers en Riesgo")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_notas()
        elif opcion == "2":
            campersriesgo()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def registrar_notas():
    datos= abrirJSON()
    idees = int(input("ID del Camper: "))
    for estudiantes in datos:
        if estudiantes["ide"] == idees:
            nota_teorica = float(input("Nota Teórica (0-100): "))
            nota_practica = float(input("Nota Práctica (0-100): "))
            nota_quices = float(input("Nota de Quices/Trabajos (0-100): "))
            notafinal= (nota_quices*0,1)(nota_practica*0.6)(nota_teorica*0,3)/3
        if notafinal > 59:
            [estado]= 

