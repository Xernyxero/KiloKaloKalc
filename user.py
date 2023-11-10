""" VARIABLES DE USO"""

keys_macros = ["Grasas", "Saturadas", "Hidratos", "Azucares", "Proteinas", "Kcal"]
proporciones = dict(zip(["almuerzo", "comida", "merienda","cena"],[0.2,0.3,0.2,0.3]))

values_definicion = [0.13, 0.05,0.35,0.05,0.52,2222]
values_volumen = [ 0.13, 0.05, 0.52, 0.05, 0.35, 3333]

definicion = dict(zip(keys_macros, values_definicion))
volumen = dict(zip(keys_macros, values_volumen))