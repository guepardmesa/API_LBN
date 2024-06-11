from flask import Flask, jsonify
import sqlite3
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/siren/<siren>', methods=['GET'])
def get_data(siren):
    conn = sqlite3.connect('egapro.db') # Connexion à la base de données SQLite
    cursor = conn.cursor()
     # Exécution de la requête SQL pour récupérer les données du SIREN
    cursor.execute('SELECT data FROM egapro WHERE siren = ?', (siren,))
    result = cursor.fetchone()
    conn.close() # Fermeture de la connexion à la base de données
    # Vérification si des données ont été trouvées pour le SIREN donné
    if result:
        # Renvoie les données au format JSON si trouvées
        return jsonify({'data': result[0]})
    else:
    # Renvoie un message d'erreur avec un code 404 si le SIREN n'est pas trouvé
        return jsonify({'error': 'SIREN non trouvé'}), 404

# Configuration de Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "EgaPro API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
# Exécution de l'application Flask en mode debug si ce script est exécuté directement
if __name__ == '__main__':
    app.run(debug=True)
