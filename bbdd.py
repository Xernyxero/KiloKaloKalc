import json
from classes import *

# -------------------- Escribir y Leer en la base de datos-----------------------------

def guardar_lista(lista, nombre_archivo):
  with open(nombre_archivo + ".json", "a+") as archivo:
    lista_json = json.dumps(lista) # Convertir la lista en un objeto JSON.
    archivo.write(lista_json + "\n") # Escribir el objeto JSON en el archivo.

def cargar_archivos():
	file = ["alimentos", "recetas"]
	datos = [None]*2
	for i,name in enumerate(file):
		try:
			with open(name + ".json", "r") as archivo:
				datos[i] = archivo.readlines()		
		except:
			with open(name + ".json", "w") as archivo:
				pass
	return(datos[0], datos[1])

# --------------------------------------------------------------------------------

def json_to_obj():
	""" Carga todos los datos para crear las instancias de las clases alimento y receta"""
	datos_alimentos, datos_recetas = cargar_archivos()
	names_alimentos = []
	names_recetas = []

	for elemento in datos_alimentos:
		datos_alimento = eval(elemento)
		nueva_instancia = Alimento(datos_alimento)
		names_alimentos += [nueva_instancia]

	for elemento in datos_recetas:
		datos_receta = eval(elemento)
		nueva_instancia = Receta(datos_receta)
		names_recetas += [nueva_instancia]
		
	return(names_alimentos,names_recetas)

def is_object(estrin, lista_objetos):
	objeto = estrin
	for elemento in lista_objetos:
		if estrin == elemento.nombre:
			objeto = elemento
			#print("Se ha encontrado el objeto")
	if objeto == estrin:
		print("No se encontró el objeto")
	return(objeto)