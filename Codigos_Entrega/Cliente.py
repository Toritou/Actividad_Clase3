import requests

#URL de la API
URL_API = 'http://54.83.174.173:8080/lista_total'

#Funcion para obtener y mostras las tareas pendientes
def ObtenerTodos():
    try:
        Respuesta = requests.get(URL_API)
        #Exepcion para los errores http
        Respuesta.raise_for_status()
        Tareas    = Respuesta.json()
        print("Tareas pendientes: ")
        for tarea in Tareas:
            print(f"ID: {tarea['ID']}, Tarea: {tarea['Tarea']}, Completado: {tarea['Completado']}")
    #Manejo de errores para diferentes excepciones
    except requests.RequestException as e:
        print(f"Error al obtener las tareas pendientes: {e}")

#Funcion para agregar una nueva tarea pendiente
def AgregarTarea(tarea):
    try:
        Respuesta = requests.post(URL_API, json={'tarea': tarea})
        Respuesta.raise_for_status()
        NuevaTarea = Respuesta.json()
        print(f"Tarea añadida: {NuevaTarea}")
    except requests.RequestException as e:
        print(f"Error al agregar la tarea: {e}")

#Funcion para actualizar una tarea pendiente existente
def ActualizarTarea(ID, tarea=None, completado=None):
    data = {}
    if tarea is not None:
        data['tarea'] = tarea
    if completado is not None:
        data['completado'] = completado

    try:
        Respuesta = requests.put(f"{URL_API}/{ID}", json=data)
        Respuesta.raise_for_status()
        TareaActualizada = Respuesta.json()
        print(f"Tarea actualizada: {TareaActualizada}")
    except requests.RequestException as e:
        print(f"Error al actualizar la tarea: {e}")

#Funcion para eliminar una tarea pendiente con el ID especificado
def EliminarTarea(ID):
    try:
        Respuesta = requests.delete(f"{URL_API}/{ID}")
        Respuesta.raise_for_status()
        print("Tarea eliminada.")
    except requests.RequestException as e:
        print(f"Error al eliminar la tarea: {e}")

#Funcion principal para interactuar con el usuario
def main():
    #Bucle para que no se cierre el programa al terminar una ejecucion
    while True:
        print("|-----------------------------------|")
        print("|        |Gestion de tareas|        |")
        print("|-----------------------------------|")
        print("| [1] Obtener las tarea pendientes  |")
        print("| [2] Agregar tarea                 |")
        print("| [3] Actualizar tarea              |")
        print("| [4] Eliminar tarea                |")
        print("|-----------------------------------|")

        Opcion = input("Seleccione una opcion: ")

        if Opcion == '1':
            ObtenerTodos()
        elif Opcion == '2':
            Tarea = input("Ingrese la tarea: ")
            AgregarTarea(Tarea)
        elif Opcion == '3':
            ID = int(input("Ingrese el ID de la tarea: "))
            Tarea = input("Ingrese la nueva tarea: ")
            Completado = input("Ingrese el estado de la tarea (Terminado/Pendiente): ")
            ActualizarTarea(ID, Tarea, Completado)
        elif Opcion == '4':
            ID = int(input("Ingrese el ID de la tarea a eliminar: "))
            EliminarTarea(ID)
        else:
            print("Ingrese una opcion valida (1, 2, 3, 4)")

if __name__ == '__main__':
    main()



