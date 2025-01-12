from flask import *

app = Flask(__name__)

# Ruta para recibir y mostrar la data via GET
@app.route('/data', methods=['GET'])
def get_data():
    # Obtener los parámetros de la query string
    data = request.args.to_dict()
    
    # Si no se recibe data, retornamos un mensaje de error
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    # Retornar la data recibida como JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
