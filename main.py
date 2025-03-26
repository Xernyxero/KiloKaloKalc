import bbdd as bd
import executable as exe
import os

ingredientes, recetas, usuarios, dietas = bd.actualizar_todo()

user = None
comando = input("¿Quieres añadir un nuevo usuario o elegir uno existene?\n")

while comando != "elegir usuario":

    if comando == "nuevo usuario":
        usuario = exe.pedir_datos_user()
        bd.guardar_datos_excel(usuario, "Usuarios")
        alimentos, recetas, usuarios, dietas = bd.extraer_datos_excel()
    else:
        comando = input("❌ Error: Solo puedes introducir entre 'nuevo usuario' o 'elegir usuario'\n")

print("Estos son los usuarios disponibles:")
for usuario in usuarios:
    print(usuario.nombre)

while user == None:
    nombre = input()
    for usuario in usuarios:
        if nombre == usuario.nombre:
            user = usuario
            print("Has seleccionado el usuario:", user)
        else:
            print(f"⚠️ Usuario '{nombre}' no encontrado en la base de datos.")

comando = "help"
while comando != "stop":
    os.system('cls')

    if comando == "help":

        print("---------- Estas son algunas de las opciones que puedes hacer ----------")
        print("- ver datos -")
        print("- nuevo usuario -")
        print("- nuevo alimento -")
        print("- nueva receta -")
        print("- nueva dieta -")
        print("- ajustar receta -")
        print("- help -")
        print("- stop -")

    if comando == "ver datos":

        print("📌 Usuarios:")
        for usuario in usuarios:
            print(usuario)
        print("📌 Alimentos:")
        for ingrediente in ingredientes:
            print(ingrediente)
        print("📌 Recetas:")
        for receta in recetas:
            print(receta)
        print("📌 Dietas:")
        for dieta in dietas:
            print(dieta)

    if comando == "nuevo alimento":
        ingrediente = exe.pedir_datos_alimentos()
        bd.guardar_datos_excel(ingrediente, "Alimentos")
        ingredientes, recetas, usuarios, dietas = bd.actualizar_todo()

    if comando == "nueva receta":
        print("------ Estos son los ingredientes disponibles ------")
        print([ingrediente for ingrediente in ingredientes])
        receta = exe.pedir_datos_recetas()
        bd.guardar_datos_excel(receta, "Recetas")
        ingredientes, recetas, usuarios, dietas = bd.actualizar_todo()

    if comando == "nuevo usuario":
        usuario = exe.pedir_datos_user()
        bd.guardar_datos_excel(usuario, "Usuarios")
        ingredientes, recetas, usuarios, dietas = bd.actualizar_todo()

    if comando == "nueva dieta":
        print("------ Estos son los desayunos y meriendas disponibles ------")
        print([receta for receta in recetas if receta.tipo == "desayuno"])
        print("------ Estos son los almuerzos y cenas disponibles ------")
        print([receta for receta in recetas if receta.tipo == "comida"])
        dieta = exe.pedir_datos_dietas()
        bd.guardar_datos_excel(dieta, "Dietas")
        ingredientes, recetas, usuarios, dietas = bd.actualizar_todo()

    if comando == "ajustar dieta":
        print("------ Estas son las dietas disponibles ------")
        print([dieta for dieta in dietas])
        while True:
            eleccion = input()
            for dieta in dietas:
                if eleccion == dieta.nombre:
                    print("Has seleccionado:", dieta)
                    eleccion = dieta
                    break
            print(f"⚠️ Dieta '{eleccion}' no encontrada en la base de datos.")

        for receta in eleccion:
            receta.get_cantidades(user)
            print(receta.ingrediente_cantidad)

    if comando == "ajustar receta":
        print("------ Estas son las recetas disponibles ------")
        print([receta for receta in recetas])
        salir = False
        while salir == False:
            eleccion = input()
            for receta in recetas:
                if eleccion == receta.nombre:
                    print("Has seleccionado:", receta)
                    receta.get_cantidades(user)
                    print(receta.ingrediente_cantidad)
                    print(receta.macros)
                    print("Estos son los macros objetivos", user.macros)
                    salir = True
                    break
            if salir:
                break
            print(f"⚠️ Receta '{eleccion}' no encontrada en la base de datos.")

    comando = input()