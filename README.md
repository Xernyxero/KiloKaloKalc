Descripción:

  Este proyecto permite gestionar recetas y dietas personalizadas en función de los macronutrientes
  y calorias de los ingredientes. Los usuarios pueden registrarse, añadir alimentos, crear recetas y
  ajustar sus dietas segun sus objetivos.
  
Estructura del proyecto:

  * main.py:
      Archivo principal que es el que se deberá ejecutar.
      Contiene el cuerpo y toda la forma de como se ejecuta el programa
  * bbdd.py:
      Administra la base de datos en un archivo Excel (Datos.xlsx).
      Permite guardar y extraer datos de las hojas: Alimentos, Recetas, Usuarios, Dietas.
      Crea objetos a partir de los datos almacenados
  * executable.py:
      Contiene las funciones necesarias para el correcto funcionamiento del archivo main.py
  * classes.py:
      Contiene las definiciones y metodos de las clases Ingrediente, Usuario, Receta
  * Datos.xlsx:
      Actúa como base de datos. Debe tenerla aun estando vacia para que funcione.

Requisitos:
  
  * Python 3.x
  * Librerias necesarias: openpyxl, pandas, numpy, scipy

