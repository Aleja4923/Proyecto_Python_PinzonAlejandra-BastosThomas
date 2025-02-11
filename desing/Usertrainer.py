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


def registrarNotas():
    campers = guardarJSON
    ide = input("ingrese el ID del camper : ")
    if ide in campers:
        notas = input("agrega la nota de 10 a 100 :")
        campers[ide]["nota"]=notas
        print ("nota actualizada correctamente")
    else:
        print("camper no encontrado.")
def mirar_rutas():
    rutas = {
        "Ruta Java": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MySQL", "Java", "PostgreSQL", "SpringBoot"],
        "Ruta NodeJS": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MongoDB", "JavaScript", "MySQL", "Express"],
        "Ruta .NET": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MySQL", "C#", "PostgreSQL", ".Net Core"]
    }
    print("--- Rutas de Entrenamiento ---")
    for ruta, modulos in rutas.items():
        print(f"{ruta}: {', '.join(modulos)}")
        
def listar_estudiantes():
    datos = abrirJSON()
    print("--- Lista de Estudiantes ---")
    for estudiante in datos["campers"]:
        print(f"ID: {estudiante['ide']}, Nombre: {estudiante['Nombre']} {estudiante['Apellidos']}, Estado: {estudiante['Estado']}, Riesgo: {estudiante['Riesgo']}")