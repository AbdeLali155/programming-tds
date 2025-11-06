#Exercice 1
#1
def EMpiler_fat(n,P1):
    fac=1
    P1.append(fac)
    for i in range(1,n+1):
        fac*=i
        P1.append(fac)
    
    return P1
#2
def Empiler_Puiss(n,x,P2):
    for i in range(0,n+1):
        P2.append(x**i)
    return P2
#3
def Empiler_Frac(P1 , P2):
    P3=[]
    for i,j in P1 and zip(P1,P2):
        P3.append(j/i)
    return P3
#4
def Somme(n ,x):
    P1=[]
    P2=[]
    P3= Empiler_Frac(EMpiler_fat(n,P1),Empiler_Puiss(n,x,P2))
    return sum(P3)
#exercice2
#question 1

# ona 17 10 - expressions en notation classique ->17-10
#lire 17 empiler la pile =pile[17]
#lire 10 empiler la pile=pile[17,10]
#lire - depiler 10 et 17 -> 17-10=7
#empiler la pile =pile[7]

# ona 3 28 7 / + expressions en notation classique (28/7)+4
#lire 3 empiler la pile 
#lire 28 empiler la pile 
#lire 7 empiler la pile =pile[3,28,7]
#lire / depiler 7 et 28 -> 28/7=4
#empiler la pile par 3=pile[3,4]
#lire + depiler la pile -> 3+4=7
#empiler la pile par 7 ->pile[7]

#question 2
#(19 * 6) – 7  polonaise inversée est 19 6 * 7 -

#question 3
def PileVide():
    return []
def PileVide(pile):
    return len(pile)==0
def Empiler(pile,n):
    pile.append(n)
def Depiler(pile):
    return pile.pop()
def SommetPile(pile):
    return pile[-1]
#question 4
def EstChiffre(c):
    return 1 if c in '0123456789' else 0
#question 5
def  Convertir(c):
    return int(c)
#question 6
def Evaluer(expression):
    pile = PileVide()  
    for i in expression.split():
        if EstChiffre(i):
            Empiler(pile, Convertir(i))  
        else:
            a = Depiler(pile)
            b = Depiler(pile)
            if i =='+':
                Empiler(pile,b+a)  
            elif i =='-':
                Empiler(pile,b-a)  
            elif i =='*':
                Empiler(pile,b*a)  
            elif i =='/':
                Empiler(pile,b/a)  
    return pile[-1]
#question 6

def EvaluerTexte(Fsrc, Fdest):
    with open(Fsrc, 'r') as fsrc:
        with open(Fdest, 'w') as fdest:
            for ligne in fsrc:
                ligne = ligne.strip() 
                if ligne !="":  
                    resultat = Evaluer(ligne)  
                    fdest.write(f"{ligne} = {resultat}\n")  
#exercice 3

def creer_file_priorite():
    return []

def deposer_dans_queue(file, element, priorite):
    ordre_arrivee = len(file)
    file.append((element, priorite, ordre_arrivee))

def retirer_de_queue(file):
    max_priorite = 0
    for element, priorite, ordre in file:
        if priorite > max_priorite:
            max_priorite = priorite
    element_a_retirer = None
    min_ordre = 1000
    
    for item in file:
        element, priorite, ordre = item
        if priorite == max_priorite:  
            if ordre < min_ordre:      
                element_a_retirer = item
                min_ordre = ordre
    
    file.remove(element_a_retirer)

    return element_a_retirer[0]
#exercice 4
import random
INTERVALLE_MAX=60
DUREE_TRAITEMENT_MAX = 360
def CreerListeClients():
    client=[]
    datedarive=8*3600
    duréeDattente=0
    nombreClient=int(input("entrer le nombre de clients"))
    for i in range(1,nombreClient+1):
        client[i]=[i,datedarive,duréeDattente]
        duréeDattente=(datedarive+INTERVALLE_MAX+DUREE_TRAITEMENT_MAX)-datedarive
    
    return client

def afficheClient(client):
    for num,datearive,duréeDattente in client:
        print(num,datearive/3600,(datearive+duréeDattente)/3600)
#exercice5 
#1. Importer
contenu = """nom genre score_1 score_2 email
Morgan M 199 352 momo@example.com
Celia F 993 239 celiadupont@example.com
Mehdi M 234 876 bossDeLoctogone@rapgame.fr
John M 1452 86 jonny@example.com
Axelle F 290 222 ax59@ici.com
Sonia F 1987 965 soso@example.com
Sabina F 197 25 booba@example.com
Thibault F 1987 765 thiball@goog.com
Louis M 223 65 lmax@example.com
Lena F 1987 765 leterminator@caramail.com
Luka M 977 535 lulu@example.com
Sandra F 197 259 temointemoin@example.com
Irena F 17 893 nena@example.com"""

with open("utilisateurs.csv", "w") as f:
    f.write(contenu)

import csv
def importer_csv(fichier):
    table=[]
    with open(fichier,"r") as fichier:
        lecteur=csv.DictReader(fichier,delimiter=" ")

        for ligne in lecteur:
            ligne['score_1'] = int(ligne['score_1'])
            ligne['score_2'] = int(ligne['score_2'])
            table.append(ligne)
        
    return table   


#2. Sélectionner
def enregistrementsjoueursmoins300(table):
        table2=[]
        for jou in table:
            if jou['score_1']<300:
                table2.append(jou)
        
        return table2

def enregistrementsjoueursFilles(table):
        table2=[]
        for jou in table:
            if jou['genre']=="F":
                table2.append(jou)
        
        return table2
def nregistrementsexamplefr(table):
        table2=[]
        for jou in table:
            if jou['email'].endswith('@example.fr'):
                table2.append(jou)
        
        return table2
#3. Projecter
#1
def meilleursscorespourchaquejeu(table):
    tablejeu1=[]
    tablejeu2=[]
    for jeu in table:
        tablejeu1.append(jeu["score_1"])
        tablejeu2.append(jeu["score_2"])
    return  tablejeu1,tablejeu2

def meilleursscorespourchaquejeutrie(table):
     tablejeu1trier,tablejeu2trier=meilleursscorespourchaquejeu(table)

     tablejeu1trier=sorted(tablejeu2trier,key=lambda x: x['score'])
     tablejeu2trier=sorted(tablejeu2trier,key=lambda x: x['score'])
     return tablejeu1trier,tablejeu2trier

def scoremoyen(table):
    
    jeu1=0
    jeu2=0
    for jeu in table:
        jeu1+=table["score_1"]
        jeu2+=table["score_2"]

    return jeu1/len(table),jeu2/len(table)


#2. Adresses mail.

def email(table):
    tableemail=[]
    for jeu in table:
        tableemail.append(jeu["email"])
        
    return  tableemail
def movies10scoreemail(table):
    movies10score1,movies10score2=meilleursscorespourchaquejeutrie(table)
    movies10score1email=[]
    movies10score2email=[]
    for i in movies10score1[:10]:
        movies10score1email.append(i["email"])
    for i in movies10score2[:10]:
        movies10score2email.append(i["email"])

    return movies10score1email,movies10score2email

   
def emails_sans_doublons(emails):
   
    return list(set(emails))

