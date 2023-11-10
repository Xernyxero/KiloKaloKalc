import user as us
import bbdd as bd
import executables as exe
from classes import *

alimentos, recetas = bd.json_to_obj()
comando = ""

prueba = bd.is_object("pollo", alimentos)
print(prueba)
print(type(prueba))	

while comando != "stop":
	comando = input()

	if comando == "help":
		print("Estas son algunas de las opciones que puedes hacer:")
		print("nuevo alimento")
		print("nueva receta")
		print("ver datos")
		print("ajustar")
		print("stop")

	if comando == "nuevo alimento":
		nuevo = exe.nuevo_alimento()
		bd.guardar_lista(nuevo,"alimentos")

	if comando == "nueva receta":
		nuevo = exe.nueva_receta()
		bd.guardar_lista(nuevo,"recetas")

	if comando == "ver datos":
		alimentos, recetas = bd.json_to_obj()
		print("-------INGREDIENTES--------")
		for elemento in alimentos:
			print(elemento)
			print(type(elemento))
		print("-------RECETAS--------")
		for elemento in recetas:
			print(elemento)
			print(type(elemento))

	if comando == "ajustar":
		print("¿Que receta quieres ajustar?:")
		for i in range(0, len(recetas)):
			print(recetas[i])
			entrada = input()
			if f"{entrada}_obj" == f"{recetas[i]}":
				recetas[i].ajustar_receta(us.definicion,alimentos)
		if isinstance(entrada, str):
			print("Tu entrada no es valida")