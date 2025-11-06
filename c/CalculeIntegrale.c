#include <stdio.h>
#include <math.h>

// Définir la fonction à intégrer f(x)
// Vous pouvez changer cette fonction selon vos besoins
double f(double x) {
    return 2*x ; // Exemple: f(x) = x²
    // Autres exemples:
    // return sin(x);
    // return exp(x);
    // return 1/x;
}

// Fonction pour calculer l'intégrale avec la méthode des trapèzes
double calculerIntegrale(double a, double b, int n) {
    double h = (b - a) / n;  // Pas h
    double somme = 0.0;
    
    // Formule des trapèzes: I = h/2 * [f(a) + 2*sum(f(xi)) + f(b)]
    somme = f(a) + f(b);
    
    for (int i = 1; i < n; i++) {
        double xi = a + i * h;
        somme += 2 * f(xi);
    }
    
    return (h / 2) * somme;
}

int main() {
    double a, b;  // Les bornes de l'intégrale
    int n;        // Nombre de subdivisions
    double resultat;
    
    printf("=== CALCUL D'INTEGRALE (Methode des Trapezes) ===\n\n");
    
    // Saisie des variables
    printf("Entrez la borne inferieure a: ");
    scanf("%lf", &a);
    
    printf("Entrez la borne superieure b: ");
    scanf("%lf", &b);
    
    printf("Entrez le nombre de subdivisions n: ");
    scanf("%d", &n);
    
    // Vérification des entrées
    if (b <= a) {
        printf("Erreur: b doit etre superieur a a!\n");
        return 1;
    }
    
    if (n <= 0) {
        printf("Erreur: n doit etre positif!\n");
        return 1;
    }
    
    // Calcul de l'intégrale
    resultat = calculerIntegrale(a, b, n);
    
    // Affichage du résultat
    printf("\n=== RESULTAT ===\n");
    printf("Integrale de f(x) de %.2f a %.2f = %.6f\n", a, b, resultat);
    printf("Nombre de subdivisions: %d\n", n);
    printf("Pas h = %.6f\n", (b - a) / n);
    
    return 0;
}