from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connection import connect, disconnect

app = Flask(__name__)
CORS(app)

@app.route('/operador', methods=["GET"])
def operador():
    try:
        connection, cursor = connect()

        query = "SELECT * FROM operador;"
        cursor.execute(query)
        respuesta = cursor.fetchall()
        disconnect(connection, cursor)

        return jsonify(respuesta)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/clientes', methods=["POST"])
def guardar_datos():
    try:
        data = request.get_json()

        nombre = data["Nombre"]
        operacion= data["Operacion"]
        monto= data["Monto"]

        connection, cursor = connect()
        query = "INSERT INTO clientes (nombre, operacion, monto) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, operacion, monto))
        connection.commit()
        disconnect(connection, cursor)

        return jsonify({"message": "Datos guardados correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
