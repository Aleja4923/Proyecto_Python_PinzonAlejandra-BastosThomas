import json
# Función para cargar el inventario desde un archivo JSON
def abrirJSON():
    try:
        with open("./estudiantes.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = {"campers": []} 
    return estudiantes
# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./estudiantes.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible


def agregarEstudiantes(estudiantes): 
    print("Agregar un nuevo Estudiante i:")
    ide= int(input("Ingresa el ID: "))
    for estudiante in estudiantes["campers"]:
        if estudiante["ide"] == ide:
            print ("El id ya existe")
            return
        
    Nombre = input("Ingresa el nombre: ")
    Direccion = (input("Ingresa el stock: "))
    TelefonoCel = int(input("ingrese el numero de telefono celular: "))
    TelefonoFijo = int(input("ingrese el numero de telefono fijo: "))
    correoElectronico= (input("ingrese el correo electronico: "))
    estado= input("ingrense el estado del estudiante : ")
    riesgo= input("ingrese el nivel de riesgo : ")
    estudiante23 ={
    "ide": ide,
    "Nombre": Nombre,
    "Dirección" : Direccion,
    "Telefono Celular": TelefonoCel,
    "Telefono Fijo": TelefonoFijo,
    "Correo electrónico": correoElectronico,
    "Estado": estado,
    "Riesgo": riesgo,
    }

    estudiantes["campers"].append(estudiante23)
    guardarJSON(estudiantes)
    print("estudiante agregado con exito")

def verestudiantes(estudiantes):
    for i,estudiantes in enumerate (estudiantes["campers"], 1):
        print("Estudiante "),i+1
        print("  ID: " + str(estudiantes['ide']))
        print("  Nombre: " + estudiantes['Nombre'])
        print("  Dirección: " + estudiantes['Direccion'])
        print("  Teléfono Celular: " + str(estudiantes['Telefono Celular']))
        print("  Teléfono Fijo: " + str(estudiantes['Telefono Fijo']))
        print("  Correo Electrónico: " + estudiantes['Correo electronico'])
        print("  Estado: " + estudiantes['Estado'])
        print("  Riesgo: " + estudiantes['Riesgo'])

def editar_estudi(estudiantes):
    ide= int(input("Ingrese el id del estudiante a editar"))
    estudiencon= None
    for estudiante in estudiantes["campers"]:
        if estudiante ["ide"] == ide:
            estudiencon = estudiante
            break

    print ("Que desea editar")
    print("1. Nombre")
    print("2. Direccion")
    print("3. Telefono Celular")
    print("4. Telefono Fijo")        
    print("5. Correo electrónico")
    print("6. Estado")
    print("7. Riesgo")
    print("8. Volver a menu")
    
    op=input("Selecione una opcion digitando el numero")

    if op == "1":
        estudiencon["Nombre"] = str(input("Ingrese el nuevo nombre"))
    elif op =="2":
        estudiencon["Direccion"] = input("Ingrese la nueva direccion")
    elif op == "3":
        estudiencon["Telefono Celular"] = int(input("Ingrese el nuevo telefono celular"))
    elif op == "4":
        estudiencon["Telefono Fijo"] = int(input("Ingrese el nuevo telefono fijo"))
    elif op == "5":
        estudiencon["Correo electronico"] = input("Ingrese el nuevo correo electronico")
    elif op == "6":
        estudiencon["Estado"] = input("Ingrese el nuevo estado")
    elif op == "7":
        estudiencon["Riesgo"] = input("Ingrese el nuevo nivel de riesgo")
    elif op == "8":
        return

    else:
        print("Opcion no valida")
        return 
    
    guardarJSON(estudiantes)

estudiantes = abrirJSON()   

verestudiantes = (estudiantes)