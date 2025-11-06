#parite1
def occurences(lettre,mot):
    return mot.count(lettre)

print(occurences("a","aaaa"))
from collections import Counter

def occurences(lettre,mot):
    return Counter(mot)[lettre]

print(occurences("a","aaaa"))

#partie 2
from collections import Counter

scrabble = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 10, "l": 1, "m": 2, "n": 1, "o": 1, "p": 3, "q": 8, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 10, "x": 10, "y": 10, "z": 10}

def score_mot(mot):
    
    x = 0
    for key, value in Counter(mot.lower()).items():
        x += value * scrabble.get(key,0)  
    return x

print(score_mot("Bonjour"))  
#partie 3
from collections import Counter
jetons = {"a": 9, "b": 2, "c": 2, "d": 3, "e": 15, "f": 2, "g": 2, "h": 2, "i": 8, "j": 1, "k": 1, "l": 5, "m": 3, "n": 6, "o": 6, "p": 2, "q": 1, "r": 6, "s": 6, "t": 6, "u": 6, "v": 2, "w": 1, "x": 1, "y": 1, "z": 1}
L_jetons = []
for lettre in jetons:
    L_jetons = L_jetons + [lettre] * jetons[lettre]

from random import randint
print(L_jetons)
def poiche():
    
    mot=""
    for i in range(7):
        x=randint(0,99) 
        mot+=L_jetons[x]
    print(mot)

    return Counter(mot)

print(poiche())

        

        
    
    