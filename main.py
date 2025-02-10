from desing.Usercordinadora import *
from desing.Usertrainer import * 

def obtener_opcion(): 
    while True:
        print("""
        *****************************************************
            Menú de productos
                1. Inscripciones
                2. Rutas de entrenamiento
                0. Salir
        *****************************************************           
        """)
        
        try:
            opcion = int(input("--> "))
            
            match opcion:
                case 1:
                    agregarEstudiantes()
                case 2:
                    while True:
                        print("""
                        ===========================================
                        Ver Todos los Elementos
                        ===========================================
                        ¿Qué categoría deseas ver?
                        1. Ver Todos los campers 
                        2. Ver Todas las notas 
                        3. Ver Todas las rutas 
                        4. Regresar al Menú Principal
                        ===========================================
                        """)
                        try:
                            sub_opcion = int(input("--> "))
                            
                            match sub_opcion:
                                case 1:
                                    seeTables(RUTA_campers)
                                case 2:
                                    seeTables(RUTA_notas) 
                                case 3:
                                    seeTables(RUTA_rutas)  
                                case 4:
                                    break
                                case _:
                                    print("Opción no válida, intenta de nuevo.")
                        except ValueError:
                            print("Error: Ingresa un número válido.")

                case 0:
                    print("Saliendo del programa...")
                    break
                
                case _:
                    print("Opción no válida, intenta de nuevo.")
        
        except ValueError:
            print("Error: Ingresa un número válido.")

def seeTables(ruta): 
    """Muestra los datos en formato de tabla"""
    try:
        data = abrirJSON(ruta)  # Toma la información del JSON
        if not data:
            print("No hay datos disponibles.")
        else:
            print(tabulate(data, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

    input("--> Presione enter para continuar")

# Llamada a la función para probar el menú
obtener_opcion()

        