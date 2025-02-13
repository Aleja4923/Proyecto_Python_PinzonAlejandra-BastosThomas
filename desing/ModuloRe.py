import json
from desing.userCordinadora import *
from desing.userTrainer import *

DB_FILE = "/data/campers.json"

MENU_REPORTES = """
*-----------------------------*
---------Menu Reportes---------
*-----------------------------*
¿Que deseas hacer?

    1. Ver campers inscritos
    2. Ver campers aprobados
    3. Ver trainers
    4. Ver campers con bajo rendimiento
    5. Regresar menu anterior
"""

def mostrarMenuR():
    print (MENU_REPORTES)
    opt = input("= ")
    match opt:
            case "1":
                campersInscritos()
            case "2":
                campersAprobados()
            case "3":
                print (" Pedro, Juan, Aura ")
            case "4":
                campersRiesgo()
            case _:
                print ("Error")
                return mostrarMenuR ()