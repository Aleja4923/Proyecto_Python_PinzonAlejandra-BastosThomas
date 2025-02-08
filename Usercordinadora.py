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
    Dirección = (input("Ingresa el stock: "))
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
    "salon": salon,
    "estado": estado,
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
def cargar_desde_json(archivo="estudiantes.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def registrar_notas():
    ide = int(input("Ingrese el id del estu"))
    notateorica=int(input("Ingrese nota teorica del estudiante"))

def editar_estudi(lista_estudiantes):
    while True:
        ide= int(input("Ingrese el id del estudiante a editar"))
        estudiencon= None
        for estudiante in lista_estudiantes:
            if estudiante ["ide"] == ide:
                estudiencon = estudiante
                break
            else:
                print ("id no encontrado")
                return
    
        print ("Que desea editar")
        print("1. Nombre")
        print("2. Edad")
        print("3. Género")
        print("4. Dirección")
        print("5. Teléfono")
        print("6. Correo electrónico")
        print("7. Salón")
        print("8. Estado")
        print("9. Riesgo")
        print("10. Volver a menu")
    
        op=int(input("Selecione una opcion digitando el numero"))

        if op == "1":
            estudiencon["nombre"] = input ("Ingrese el nuevo nombre")
        elif op =="2":
            estudiencon["edad"] = input ("Ingrese la nueva edad")
        elif op== "3":
            estudiencon["genero"] = input("Ingrese el nuevo genero")
        elif op== "4":
            estudiencon["direccion"] = input("Ingrese la nueva direccion")
        elif op == "5":
            estudiencon["telefono"] = int(input("Ingrese el nuevo telefono"))
        elif op == "6":
            estudiencon["correo_electronico"] = input("Ingrese el nuevo correo electronico")
        elif op == "7":
            estudiencon["salon"] = int(input("Ingrese el nuevo salon"))
        elif op == "8":
            estudiencon["estado"] = input("Ingrese el nuevo estado")
        elif op == "9":
            estudiencon["riesgo"] = input("Ingrese el nuevo nivel de riesgo")
        elif op == "10":
            break

        else:
            print("Opcion no valida")
            return 
    
        guardarJSON(lista_estudiantes)
        print

lista_estudiantes = cargar_desde_json()


ide = input("Ingrese el ID del estudiante: ")
nuevo_estado = input("Ingrese el nuevo estado (Inscrito, Aprobado, etc.): ")
nuevo_riesgo = input("Ingrese el nivel de riesgo (Alto, Medio, Bajo, No determinado): ")

if actualizar_estado_riesgo(lista_estudiantes, ide, nuevo_estado, nuevo_riesgo):
    cargar_desde_json(lista_estudiantes)
    print("Cambios guardados exitosamente.")

lista_estudiantes = cargar_desde_json()


ide = input("Ingrese el ID del estudiante: ")
nuevo_estado = input("Ingrese el nuevo estado (Inscrito, Aprobado, etc.): ")
nuevo_riesgo = input("Ingrese el nivel de riesgo (Alto, Medio, Bajo, No determinado): ")

if actualizar_estado_riesgo(lista_estudiantes, ide, nuevo_estado, nuevo_riesgo):
    cargar_desde_json(lista_estudiantes)
    print("Cambios guardados exitosamente.")
    
