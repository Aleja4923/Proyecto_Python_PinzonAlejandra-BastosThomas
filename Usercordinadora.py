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
    salon= int(input("ingrese el numero del salon"))
    
    estudiante23 ={
    "ide": ide,
    "nombre": Nombre,
    "edad": edad,
    "genero":Género,
    "Direccion" : Dirección,
    "telefono": Teléfono,
    "correoElectronico": correoElectronico,
    "salon ": salon,
    }

    estudiantes.append(estudiante23)
    guardarJSON(estudiantes)
    print("estudiante agregado con exito")




