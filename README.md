## Cómo correr la aplicación

Para levantar la aplicación, en la consola ingresar al proyecto *visit-tracker* y ejecutar el script *./run.sh*

## Cómo ejecutar las pruebas de carga

Incluir el archivo Crear.jmx en JMeter y ejecutarlo.

## Notas

En la carpeta *documents* hay:
- 4 colecciones de postman para correr todas las funcionalidades pedidas, es decir, los métodos CRUD para los empleados, las propiedades y las visitas a
propiedades, y, también, una colección llamada INMOBILIARIA METRICAS, que contiene dos endpoints, uno para obtener todas las propiedades que visitó un empleado
y otra que calcula la distancia total que recorrió un empleado en las visitas.

- un pdf en donde está el diagrama del modelo de datos

- una carpeta llamada *jmeter* en donde está el archivo con la configuración para ejecutar la prueba de carga en el programa jmeter y un documento con
las imágenes que resultaron de la misma y sus respectivos análisis

## Refactors que me hubiera gustado hacer:

- Agregar manejo de excepciones

- Agregar logs

- Agregar los test unitarios para los endpoints y terminar los casos de prueba para el repository y metric_analysis. Y corregir el error 
```
self = <repository.employee_repository.EmployeeRepository object at 0x7f93bf9301f0>
db_file = './tests/data_base_preparation/fake_visit_tracker.db'

    def __init__(self, db_file="./db/visit_tracker.db"):
>       self.conn = sqlite3.connect(db_file, check_same_thread=False)
E       sqlite3.OperationalError: unable to open database file
```