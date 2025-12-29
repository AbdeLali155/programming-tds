import sqlite3
import os


def AccederBD(maBase):
    conn = sqlite3.connect(maBase)
    c = conn.cursor()
    print(f"✓ Connexion établie avec {maBase}")
    return conn, c


def CreerTable1(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILM (
        idFilm INTEGER PRIMARY KEY,
        titre TEXT NOT NULL,
        realisateur TEXT,
        annee INTEGER
    )''')
    print("✓ Table FILM créée")

def CreerTable2(c):
    c.execute('''CREATE TABLE IF NOT EXISTS ACTEUR (
        idActeur INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL
    )''')
    print("✓ Table ACTEUR créée")

def CreerTable3(c):
    c.execute('''CREATE TABLE IF NOT EXISTS FILMOGRAPHIE (
        idActeur INTEGER,
        idFilm INTEGER,
        role TEXT,
        salaire REAL,
        PRIMARY KEY (idActeur, idFilm),
        FOREIGN KEY (idActeur) REFERENCES ACTEUR(idActeur),
        FOREIGN KEY (idFilm) REFERENCES FILM(idFilm)
    )''')
    print("✓ Table FILMOGRAPHIE créée")
def rech_personne(c, nom, prenom):
    c.execute("SELECT * FROM ACTEUR WHERE nom=? AND prenom=?", (nom, prenom))
    resultat = c.fetchone()
    return resultat is not None

def insert_acteur(c, id, nom, prenom):
    if not rech_personne(c, nom, prenom):
        c.execute("INSERT INTO ACTEUR (idActeur, nom, prenom) VALUES (?, ?, ?)", 
                  (id, nom, prenom))
        print(f"✓ Acteur {prenom} {nom} ajouté avec succès")
    else:
        print(f"⚠ L'acteur {prenom} {nom} existe déjà dans la base")

def affiche_table(c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    resultats = c.fetchall()
    print(f"\n=== Contenu de la table {nomTable} ===")
    if resultats:
        for row in resultats:
            print(row)
    else:
        print("(Aucune donnée)")

def affiche_film(c, id):
    c.execute("SELECT * FROM FILM WHERE idFilm=?", (id,))
    film = c.fetchone()
    if film:
        print(f"\nDétails du film:")
        print(f"ID: {film[0]}")
        print(f"Titre: {film[1]}")
        print(f"Réalisateur: {film[2]}")
        print(f"Année: {film[3]}")
    else:
        print(f"⚠ Aucun film trouvé avec l'ID {id}")

def supr_film(c, id):
    c.execute("DELETE FROM FILMOGRAPHIE WHERE idFilm=?", (id,))
    c.execute("DELETE FROM FILM WHERE idFilm=?", (id,))
    print(f"✓ Film avec ID {id} supprimé")

def modif_FILMOGRAPHIE(c, id1, id2, val):
    c.execute("UPDATE FILMOGRAPHIE SET salaire=? WHERE idActeur=? AND idFilm=?", 
              (val, id1, id2))
    print(f"✓ Salaire modifié pour l'acteur {id1} dans le film {id2}")

def Nbr_acteurs(c, nomFilm):
    c.execute("""SELECT COUNT(DISTINCT f.idActeur) 
                 FROM FILMOGRAPHIE f 
                 JOIN FILM fm ON f.idFilm = fm.idFilm 
                 WHERE fm.titre=?""", (nomFilm,))
    resultat = c.fetchone()
    return resultat[0] if resultat else 0

def ActeursSansFilms(c):
    c.execute("""SELECT nom, prenom 
                 FROM ACTEUR 
                 WHERE idActeur NOT IN (SELECT DISTINCT idActeur FROM FILMOGRAPHIE)""")
    acteurs = c.fetchall()
    print("\n=== Acteurs sans films ===")
    if acteurs:
        for acteur in acteurs:
            print(f"- {acteur[1]} {acteur[0]}")
    else:
        print("(Aucun acteur sans film)")

def ActeursDebutants(c):
    c.execute("""SELECT a.nom, a.prenom, AVG(f.salaire) as salaire_moyen
                 FROM ACTEUR a
                 JOIN FILMOGRAPHIE f ON a.idActeur = f.idActeur
                 GROUP BY a.idActeur, a.nom, a.prenom""")
    acteurs = c.fetchall()
    print("\n=== Acteurs débutants avec salaire moyen ===")
    if acteurs:
        for acteur in acteurs:
            print(f"- {acteur[1]} {acteur[0]} : Salaire moyen = {acteur[2]:,.2f}$")
    else:
        print("(Aucun acteur)")

def ActeursMemeSalaire(c):
    c.execute("""SELECT DISTINCT a1.nom, a1.prenom, a2.nom, a2.prenom, f1.salaire
                 FROM FILMOGRAPHIE f1
                 JOIN FILMOGRAPHIE f2 ON f1.salaire = f2.salaire AND f1.idActeur < f2.idActeur
                 JOIN ACTEUR a1 ON f1.idActeur = a1.idActeur
                 JOIN ACTEUR a2 ON f2.idActeur = a2.idActeur""")
    paires = c.fetchall()
    print("\n=== Paires d'acteurs avec même salaire ===")
    if paires:
        for paire in paires:
            print(f"- {paire[1]} {paire[0]} et {paire[3]} {paire[2]} : {paire[4]:,.2f}$")
    else:
        print("(Aucune paire trouvée)")

def SalaireDollarToDirham(c):
    taux_conversion = 9
    c.execute("""SELECT a.nom, a.prenom, f.salaire, fm.titre
                 FROM FILMOGRAPHIE f
                 JOIN ACTEUR a ON f.idActeur = a.idActeur
                 JOIN FILM fm ON f.idFilm = fm.idFilm""")
    salaires = c.fetchall()
    print("\n=== Salaires en Dirhams (1$ = 9 DH) ===")
    if salaires:
        for salaire in salaires:
            salaire_dirham = salaire[2] * taux_conversion
            print(f"- {salaire[1]} {salaire[0]} dans '{salaire[3]}' : {salaire_dirham:,.2f} DH")
    else:
        print("(Aucun salaire)")

def ValiderTrans(conn):
    conn.commit()
    print("✓ Transactions validées")

def TableToFile(Fich, c, nomTable):
    c.execute(f"SELECT * FROM {nomTable}")
    resultats = c.fetchall()
    with open(Fich, 'w', encoding='utf-8') as f:
        for row in resultats:
            f.write(str(row) + '\n')
    print(f"✓ Table {nomTable} exportée vers {Fich}")

def FileToTable(Fich, c, nomTable):
    try:
        with open(Fich, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    print(f"Ligne à insérer: {ligne}")
        print(f"✓ Données de {Fich} importées dans {nomTable}")
    except FileNotFoundError:
        print(f"⚠ Fichier {Fich} non trouvé")

def FermerConnex(conn):
    conn.close()
    print("✓ Connexion fermée")


if __name__ == "__main__":
    print("="*50)
    print("TEST DU MODULE cinema_db.py")
    print("="*50)
    
    conn, c = AccederBD('cinema.sqlite')
    
    CreerTable1(c)
    CreerTable2(c)
    CreerTable3(c)
    
    print("\n✓ Module cinema_db.py fonctionne correctement!")
    print("Vous pouvez maintenant l'importer dans vos autres fichiers.")
    
    FermerConnex(conn)