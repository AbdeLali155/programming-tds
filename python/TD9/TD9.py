import numpy as np
import matplotlib.pyplot as plt
from random import randrange

#partie 1
#q 1
def image_noire(h, l):
    return np.zeros((h, l), dtype=int)
#q 2
def image_blanche(h, l):
    return np.ones((h, l), dtype=int)
#q 3
def creerImgBlancNoir(h, l):
    img = np.zeros((h, l), dtype=int)
    for i in range(h):
        for j in range(l):
            img[i][j] = (i + j) % 2
    return img
#q 4
def negatif(img):
    h, l = img.shape
    neg = np.zeros((h, l), dtype=int)
    for i in range(h):
        for j in range(l):
            neg[i][j] = 1 - img[i][j]
    return neg
#partie 2
#q 5
def luminance(img):
  
    return np.mean(img)
#q 6
def contraste(img):
    return np.var(img)
#q 7
def profondeur(img):
    return np.max(img)

#q8
def Ouvrir(chemin):
    img = plt.imread(chemin)
    return img
#partie 3
#q9
def inverser(img):
    p = profondeur(img)
    return p - img
#q10
def flipH(img):
    return np.fliplr(img)
#q11
def poserV(img1, img2):
    return np.vstack((img1, img2))
#q12
def poserH(img1, img2):
    return np.hstack((img1, img2))
#partie 4
#q13
def transferer(img, q, t):
    h, l = img.shape
    nouvelle_img = np.zeros((h, l), dtype=int)
    for i in range(h):
        for j in range(l):
            nouvelle_img[i][j] = t[int(img[i][j])]
    return nouvelle_img
#q14
def inverser_transfert(img):
    p = profondeur(img)
    t = [p - i for i in range(int(p) + 1)]
    return transferer(img, p, t)
#q15
def histogramme(img):
    p = int(profondeur(img))
    hi = [0] * (p + 1)
    h, l = img.shape
    for i in range(h):
        for j in range(l):
            hi[int(img[i][j])] += 1
    return hi
#q16
def egaliser(img):
    h, l = img.shape
    p = int(profondeur(img))
    hi = histogramme(img)
    
    vmin = 0
    for v in range(p + 1):
        if hi[v] > 0:
            vmin = v
            break
    
    somme_cumul = 0
    t = [0] * (p + 1)
    
    for v in range(vmin, p + 1):
        somme_cumul += hi[v]
        if v > vmin:
            v_prime = ((somme_cumul - hi[vmin]) * p) / (h * l - hi[vmin])
            t[v] = int(round(v_prime, 0))
        else:
            t[v] = 0
    
    return transferer(img, p, t)
#q18
def reduire(img, q):
    p = profondeur(img)
    t = [0] * (int(p) + 1)
    for v in range(int(p) + 1):
        t[v] = int(round((v * q) / p, 0))
    return transferer(img, q, t)
#partie 5
#q 21
def initImageRGB(n, m, p=255):
    imageRGB = np.zeros((n, m, 3), dtype=int)
    for i in range(n):
        for j in range(m):
            for k in range(3):
                imageRGB[i][j][k] = randrange(p + 1)
    return imageRGB
#q 22
def symetrie_horizontale(img):
    return np.flipud(img)

def symetrie_verticale(img):
    return np.fliplr(img)
#q 23
def grayscale(imageRGB):
    n, m = imageRGB.shape[0], imageRGB.shape[1]
    gray_img = np.zeros((n, m), dtype=int)
    
    for i in range(n):
        for j in range(m):
            r, g, b = imageRGB[i][j][0], imageRGB[i][j][1], imageRGB[i][j][2]
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            gray_img[i][j] = int((max_val + min_val) / 2)
    
    return gray_img
#partie 6
# q 24: BONJOUR en binaire
# B=00001, O=01110, N=01101, J=01001, O=01110, U=10100, R=10001
# Résultat: 0000101110011010100101110101001000

# q 25:01010011110110001001
# 01010=R,01111=P,01100=M,01001=J -> RPMJ
#q 15
def disposer(L, A):
    h, l = A.shape
    C = np.zeros((h, l), dtype=int)
    idx = 0
    for i in range(h):
        for j in range(l):
            if idx < len(L):
                C[i][j] = L[idx]
                idx += 1
            else:
                C[i][j] = 0
    return C
#q 17
def dissimuler(A, C):
    h, l = A.shape
    B = np.zeros((h, l), dtype=int)
    for i in range(h):
        for j in range(l):
            if A[i][j] % 2 == 0:
                B[i][j] = A[i][j] + C[i][j]
            else:
                B[i][j] = A[i][j] - 1 + C[i][j]
    return B
#q 18
def retrouver(B):
    h, l = B.shape
    L = []
    for i in range(h):
        for j in range(l):
            L.append(B[i][j] % 2)
    return L
