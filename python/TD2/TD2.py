#exercice3
n=int(input("enter un entier :"))
x=int(input("enter un reel :"))
s=0
for k in range(0,n+1):
    s+=k*(x**k)
print("la somme est=",s)

# exercice4
n = int(input("Entrer le nombre de notes : "))
s = 0
for k in range(n):
    note = float(input(f"Entrer la note {k+1} : "))
    while(note<0 or note>20):
        note = float(input(f"Entrer la note {k+1} : "))
    s += note
print("La moyenne des notes est :", s / n)

#exercie5
# method1
def factorielle(n):
    s=1
    for i in range(1,n+1):
        s=s*i

    print(f"{n}!={s}")

factorielle(4)
# method2
def factorielle2(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorielle2(n-1)
    
n=factorielle2(4)
print(n)

# exercice 8
# 1
n=int(input(f"entrer un entrier naturel non nul: "))
while  n<0:
    n=int(input(f"entrer un entrier naturel non nul: "))
s=1
while(n>1):
    s=s+(1/n)
    n-=1
print(s)
#  2
n=2
s=1
while(s<=8):
    s=s+(1/n)
    n+=1
print(s)
print(n-1)
# Exercice 9
import random
nombre = random.randint(1, 1000)
print(nombre)
n=int(input("entrer un nombre entre 1 et 1000 : "))
while n!=nombre:
    if n>nombre:
        print("le nnoombre est plus grand")
    else:
        print("le nnoombre est plus petit")
    n=int(input("Novel essai : "))
print("Bravo")







    
    


