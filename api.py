from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get-link', methods=['POST'])
def get_teams_link():
    try:
        # Verifica si el contenido tiene el tipo 'text/html'
        content_type = request.content_type
        if content_type not in ['text/html', 'application/x-www-form-urlencoded']:
            return jsonify({"error": "Unsupported Media Type: Please send HTML content with Content-Type 'text/html'"}), 415

        # Obtiene el contenido HTML del cuerpo de la solicitud
        html_content = request.data.decode('utf-8')

        # Procesa el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encuentra todos los enlaces (elementos <a>)
        all_links = soup.find_all('a')

        # Verifica si hay al menos dos enlaces y extrae el segundo
        if len(all_links) >= 2:
            teams_link = all_links[1].get('href', None)  # Obtiene el href del segundo enlace
            if teams_link:
                return jsonify({"teams_link": teams_link}), 200

        return jsonify({"error": "No se encontró un segundo enlace en el contenido HTML."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
