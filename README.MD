# Proyecto Ejemplo de la Estructura de un proyecto Python con practicas de Clean Code

Este proyecto se modificó en un fork por BillVelasquez

El archivo README.MD es el lugar donde los usuariso de un proyecto van a buscar las respuestas
a las preguntas que se hacen antes de poder comenzar a usarlo.

Se escribe usando la notación Markdown, que pueden consultar en internet en muchas páginas

Por ejemplo, este Cheat Sheet: https://www.markdownguide.org/cheat-sheet/

## ¿Quién hizo esto?

Lista de autores (no ponga email, telefonos, nada de informacion privada)

## ¿Qué es y para qué es?

Describir el propósito del proyecto

## ¿Cómo lo hago funcionar?

- Prerrequisitos: que se debe hacer o tener antes de poder correr este proyecto
- Ejecución: como hacemos correr el programa, POR FUERA DEL ENTORNO DE DESARROLLO

Ejemplo:

Ubicados en la carpeta raiz del proyecto, ejecute:

```
py src\Console\CreditCardConsole.py
```

## ¿Cómo está hecho?

Describir la arquitectura del proyecto, bibliotecas usadas, dependencias de otros proyectos

Y la organización de los módulos (que hay en cada carpeta)


## Estructura sugerida

- Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
- Carpeta tests: Pruebas Unitarias 

Recuerde que cada carpeta de código fuente debe contener un archivo __init.py que permite que python
reconozca la carpeta como un Módulo y pueda hacer import

## Uso

Para ejecutar las pruebas unitarias, desde la carpeta raiz, use el comando

`
  py tests\CreditCardTests.py
`
Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`
  import sys
  sys.path.append("src")
`
