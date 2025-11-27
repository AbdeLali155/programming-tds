import sympy as sp

x,y=sp.symbols('x,y')

# # exercice 1
# # 1
f=x**3-6*x**2+5*x+12
Fprime=sp.diff(f,x)
print(Fprime)
valeurFprime=sp.solveset(Fprime,x)
print(valeurFprime)
# # 2
exp=sp.sin(x)*sp.cos(x)+sp.cos(x)*sp.sin(y)
exp_sim=sp.simplify(exp)
print(exp_sim)
exp=(2*x+3)**4
exp_dev=sp.expand(exp)
print(exp_dev)


# # 3  
intgrale_calculer=sp.integrate(sp.sin(x)*sp.cos(x),(x,0,sp.pi/2))

print(intgrale_calculer)

#4
equation=4*x+7-3*(x-1)
equation_reso=sp.solveset(equation)
print(equation_reso)

#5 
equ=(sp.exp(2*x)-1)/x
lim=sp.limit(equ,x,0)
print(lim)

# #6 
equ1=2*x-3*y-5
equ2=-x+2*y+3

resolv=sp.solve((equ1,equ2),(x,y))
print(resolv)

#7 
f=sp.Function('f')
equ=sp.Eq(sp.diff(f(x),x)-f(x),x**2)
equ_solve=sp.dsolve(equ,f(x))
print(equ_solve.lhs)

# exercie 2
# Ce code simule un seule lancer de pièce avec une probabilité de 1/3 d'obtenir PILE
import numpy as np
def simul_x():
    x=0
    for i in range(3):
        if(np.random.random()<(1/3)):
            x+=1
    return x

result=[simul_x() for i in range(1000)]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.hist(result, bins=4,
         edgecolor='black', color='blue')
plt.xlabel('Nombre de PILE (X)')
plt.ylabel('Fréquence')
plt.title('Histogramme de X sur 10000 simulations')
plt.xticks([0, 1, 2, 3])
plt.grid(axis='y', alpha=0.3)
plt.show()

# exercice 3
#Étoile
import matplotlib.pyplot as plt
import numpy as np

n = 5
angles = np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / 2
x = np.cos(angles)
y = np.sin(angles)


order = [0, 2, 4, 1, 3, 0]
x_star = x[order]
y_star = y[order]

plt.plot(x_star, y_star)
plt.title("Étoile à 5 branches")
plt.axis("equal")
plt.grid(True)
plt.show()
#
#Pentagone
n = 5
angles = np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / 2
x = np.cos(angles)
y = np.sin(angles)


x_pent = np.append(x, x[0])
y_pent = np.append(y, y[0])

plt.plot(x_pent, y_pent)
plt.title("Pentagone régulier")
plt.axis("equal")
plt.grid(True)
plt.show()

#2
import numpy as np
import matplotlib.pyplot as plt

# f1 : x → 3√(1 - x²/49)
x1a = np.linspace(3, 7, 100)
x1b = np.linspace(-7, -3, 100)
f1a = 3 * np.sqrt(1 - x1a**2 / 49)
f1b = 3 * np.sqrt(1 - x1b**2 / 49)

# f2 : x → -3√(1 - x²/49)
x2a = np.linspace(4, 7, 100)
x2b = np.linspace(-7, -4, 100)
f2a = -3 * np.sqrt(1 - x2a**2 / 49)
f2b = -3 * np.sqrt(1 - x2b**2 / 49)

# f3 : x → 9 - 8|x|
x3a = np.linspace(0.75, 1, 100)
x3b = np.linspace(-1, -0.75, 100)
f3a = 9 - 8 * np.abs(x3a)
f3b = 9 - 8 * np.abs(x3b)

# f4 : x → 0.75 + 3|x|
x4a = np.linspace(0.5, 0.75, 100)
x4b = np.linspace(-0.75, -0.5, 100)
f4a = 0.75 + 3 * np.abs(x4a)
f4b = 0.75 + 3 * np.abs(x4b)

# f5 : x → 2.25
x5 = np.linspace(-0.5, 0.5, 100)
f5 = np.full_like(x5, 2.25)

# f6 : x → |x|/2 + (3√33 - 7)/112 * x² + √(1 - (|x| - 2)²) - 3
x6 = np.linspace(-4, 4, 400)
f6 = (np.abs(x6) / 2) + ((3 * np.sqrt(33) - 7) / 112) * (x6**2) + np.sqrt(1 - (np.abs(x6) - 2)**2) - 3

# f7 : x → (6√10/7) + (1.5 - 0.5|x|)√(3 + 2|x| - x²)
x7a = np.linspace(-3, -1, 200)
x7b = np.linspace(1, 3, 200)
f7a = (6 * np.sqrt(10) / 14) * np.sqrt(3 + 2 * np.abs(x7a) - x7a**2)
f7b = (6 * np.sqrt(10) / 14) * np.sqrt(3 + 2 * np.abs(x7b) - x7b**2)

plt.figure(figsize=(8, 8))

# f1
plt.plot(x1a, f1a, 'b')
plt.plot(x1b, f1b, 'b')
# f2
plt.plot(x2a, f2a, 'b')
plt.plot(x2b, f2b, 'b')
# f3
plt.plot(x3a, f3a, 'b')
plt.plot(x3b, f3b, 'b')
# f4
plt.plot(x4a, f4a, 'b')
plt.plot(x4b, f4b, 'b')
# f5
plt.plot(x5, f5, 'b')
# f6
plt.plot(x6, f6, 'b')
# f7
plt.plot(x7a, f7a, 'b')
plt.plot(x7b, f7b, 'b')


plt.axis('equal')
plt.title("Courbes des fonctions f₁ à f₇ sur un même graphique")
plt.grid(True)
plt.show()



