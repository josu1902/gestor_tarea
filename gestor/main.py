
import funciones as f

diccionario = {1:"Agregar tareas", 2: "Actualizar tareas", 3: "Eliminar tareas", 4: "Mostrar prioridad", 5: "Mostrar categorias", 6: "Salir"}
print(diccionario)


bandera = True

while bandera:
    opcion = int(input("Ingresa una opcion: "))
    if opcion in diccionario:
        if opcion == 1:
            f.agregar_tareas()
        elif opcion == 2:
            f.actualizar_tarea()
        elif opcion == 3:
            f.eliminar_tarea()
        elif opcion == 4:
            f.mostrar_prioridad()
        elif opcion == 5:
            f.mostrar_categoria()
        elif opcion == 6:
            print("Saliendo....")
            break
    else:
        print("Ingresa una opcion valida")