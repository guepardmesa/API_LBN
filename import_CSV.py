import sqlite3
import csv

# Connexion à la base de données
conn = sqlite3.connect('egapro.db')
cursor = conn.cursor()

# Lecture des données CSV
with open('/mnt/data/index-egalite-fh.xlsx', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        siren = row['SIREN']
        annee = int(row['Année'])
        data = str(row)
        
        cursor.execute('''
        INSERT OR REPLACE INTO egapro (siren, annee, data) VALUES (?, ?, ?)
        ''', (siren, annee, data))

conn.commit()
conn.close()
