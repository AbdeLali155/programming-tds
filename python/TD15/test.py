from cinema_db import *

# Connexion et création des tables
conn, c = AccederBD('cinema.sqlite')
CreerTable1(c)
CreerTable2(c)
CreerTable3(c)

# Ajoutez quelques données de test
print("=== Ajout de données ===")
c.execute("INSERT INTO FILM VALUES (1, 'Inception', 'Christopher Nolan', 2010)")
insert_acteur(c, 1, 'DiCaprio', 'Leonardo')
insert_acteur(c, 2, 'anashani', 'abmola')

c.execute("INSERT INTO FILMOGRAPHIE VALUES (1, 1, 'Cobb', 20000000)")

ValiderTrans(conn)

# Testez l'affichage
print("\n=== Affichage des tables ===")
affiche_table(c, 'FILM')
affiche_table(c, 'ACTEUR')
affiche_table(c, 'FILMOGRAPHIE')

FermerConnex(conn)
print("\n✓ Tout fonctionne !")