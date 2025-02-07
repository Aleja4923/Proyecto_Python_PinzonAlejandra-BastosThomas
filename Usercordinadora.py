import json
# Función para cargar el inventario desde un archivo JSON
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


def agregarEstudiantes(estudiantes): 
    print("\nAgregar un nuevo Estudiante i:")
    ide= int(input("Ingresa el ID: "))
    Nombre = input("Ingresa el nombre: ")
    edad =  int(input("Ingresa la edad: "))
    Género = input("Ingresa el precio: ")
    Dirección = int(input("Ingresa el stock: "))
    Teléfono = int(input("ingrese el numero de telefono: "))
    correoElectronico= (input("ingrese el correo electronico: "))
    salon= int(input("ingrese el numero del salon: "))
    estado= input("ingrense el estado del estudiante : ")
    riesgo= input("ingrese el nivel de riesgo : ")
    estudiante23 ={
    "ide": ide,
    "nombre": Nombre,
    "edad": edad,
    "genero":Género,
    "Direccion" : Dirección,
    "telefono": Teléfono,
    "correoElectronico": correoElectronico,
    "salon ": salon,
      "estado": estado,
    "riesgo": riesgo,
    }

    estudiantes.append(estudiante23)
    guardarJSON(estudiantes)
    print("estudiante agregado con exito")

def actualizar_estado_riesgo(lista_estudiantes, ide, nuevo_estado, nuevo_riesgo):
    for estudiante in lista_estudiantes:
        if estudiante["ide"] == ide:
            estudiante["estado"] = nuevo_estado
            estudiante["riesgo"] = nuevo_riesgo
            print(f"Estado y riesgo actualizados para {estudiante['nombre']}")
            return True
    print("Estudiante no encontrado.")
    return False

import json

def cargar_desde_json(archivo="estudiantes.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  


lista_estudiantes = cargar_desde_json()


ide = input("Ingrese el ID del estudiante: ")
nuevo_estado = input("Ingrese el nuevo estado (Inscrito, Aprobado, etc.): ")
nuevo_riesgo = input("Ingrese el nivel de riesgo (Alto, Medio, Bajo, No determinado): ")

if actualizar_estado_riesgo(lista_estudiantes, ide, nuevo_estado, nuevo_riesgo):
    cargar_desde_json(lista_estudiantes)
    print("Cambios guardados exitosamente.")
    
