import json 
import tabulate
from desing.userTrainer import *


# Función para cargar el inventario desde un archivo JSON
def abrirJSON(DBFILE):
    dicFinal={}
    with open("./data/campers.json",'r') as openFile:
        dicFinal=json.load(openFile)        
    return dicFinal

def guardarJSON(dic):
    with open("./data/campers.json",'w') as outFile:
        json.dump(dic,outFile)


estudiantes = abrirJSON()   

def agregarEstudiantes():
    ide = input("Ingresa el ide : ")
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingrese el apellido: ")
    acudiente = input("Ingrese el acudiente: ")
    direccion = input("Ingresa la dirección: ")
    telefono_cel = input("Ingrese el número de teléfono celular: ")
    telefono_fijo = input("Ingrese el número de teléfono fijo: ")
    correo_electronico = input("Ingrese el correo electrónico: ")
    estado = input("Ingrese el estado del estudiante: ")
    riesgo = input("Ingrese el nivel de riesgo: ")
    
    estudiante = {
        "ide": ide,
        "Nombre": nombre,
        "Apellido": apellido,
        "Acudiente": acudiente,
        "Dirección": direccion,
        "Telefono Celular": telefono_cel,
        "Telefono Fijo": telefono_fijo,
        "Correo Electrónico": correo_electronico,
        "Estado": estado,
        "Riesgo": riesgo
    }
    
    estudiantes.append(estudiante)

    guardarJSON(estudiantes)
    print("Estudiante agregado con é   Scrumito.")


def verestudiantes():
    for i in range (len(estudiantes)):
        print("Estudiante "),i+1
        print("  ID: " + (estudiantes[i]["ide"])) ,
        print("  Nombre: " + (estudiantes[i]["Nombre"])),
        print("  Apellido: " + (estudiantes[i]["Apellido"])),
        print("  Acudiente" + (estudiantes["Acudiente"][i]["Acudiente"])),
        print("  Dirección: " + (estudiantes[i]["Dirrecion"])),
        print("  Teléfono Celular: " + (estudiantes[i]["Telefono Celular"])),
        print("  Teléfono Fijo: " + (estudiantes[i]["Telefono Fijo"])),
        print("  Correo Electrónico: " + (estudiantes[i]["Correo electronico"])),
        print("  Estado: " + (estudiantes[i]["Estado"])),
        print("  Riesgo: " + (estudiantes[i]["Riesgo"]))

def editar_estudi():
    verestudiantes()
    ide= int(input("Ingrese el id del estudiante a editar"))
    print ("Que desea editar")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Acudiente")
    print("4. Direccion")
    print("5. Telefono Celular")
    print("6. Telefono Fijo")        
    print("7. Correo electrónico")
    print("8. Estado")
    print("9. Riesgo")
    print("10. Volver a menu")
    opc=int(input(": "))
    for i in range(estudiantes):
        match opc:
            case 1:
                nm=input("Ingrese el nuevo nombre: ")
                estudiantes[ide-1]["Nombre"]=(nm)
            case 2: 
                ap=input("Ingrese el nuevo apellido: ")
                estudiantes[ide-1]["Apellido"]=(ap)
            case 3:
                ac=input("Ingrese el numero acudiente")
                estudiantes[ide-1]["Acudiente"]=(ac)
            case 4:
                di=input("Ingrese la nueva dirrecion")
                estudiantes[ide-1]["Dirrecion"]=(di)
            case 5:
                tc=input("Ingrese el nuevo telefono")
                estudiantes[ide-1]["Telefono Celular"]=(tc)
            case 6:
                tf=input("Ingrese el nuevo telefono fijo")
                estudiantes[ide-1]["Telefono Fijo"]=(tf)
            case 7:
                ce=input("Ingrese el correo electronico")
                estudiantes[ide-1]["Correo electronico"]=(ce)
            case 8:
                es=input("Ingrese el estado que se encuentra")
                estudiantes[ide-1]["Estado"]=(es)
            case 9:
                Ri=input("Ingrese el riesgo en el que esta")
                estudiantes[ide-1]["Riesgo"]=(Ri)         

    guardarJSON(estudiantes)


campers = {}  #Diccionario para almacenar los datos de los campers

###
def modulo_matriculas():
    datos = abrirJSON()
    ide = int(input("Ingrese el ID del camper: "))
    for estudiante in datos:
        if estudiante["ide"] == ide:
            print("1. Matricular camper en una ruta")
            print("2. Ver ruta actual del camper")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ruta = input("Ingrese la ruta de entrenamiento (Java, NodeJS, .NET): ")
                estudiante["Ruta"] = ruta
                guardarJSON(datos)
                print(f"Camper matriculado en la ruta {ruta}.")
            elif opcion == "2":
                if "Ruta" in estudiante:
                    print(f"Ruta actual: {estudiante['Ruta']}")
                else:
                    print("El camper no está matriculado en ninguna ruta.")
            return
    print("Camper no encontrado.")



def campersRiesgo():

    altoriesgo = []

    data = abrirJSON()
    for camper in data:
        if camper["Riesgo"] == "Alto":
            altoriesgo.append(camper)
    if altoriesgo:
        for camper in altoriesgo:
            print (camper)

data = abrirJSON()
def campersInscritos():
    print(data)  

    for camper in data:
        if camper.get("Estado") == "Inscrito":  
            print(camper)

def campersAprobados():
    data = abrirJSON()  
    for camper in data:
        if camper.get("Estado") == "Aprobado":  
            print(camper)

def vernotas():
    verestudiantes()
    print("Ingrese el ID del estudiante que quieres ver las notas")
    id=int(input(": "))
    print("Ingrese el skill del cual quiera saber la nota")
    skill=str(input(": "))
    for i in range(data):
        if id==data[i]["ide"]:
            print("Estudiante: ",i+1,data[i]["Nombre"])
            print("Nota Teorica: ",data[i]["cursos"][skill]["nota1"],
                  "Nota Practica", data[i]["cursos"][skill]["nota2"],
                  "Nota Quizes: ",data[i]["cursos"][skill]["nota3"],
                  "Nota Final",data[i]["cursos"][skill]["notaF"])