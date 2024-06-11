from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import sqlite3

# Définition du service EgaProService qui hérite de ServiceBase
class EgaProService(ServiceBase):
    # Définition de la méthode RPC pour obtenir les données par SIREN
    @rpc(Unicode, _returns=Unicode)
    def get_data_by_siren(ctx, siren):
        # Connexion à la base de données SQLite
        conn = sqlite3.connect('egapro.db')
        cursor = conn.cursor()
        
        # Exécution de la requête SQL pour obtenir les données correspondant au SIREN
        cursor.execute('SELECT data FROM egapro WHERE siren = ?', (siren,))
        result = cursor.fetchone()
        
        # Fermeture de la connexion à la base de données
        conn.close()
        
        # Vérification si le résultat existe et retour de celui-ci
        if result:
            return result[0]
        else:
            return "SIREN non trouvé"

# Création de l'application SOAP en spécifiant le service et les protocoles d'entrée et de sortie
application = Application([EgaProService], 'egapro.service', in_protocol=Soap11(), out_protocol=Soap11())

# Création de l'application WSGI pour le service SOAP
wsgi_application = WsgiApplication(application)

# Démarrage du serveur WSGI pour écouter sur le port 8000
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_application)
    print("Serveur SOAP en cours d'exécution sur le port 8000...")
    server.serve_forever()
