import sqlite3

# Connexion
conn = sqlite3.connect('cinema.sqlite')
c = conn.cursor()

# Afficher toutes les tables
print("=== TABLES DISPONIBLES ===")
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
for table in tables:
    print(f"- {table[0]}")

# Afficher le contenu de chaque table
for table in tables:
    nom_table = table[0]
    print(f"\n{'='*50}")
    print(f"TABLE: {nom_table}")
    print('='*50)
    
    c.execute(f"SELECT * FROM {nom_table}")
    lignes = c.fetchall()
    
    if lignes:
        for ligne in lignes:
            print(ligne)
    else:
        print("(Vide)")

conn.close()