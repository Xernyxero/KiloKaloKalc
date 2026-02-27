def pedir_datos_user():
	while True: #Se repetirá hasta que los datos sean correctos
		try:
			user = input("Usuario: ")
			sexo = input("Hombre o Mujer (H o M): ")
			edad = int(input("Edad: "))
			peso = float(input("Peso (kg): "))
			altura = float(input("Altura (cm): "))

			print("Actividad Fisica diaria:")
			print("1: poco o nada")
			print("2: de 1-3 días a la semana")
			print("3: de 3-5 días a la semana")
			print("4: 6-7 días a la semana")
			print("5: Acividad intensa y diaria")

			actividad = float(input())
			objetivo = input("¿Definición (D), Mantenimiento (M) o Volumen (V)?")		
			
			return(user, edad, sexo, peso, altura, actividad, objetivo)

		except ValueError:
    			print("Error: Asegúrate de ingresar los valores correctos")

def pedir_datos_alimentos():
	while True:
		try:
			nombre = input("Alimento: ")
			print("Introduzca todos los valores por cada 100gr de peso")
			kcal = float(input("kCal: "))
			grasas = float(input("Grasas: "))
			saturadas = float(input("Saturadas: "))
			hidratos = float(input("Hidratos: "))
			azucares = float(input("Azucares: "))
			proteinas = float(input("Proteinas: "))
			precio = float(input("Precio: "))
			return (nombre, kcal, grasas, saturadas, hidratos, azucares, proteinas, precio)
	    
		except Exception as e:
	    		print(f"❌ Error al leer los datos: {e}")

def pedir_datos_recetas():
	while True:
		try:
			receta = [input("Receta: ")]
			receta.append(input("desayuno o almuerzo:"))
			n = int(input("Cuantos ingredientes lleva: "))
			for i in range(1, n + 1):
				print("Ingrediente", i)
				receta.append(input())
			return receta
	    
		except Exception as e:
	    		print(f"❌ Error al leer los datos: {e}")

def pedir_datos_dietas():
	while True:
		try:
			dieta = []
			n = int(input("Cuantas recetas lleva: "))
			for i in range(1, n + 1):
				print("Receta", i)
				dieta.append(input())
			return dieta
		except Exception as e:
	    		print(f"❌ Error al leer los datos: {e}")