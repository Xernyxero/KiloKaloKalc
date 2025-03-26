import numpy as np
from scipy.optimize import lsq_linear

class Ingrediente:
    def __init__(self, nombre, kcal, grasas, saturadas, hidratos, azucares, proteinas, precio):
        self.nombre = nombre
        self.kcal = kcal
        self.grasas = grasas
        self.saturadas = saturadas
        self.hidratos = hidratos
        self.azucares = azucares
        self.proteinas = proteinas
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre}"

class Receta:
    def __init__(self, nombre, tipo, ingredientes,  lista_ingredientes):
        self.nombre = nombre
        self.ingredientes = [ing for ing in lista_ingredientes if ing.nombre in ingredientes]
        self.cantidades = [0]*len(self.ingredientes)
        self.ingrediente_cantidad = dict(zip(self.ingredientes,self.cantidades))
        self.tipo = tipo
        self.proporcion = 0
        if self.tipo == "desayuno":
        	self.proporcion = 0.2
        if self.tipo == "almuerzo":
        	self.proporcion = 0.3

    def __repr__(self):
        return f"{self.nombre}"

    def get_cantidades(self, user):
    	matriz_macros = []
    	#filas = ingredientes, columnas = [grasas, hidratos, protes, kcal]
    	for ing in self.ingredientes:
    		fila = [ing.grasas, ing.hidratos, ing.proteinas, ing.kcal]
    		matriz_macros.append(fila)

    	#Trasnformamos los datos en formato array (necesitamos la traspuesta)
    	#filas = macros, columnas = ingredientes
    	A = np.transpose(np.array(matriz_macros))
    	#Construyo el vector de terminos independientes de la ecuacion Ax=b.
    	b = self.proporcion * np.array([user.grasas, user.hidratos, user.proteinas, user.kcal])

    	#Calculamos la solución con el método de optimización lineal
    	#El bounds es para el rango de valores posibles de la solución
    	result = lsq_linear(A, b, bounds=(0.0001,np.inf))

    	if result.success:
    		self.cantidades = result.x.tolist()
    		self.ingrediente_cantidad = dict(zip(self.ingredientes, self.cantidades))
    	else:
    		print("No se ha encontrado una solución válida:", result.message)
    		return

    	grasas = sum(ing.grasas * cantidad for ing, cantidad in self.ingrediente_cantidad.items())
    	hidratos = sum(ing.hidratos * cantidad for ing, cantidad in self.ingrediente_cantidad.items())
    	proteinas = sum(ing.proteinas * cantidad for ing, cantidad in self.ingrediente_cantidad.items())
    	kcal = sum(ing.kcal * cantidad for ing, cantidad in self.ingrediente_cantidad.items())
    	self.macros = {"grasas": grasas, "hidratos":hidratos, "proteinas": proteinas, "kcal": kcal}

class Usuario:
	def __init__(self, nombre, edad, sexo, peso, altura, actividad, objetivo):
		self.nombre = nombre
		self.edad = edad
		self.sexo = sexo	
		self.peso = peso
		self.altura = altura
		self.actividad = actividad
		self.factor_act = 1.025 + 0.175*actividad
		self.objetivo = objetivo
		self.get_tmb()
		self.get_macros_diarios()

	def get_tmb(self):
		# TMB = Tasa de Metabolismo Basal
		# GET = Gasto Energético Total		
		if self.sexo == "H":
			self.tmb = 10*self.peso + 6.25*self.altura - 5*self.edad + 5
		if self.sexo == "M":
			self.tmb = 10*self.peso + 6.25*self.altura - 5*self.edad - 16
		self.get = self.tmb*self.factor_act

	def get_macros_diarios(self):
		#todos los macros calculados estan en gramos
		if self.objetivo == "D":
			self.kcal = self.get - 300
			self.proteinas = 2.2 * self.peso # El peso debe estar en kg 
			self.grasas = 0.25/9 * self.kcal # El factor 1/9 pasa de kcal de grasas a gr de grasas.
			self.hidratos = (self.kcal - self.grasas * 9 - self.proteinas * 4) / 4 # El factor 1/4 pasas de kcal de hidratos a gr de hidratos
		elif self.objetivo == "M":
			self.kcal = self.get
			self.proteinas = 1.9 * self.peso
			self.grasas = 0.25/9 * self.kcal
			self.hidratos = (self.kcal - self.grasas * 9 - self.proteinas * 4) / 4
		elif self.objetivo == "V":
			self.kcal = self.get + 300
			self.proteinas = 1.9 * self.peso
			self.grasas = 0.225/9 * self.kcal
			self.hidratos = (self.kcal - self.grasas * 9 - self.proteinas * 4) / 4
		self.macros = {"grasas": self.grasas, "hidratos":self.hidratos, "proteinas": self.proteinas, "kcal": self.kcal}

	def __repr__(self):
        	return f"Usuario({self.nombre}, {self.edad} años, {self.peso}kg, {self.altura}cm,)"



