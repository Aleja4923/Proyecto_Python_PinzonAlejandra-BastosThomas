# [P:P:1] CampusLands ERP

---

🚨 ***Se guarda el derecho de solicitar la conexión a Discord con pantalla compartida para la validación del desarrollo de este proyecto.*** 🚨

---

## Descripción

El departamento académico de CampusLands desea crear un programa que le permita llevar el seguimiento académico de todos los ***campers*** que se encuentran matriculados en el programa intensivo de programación.

Para ello usted es contratado para liderar el desarrollo del programa que debe cumplir con las siguientes especificaciones:

1. El programa debe permitir a las personas encargadas de procesar las inscripciones
a el programa; la información que se tiene por cada ***camper*** es la siguiente : 

- # de identificación.
- Nombres.
- Apellidos.
- Dirección.
- Acudiente.
- Teléfonos de contacto(# de celular y #fijo).
- Estado (En proceso de ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado).
- Riesgo.

2. Campus cuenta con diferentes rutas de entrenamiento las cuales deben cumplir los candidatos que superen la prueba inicial. 

Las rutas son las siguientes: 

- Ruta NodeJS
- Ruta Java
- Ruta NetCore

3. El programa debe tener tres roles: **Camper, Trainer y Coordinador**, donde esta última persona debe contar con una opción en el programa que le permita registrar la nota de los ***campers*** que se han registrado y con ello cambiar su estado a “**Aprobado**”. La prueba es aprobada si el promedio entre la nota teórica y la nota practica es mayor o igual a 60.

4. Campus cuenta con diferentes áreas de entrenamiento en la cuales los ***campers*** aprenden los diferentes stacks tecnológicos dependiendo de las rutas de entrenamiento. Por el momento se cuenta con tres áreas de entrenamiento con una capacidad máxima de 33 **campers (Tener en cuenta que hay clases cada 4 horas)**.

5. La **coordinación académica** desea poder crear nuevas rutas de entrenamiento las cuales contienen la siguiente información (módulos):

- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
- Programación Web (HTML, CSS y Bootstrap).
- Programación formal (Java, JavaScript, C#).
- Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
- Backend (NetCore, Spring Boot, NodeJS y Express).

6. Los ***campers*** que pasaron de “**Inscritos**” a “**Aprobados**” podrán ser asignados a cualquiera de las rutas que se han creado previamente. Se debe tener en cuenta que no se puede exceder la capacidad de cada una de las áreas de entrenamiento.

7. **CampusLands** cuenta con **Trainers** expertos encargados de dirigir cada una de las rutas de entrenamiento. Esto quiere decir que a cada uno se le podrán asignar diferentes rutas de entrenamiento teniendo en cuenta su horario.

8. La **coordinación académica** desea contar con un módulo de matriculas que le permita
asignar los ***campers*** aprobados, **trainer** encargado, ruta de entrenamiento asignada, fecha de inicio, fecha finalización y salón de entrenamiento.

9. Periódicamente los ***campers*** son evaluados para conocer las habilidades adquiridas durante el proceso de entrenamiento, donde cuando finaliza cada modulo los ***campers*** deben presentar una prueba teórica y una prueba practica. Esta prueba es considerada como aprobada si el promedio de las dos dan un valor mayor o igual a 60. Aqui la prueba teórica tiene un peso de 30% y la prueba practica tiene un peso del 60%, donde durante dicho proceso el **Trainer** realizará quizes, trabajos los cuales tienen un peso del 10%. Al finalizar el proceso de evaluación se considerará aprobado el modulo si la nota final es mayor a 60.

10. La **coordinación académica** cuando finaliza cada uno de los módulos de las rutas
evalúa el rendimiento de cada uno de los **campers** teniendo en cuenta la nota obtenida en cada modulo. Si la nota es menor a 60 el **camper** queda en rendimiento bajo lo cual genera un llamado de atención. Por esto mismo, se deberá permitir consultar los **campers** que se encuentren en riesgo alto.

11. El módulo de reportes debe tener las siguientes funcionalidades: 

- Listar los **campers** que se encuentren en estado de inscrito.
- Listar los **campers** que aprobaron el examen inicial.
- Listar los entrenadores que se encuentran trabajando con **CampusLands**.
- Listar los **campers** que cuentan con bajo rendimiento.
- Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.
- Mostrar cuantos **campers** perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.

---

## Recursos

## Requerimientos técnicos

Para desarrollar dicho proyecto se deben tener los siguientes puntos en cuenta: 

- Se puede realizar en equipos de 2 personas, las cuales deben aportar periódicamente al repositorio de GitHub. Para este caso, se creará un repositorio llamado “Proyecto_Python_Apellido1Nombre1-Apellido2Nombre2” con dicho fin.
- Solamente se permitirá usar archivos JSON para la persistencia de datos, pues la idea es aplicar los principios CRUD (Crear, Leer, Actualizar y Eliminar).

---

# Criterios y Rúbrica Evaluativa

De acuerdo a lo establecido y solicitado, se muestra la rúbrica evaluativa a tener en cuenta:

### 1. Creación de Menú de Navegación y Persistencia

- **0 puntos**: No se creó ningún menú a nivel de consola para navegar por las funcionalidades del programa, al igual que no se encuentra persistencia alguna en un archivo externo.
- **5 puntos**: Se visualiza el intento de creación de un menú a nivel de codificación, pero no está funcional o no entendible para el usuario final, al igual que no se encuentra persistencia alguna en un archivo externo.
- **10 puntos**: Se visualiza la creación de un menú a nivel de consola, pero no cumple con los roles y funcionalidades establecidas en este ejercicio, al igual que no se encuentra persistencia alguna en un archivo externo.
- **20 puntos**: Se crea de manera exitosa un menú comprensible para el usuario final en consola, cumpliendo con los requerimientos establecidos en este documento, y manteniendo persistencia de la información manejada a lo largo del programa.

### 2. Módulo de Coordinación Académica

- **0 puntos**: No se creó ningún módulo funcional para el rol de Coordinación Académica en el programa.
- **5 puntos**: Se evidencia el intento de creación de un módulo para el rol de Coordinación Académica, pero no está funcional o no entendible para el usuario final.
- **10 puntos**: Se evidencia la creación de un módulo para el rol de Coordinación Académica, pero no cumple con los requerimientos o funcionalidades solicitadas.
- **20 puntos**: Se crea exitosamente el módulo para Coordinación Académica, cumpliendo con los requerimientos establecidos en este documento, y manteniendo persistencia de la información manejada a lo largo del programa.

### 3. Módulo de Trainer

- **0 puntos**: No se creó ningún módulo funcional para el rol de Trainer en el programa.
- **5 puntos**: Se evidencia el intento de creación de un módulo para el rol de Trainer, pero no está funcional o no entendible para el usuario final.
- **10 puntos**: Se evidencia la creación de un módulo para el rol de Trainer, pero no cumple con los requerimientos o funcionalidades solicitadas.
- **20 puntos**: Se crea exitosamente el módulo para Trainer, cumpliendo con los requerimientos establecidos en este documento, y manteniendo persistencia de la información manejada a lo largo del programa.

### 4. Módulo de reportes

- **0 puntos**: No se evidencia la creación o intento de creación de dicha funcionalidad a lo largo del programa, al igual que no se encuentra persistencia alguna en un archivo externo.
- **5 puntos**: Se crea la estructura para la funcionalidad , pero no acciona de manera correcta o en estado no funcional, al igual que no se encuentra persistencia alguna en un archivo externo.
- **10 puntos**: Se implementa el 50% de los ítems requeridos a nivel de funcionalidad, manteniendo la persistencia de la información en un archivo externo.
- **20 puntos**: Se implementa el 100% de los ítems requeridos a nivel de funcionalidad, manteniendo la persistencia de la información en un archivo externo.

### 5. GitHub y Entrega de Proyecto

- 🚨 **Cancelación o Anulación del Proyecto** : No se entregó ningún repositorio, su visualización está oculta (o no compartida con el Trainer) o hubo adulteración después de la fecha y hora establecida para su entrega, ***Evidencia de clonación o conocido como `fork` de algún repositorio, distribución y/o copia de dicho trabajo por cualquier medio de comunicación (verbal, digital, entre otras), se asumirá como cancelación del proyecto de manera definitiva.*** 🚨
- **5 puntos**: Se creó el repositorio, pero en su rama principal no se encuentra el proyecto general ,al igual que algún archivo en relación al proyecto.
- **10 puntos**: Se creó exitosamente el repositorio, donde en su rama principal se encuentra el proyecto general y sus archivos en relación a ello, con evidencia de la participación del equipo completo de manera periódica.

## Grupos M2, M3

[5. GitHub y Entrega de Proyecto](https://www.notion.so/5-GitHub-y-Entrega-de-Proyecto-430f21d6c9b5433397b5911ded22f608?pvs=21): También se les calificará el uso del ***conventional commit*** y las fotografías de las evidencias, en caso de contar con ellas.

---

# 🎉***¡Éxitos en el desarrollo de este proyecto!***🎉

![giphy.gif](https://prod-files-secure.s3.us-west-2.amazonaws.com/eaa1771c-fc19-40d4-8527-37ca1caab8fa/6db043cb-8314-4e6d-85fc-8509b539cce0/giphy.gif)