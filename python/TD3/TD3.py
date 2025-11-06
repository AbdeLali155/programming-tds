# #exercice 1
def function(n):
    return [i + 3 for i in range(n + 1)]

print(function(5))
# #exercice 2
chaine1="abc"
chaine2="de"

resultat = [c1 + c2 for c1 in chaine1 for c2 in chaine2]

 #exercie3
#1

def grands(L,x):
    L.sort()
    j=L.index(x)
    return len(L) - j - 1
 #2
 #la complexite est O(nlogn) car sort() est O(nlogn)est index(n)

def petits(L,x):
    L.sort()
    j=L.index(x)
    return j

def median(L):
    n=len(L)
    p=int(n/2)
    L.sort() 
    for i in range(n):
        x=petits(L,L[i])
        y=grands(L,L[i])
        if x <= p and y <= p:
            return i 
#exercice4
#a
def Occur(Text,lettre):
    s=0
    for i in Text:
        if(i==lettre):
            s+=1
    return s

#method 2
    return Text.count(lettre)
#method 3
    return sum(1 for i in Text if i == lettre)\
#exercice5

mot=input("entrer un mot: ")
mot = mot.lower()  
if mot == mot[::-1]:
    print(f"le mot {mot} est palindrome")
else:
    print(f"le mot {mot} n est pas  palindrome")
#exercice6


        


    

        
        
    








