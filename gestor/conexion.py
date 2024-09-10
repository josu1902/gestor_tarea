## esto solo es la conexion 
import pymysql


conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='josue_albo',
    database='gestor'
)


cursor = conexion.cursor()

def mostrar_tareas():

    cursor.execute('SELECT * FROM tareas')

    tareas = cursor.fetchall()
    print(tareas)
#cursor.close()

#conexion.close()
