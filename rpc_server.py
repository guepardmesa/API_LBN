from xmlrpc.server import SimpleXMLRPCServer
import sqlite3
#Récupère des dnnées de la base de donées en utilisant un numéro SIREN
def get_data_by_siren(siren):
    
    #on se connecte à la BD SQLite 
    conn = sqlite3.connect('egapro.db')
    cursor = conn.cursor()
    
    #Exécute une requête SQL pour sélectionner les données où le SIREN est correspondant
    cursor.execute('SELECT data FROM egapro WHERE siren = ?', (siren,))
    result = cursor.fetchone()
    
    #Fermeture de la connexion à la base de données 
    conn.close()
    
    #Retourne les données si trouvées, sinon retourne message erreur
    if result:
        return result[0]
    else:
        return "SIREN non trouvé"
    
#Création du serveur  XML-RPC écoutant sur localhoast:9000
server = SimpleXMLRPCServer(('localhost', 9000))

#Affichage d'un message pour indiquer que le serveur est en cours exécution
server.register_function(get_data_by_siren, 'get_data_by_siren')
print("Serveur RPC en cours d'exécution sur le port 9000...")

#Démarrage du serveur
server.serve_forever()
