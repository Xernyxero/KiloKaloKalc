import user as us
from math_shit import cherni_function
import bbdd as bd

class Alimento:
	def __init__(self, datos):
		self.nombre = datos[0]
		self.tipo = datos[1]
		self.valor_nutricional = dict.fromkeys(us.keys_macros)

		for i,valor in enumerate(datos[2:8]):
			self.valor_nutricional[us.keys_macros[i]] = valor

	def __str__(self):
		return(f"{self.nombre}_obj")

class Receta:
	def __init__(self, datos):
		self.nombre = datos[0]
		self.tipo = datos[1]
		self.ingredientes = datos[2]
		self.cantidades = [0]*len(self.ingredientes)
		self.ingrediente_cantidad = dict(zip(self.ingredientes,self.cantidades))
		self.macros_totales = dict.fromkeys(us.keys_macros)

	def __str__(self):
		return(f"{self.nombre}_obj")

	def get_macros(self,lista_alimentos):
		total = []
		for macro in us.keys_macros:
			macro_total = 0
			for ingrediente,cantidad in self.ingrediente_cantidad.items():
				ingrediente_obj = bd.is_object(ingrediente, lista_alimentos)
				print(cantidad)
				macro_total += cantidad * ingrediente_obj.valor_nutricional.get(macro)
				total.append(macro_total)
		self.macros_totales.update(total)

	def print_macros(self):
		for k,v in self.macros_totales.items():
			print(f'------{k}: {v}')

	def ajustar_receta(self, programa,lista_alimentos):
		macros_importantes = ["Grasas", "Hidratos", "Proteinas"]
		comida = float(us.proporciones.get(self.tipo))
		matriz_macros = []
		lista_kcal_aliment = []
		proporciones_programa = [programa.get("Grasas"), programa.get("Hidratos")]
		objetivo_kcal = float(programa.get("Kcal"))

		for ingrediente in self.ingredientes:
			ingrediente_obj = bd.is_object(ingrediente,lista_alimentos)
			macros_ingredientes = [ingrediente_obj.valor_nutricional.get(m) for m in macros_importantes]
			matriz_macros.append(macros_ingredientes)
			kcal_alimento = ingrediente_obj.valor_nutricional.get("Kcal")
			lista_kcal_aliment.append(kcal_alimento)

		print(lista_kcal_aliment)
		cantidades = cherni_function(comida, matriz_macros, lista_kcal_aliment, proporciones_programa, objetivo_kcal)
		print(cantidades)
		#self.cantidad = cantidades
		#self.get_macros(lista_alimentos)
		#self.print_macros()

class Menu:
	pass

class Usuario:
	def __init__(self,datos):
		self.nick = datos[0]
		self.programa = datos[1]