import pandas as pd
from classes import *

hojas = ["Alimentos", "Recetas", "Usuarios", "Dietas"]  # Lista de hojas definidas
archivo = "Datos.xlsx"

def guardar_datos_excel(datos, nombre_hoja):

    if nombre_hoja not in hojas:
        print(f"⚠️ Error: '{nombre_hoja}' no es una hoja válida. Debe ser una de {hojas}.")
        return

    try:
        # Intentar leer los datos existentes
        try:
            df_existente = pd.read_excel(archivo, sheet_name=nombre_hoja, header=None)
        except FileNotFoundError:
            df_existente = pd.DataFrame()  # Si el archivo no existe, creamos un DataFrame vacío
        except ValueError:
            df_existente = pd.DataFrame()  # Si la hoja no existe aún

        # Crear un DataFrame con el nuevo registro
        df_nuevo = pd.DataFrame([datos])  # Convertir la lista a un DataFrame de una fila

        # Concatenar los datos nuevos con los existentes
        df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)

        # Guardar sin borrar otras hojas
        with pd.ExcelWriter(archivo, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            df_final.to_excel(writer, sheet_name=nombre_hoja, index=False, header=False)

        print(f"✅ Nuevo registro añadido a la hoja '{nombre_hoja}' en '{archivo}'.")

    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")

def extraer_datos_excel():

    datos_extraidos = []

    try:
        for hoja in hojas:
            try:
                df = pd.read_excel(archivo, sheet_name=hoja, header=0)
                datos_extraidos.append(df.values.tolist())  # Agregar como lista de listas
            except ValueError:
                datos_extraidos.append([])  # Si la hoja no existe, devuelve una lista vacía

        #print(f"✅ Datos extraídos correctamente de '{archivo}'.")
        return datos_extraidos  # Retorna una lista de listas(1 por cada hoja) de listas(1 por cada elemento de dicha hoja)

    except Exception as e:
        print(f"❌ Error al leer los datos: {e}")
        return [[] for _ in hojas]  # Retorna una lista de listas vacías en caso de error

def actualizar_todo():
    dietas_obj = []
    alimentos, recetas, usuarios, dietas = extraer_datos_excel()
    ingredientes_obj = [Ingrediente(*alimento) for alimento in alimentos]
    recetas_obj = [Receta(receta[0], receta[1], receta[2:], ingredientes_obj) for receta in recetas]
    usuarios_obj = [Usuario(*usuario) for usuario in usuarios]
    for dieta in dietas:
        dietas_obj.append([receta for receta in recetas_obj if receta.nombre in dieta])
    return(ingredientes_obj, recetas_obj, usuarios_obj, dietas_obj)