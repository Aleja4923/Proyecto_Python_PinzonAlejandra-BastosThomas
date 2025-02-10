import json 
def abrirJSON():
    try:
        with open("./campers.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = []  # Si el archivo no existe, se crea una lista vacía
    return estudiantes
# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./estudiantes.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible

def registrar_notas():
    datos= abrirJSON()
    idees = int(input("ID del Camper: "))
    for estudiantes in datos:
        if estudiantes["ide"] == idees:
            nota_teorica = (input("Nota Teórica (0-100): "))
            nota_practica = (input("Nota Práctica (0-100): "))
            nota_quices = (input("Nota de Quices/Trabajos (0-100): "))
            notafinal= (nota_quices*0,1)(nota_practica*0.6)(nota_teorica*0,3)/3
        if notafinal > 59:
            idees["campers"]["estado"] = ["aprobado"]
        else:
            idees["campers"]["estado"] = ["desaprobado"]
            
