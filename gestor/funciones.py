
import conexion as c

def prioridad():
    #id_prioridad = int(input("ID: "))
    nombre = input("Ingresa el nombre(alta, media, baja): ")
    nivel = int(input("Ingresa el nivel (1, 2, 3)"))


    consulta = "INSERT INTO prioridades(nombre, nivel) VALUES(%s, %s)"
    c.cursor.execute(consulta, (nombre, nivel))

    c.conexion.commit()

def categorias():
    
    nombre = input("Nombre: ")
    consulta = "INSERT INTO categorias(nombre) VALUES (%s)"
    c.cursor.execute(consulta,(nombre,))
    c.conexion.commit()


def agregar_tareas():
    titulo = input("Titulo de la tarea: ")
    descripcion = input("Descripcion de  la tarea: ")
    fecha_venc = input("Fecha de vencimiento (YYYY-MM-DD): ")
    id_prioridad = int(input("ID de la prioridad: "))
    id_categoria = int(input("ID de la categoría: "))


    consulta = "INSERT INTO tareas (titulo, descripcion, fecha_venc, id_prioridad, id_categoria) VALUES (%s, %s, %s, %s, %s)"
    c.cursor.execute(consulta, (titulo, descripcion, fecha_venc, id_prioridad, id_categoria))
    c.conexion.commit() 

    

def mostrar_prioridad():
    diccionario = {1: "Alta", 2: "Media", 3: "Baja"}
    print(diccionario)
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        c.cursor.execute("SELECT * FROM tareas WHERE id_prioridad = 1")
        tareas = c.cursor.fetchall()
        #c.conexion.commit()
        print(tareas)

    elif opcion == 2:
        c.cursor.execute("SELECT * FROM tareas WHERE id_prioridad = 2")
        tareas = c.cursor.fetchall()
        print(tareas)

    elif opcion == 3:
        c.cursor.execute("SELECT * FROM tareas WHERE id_prioridad = 3")
        tareas = c.cursor.fetchall()
        print(tareas)
    else:
        print("Opcion incorrecta")

def mostrar_categoria():
    diccionario = {1: "Trabajo", 2: "Estudio", 3: "Salud", 4: "Finanzas", 5: "Proyectos", 6: "Otros"}
    print(diccionario)
    opcion = int(input("Elige una opción: "))

    
    if opcion in diccionario:
        c.cursor.execute(f"SELECT * FROM tareas WHERE id_categoria = {opcion}")
        tareas = c.cursor.fetchall()
        print(tareas)
    else:
        print("Opción no válida.")


def actualizar_tarea():

    c.cursor.execute('SELECT * FROM tareas')

    tareas = c.cursor.fetchall()
    for tarea in tareas:
        print(tarea)
    id_tar = int(input("Ingresa el id que quieres actualizar: "))
    ids_tareas = [tarea[0] for tarea in tareas] # creamos una lista de todos los id de las  tareas
    if id_tar in ids_tareas:
        titulo = input("Ingresa el nuevo titulo: ")
        des = input("Ingresa la nueva descrpcion: ")
        fecha = input("Fecha de vencimiento (YYYY-MM-DD): ")
        priorid = int(input("Ingresa la prioridad de la tarea: "))
        categ = int(input("Ingresa la categoria de la tarea: "))
        #c.cursor.execute("SELECT * FROM tareas WHERE id_tarea = id_tar")
        c.cursor.execute("""
            UPDATE tareas
            SET titulo = %s,
                descripcion = %s,
                fecha_venc = %s,
                id_prioridad = %s,
                id_categoria = %s
            WHERE id_tarea = %s""",
            (titulo, des, fecha, priorid, categ, id_tar))
        print("Se agrego")
        c.conexion.commit()
    else:
        print("El ID es incorrecto")
    
    c.cursor.close()
    c.conexion.close()

def eliminar_tarea():
    c.cursor.execute('SELECT * FROM tareas')
    tareas = c.cursor.fetchall()
    for tarea in tareas:
        print(tarea)
    id_tar = int(input("Ingresa el ID de la tarea que quieras borrar: "))
    ids_tareas = [tarea[0] for tarea in tareas] 
    if id_tar in ids_tareas:
        c.cursor.execute('DELETE FROM tareas WHERE id_tarea = %s', (id_tar,))
        print("Se ha eliminado correctamente")
        c.conexion.commit()
    else:
        print("El ID no se encuentra")

# que son las inyecciones
