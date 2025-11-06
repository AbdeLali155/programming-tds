#include<stdio.h>

long long fact(int n){
    if(n<=1){
        return 1;
    }
    return n*fact(n-1);   
}

long long C(int n, int p){
    return fact(n)/(fact(p)*fact(n-p));
}

int main(){
    int p, n;
    
    printf("Entrez la valeur de n : ");
    scanf("%d", &n);
    
    printf("Entrez la valeur de p : ");
    scanf("%d", &p);
    
    if(p > n || p < 0 || n < 0){
        printf("Erreur : p doit etre entre 0 et n\n");
        return 1;
    }
    
    printf("C(%d,%d) = %lld\n", n, p, C(n, p));
    
    return 0;
}