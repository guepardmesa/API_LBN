import sqlite3

# Création de la base de données SQLite
conn = sqlite3.connect('egapro.db')
cursor = conn.cursor()

# Création de la table EgaPro
cursor.execute('''
CREATE TABLE IF NOT EXISTS egapro (
    siren TEXT PRIMARY KEY,
    annee INTEGER,
    data TEXT
)
''')
conn.commit()
conn.close()
