import user as us
import classes as clas

def nuevo_alimento():
	print("¿Qué alimento quieres añadir?:")
	nombre = input()
	print("Indica que tipo de comida es:")
	tipo = input()
	print("Introduzca cada uno de los parametros en el siguiente orden:")

	values_macros = [None]*6

	for i in range(0,6):
		print(us.keys_macros[i])
		values_macros[i] = float(input())

	nuevo_dato = [nombre,tipo] + values_macros
	return(nuevo_dato)

def nueva_receta():
	print("Nombre de la receta:")
	nombre = input()
	print("desayuno / almuerzo / merienda / cena")
	tipo = input()
	print("Cuantos ingredientes lleva:")
	n = int(input())
	ingredientes = [None]
	for i in range(0,n):
		print(f"Introduce el ingrediente {i + 1}")
		entrada = input()
		ingredientes.insert(i,entrada)
	ingredientes.pop()
	salida = [nombre, tipo, ingredientes]
	return(salida)

def añadir_menu():
	pass

def random_menu():
	pass