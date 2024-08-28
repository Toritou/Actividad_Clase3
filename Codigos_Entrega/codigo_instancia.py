# Importación de librerías correspondientes
from flask import Flask, jsonify, request

# Creación de la instancia como en el tutorial.
app = Flask(__name__)

# Lista vacía para almacenar las tareas pendientes.
tareas = []
# Asignar un número a las tareas
id_counter = 1

# Obtener la lista de tareas con el método GET + su respectiva función
@app.route('/lista_total', methods=['GET'])
def obtener_todos():
    return jsonify(tareas), 200

# Poder agregar una nueva tarea a la lista de pendientes con el método POST + su respectiva función
@app.route('/lista_total', methods=['POST'])
def agregar():
    global id_counter
    data = request.get_json()
    if not data or 'tarea' not in data:
        return jsonify({'error': 'No hay tarea proporcionada'}), 400

    nuevo_todo = {
        'ID': id_counter,
        'Tarea': data['tarea'],
        'Completado': False
    }
    tareas.append(nuevo_todo)
    id_counter += 1
    return jsonify(nuevo_todo), 201

# Poder actualizar las tareas pendientes con el método PUT + su respectiva función
@app.route('/lista_total/<int:id>', methods=['PUT'])
def actualizar_lista(id):
    data = request.get_json()
    tarea = next((t for t in tareas if t['ID'] == id), None)
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404

    if 'tarea' in data:
        tarea['Tarea'] = data['tarea']
    if 'completado' in data:
       tarea['Completado'] = data['completado']
    return jsonify(tarea), 200

        # Para poder eliminar las tareas sin que afecte a las demás con el método DELETE + su función
@app.route('/lista_total/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['ID'] != id]
    return '', 204

        # Ejecución en Flask en el puerto 8080
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

