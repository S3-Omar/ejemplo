from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/get-link', methods=['POST'])
def get_teams_link():
    try:
        # Verifica si el contenido tiene el tipo 'text/html'
        content_type = request.content_type
        if content_type != 'text/html':
            return jsonify({
                "error": "Unsupported Media Type",
                "message": "Please send HTML content with Content-Type 'text/html'"
            }), 415

        # Obtiene el contenido HTML del cuerpo de la solicitud
        html_content = request.data.decode('utf-8')

        # Procesa el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encuentra todos los enlaces (elementos <a>)
        all_links = soup.find_all('a')

        # Verifica si hay al menos dos enlaces y extrae el segundo
        if len(all_links) >= 2:
            teams_link = all_links[1].get('href')  # Obtiene el href del segundo enlace
            if teams_link:
                return jsonify({"teams_link": teams_link}), 200

        return jsonify({
            "error": "No se encontró un segundo enlace en el contenido HTML.",
            "message": "Proporcione un HTML válido con al menos dos enlaces."
        }), 404

    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    # Obtiene el puerto desde la variable de entorno o usa el puerto 5000
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
