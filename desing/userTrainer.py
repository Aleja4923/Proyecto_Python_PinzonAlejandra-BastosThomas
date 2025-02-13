
import json 
from desing.userCordinadora import *


###funciones de notas


 ### uso de la funcion
 # ruta_json = "campers.json"
 ##actualizar_notas(ruta_json)   

## Colocar quien eres Pedro Maria o Aura dependiendo de su ruta y proyectar la ruta
## proyectarle los estudiantes
DBFILE= "/campers"

op= """Bienvenido que  trainer eres?
            1. Pedro
            2. Maria
            3. Aura
        Porfavor digite un numero
    """



def EditarNotas():
    ruta = []
    Data = abrirJSON(DBFILE)   
    for camper in Data:
        if Data[camper]["Ruta"] in [".NET", "Java", "NodeJS"]:

            ruta.append (Data[camper])
    if ruta:

        c=1
        for camper in ruta:
            print ("Estudiante# ",c,ruta[camper])
            c+=1
        print(" ")
        print("A que estudiante quiere editar (digite id)")
        x=int(input(": "))
        
        print("Ingrese el skill al cual le quiere editar las notas")
        skill=input(": ")
        print('''
              Que nota quiere editar?
              1. Prueba teorica
              2. Prueba Practica
              3. Quizes
              ''')
        nota=int(input(": "))
        if nota==1 :
            g="nota1"
        elif nota==2:
            g="nota2"
        elif g==3:
            g="nota3"
        else:
            print("Nota no valida")
        print("Ingrese la nueva nota")
        nota=int(input(": "))
        for estudiante in Data["campers"]:
            if x == estudiante["ide"]:
                if skill in estudiante["cursos"]:
                    estudiante["cursos"][skill][g] = nota
                else:
                    print("El skill ingresado no existe.")

        
