#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#define TAM 2095000

void combinar(int *arreglo, int n){
    #ifdef __DEBUGG__
        printf("%d\n", n);
    #endif
    int tamIzq=n/2, tamDer=n-tamIzq;
    int izq[tamIzq], der[tamDer];
    memcpy(izq, arreglo, tamIzq*sizeof(int));
    memcpy(der, arreglo+tamIzq, tamDer*sizeof(int));

    int j=0, i=0, k=0;
    for (; i<n && j<tamIzq && k<tamDer; i++){
        if(izq[j]<der[k]) arreglo[i]=izq[j++];
        else arreglo[i]=der[k++];
    }

    while(j<tamIzq) arreglo[i++]=izq[j++];
    while (k<tamDer) arreglo[i++]=der[k++];
}

void merge_sort(int *arreglo, int n){
    if(1<n){
        merge_sort(arreglo, n/2);
        merge_sort(arreglo+n/2, n-n/2);
        combinar(arreglo, n);
    }
}

int main(){

    // srand(time(NULL));

    int *arreglo = malloc(sizeof(int)*TAM);
    for(int i=0; i<TAM; i++) arreglo[i]=1;
    // int arreglo[TAM]={9,0,2,0,4};
    merge_sort(arreglo, TAM);
    // for (size_t i = 0; i < TAM; i++) printf("%d ", arreglo[i]);    
    printf("\n");
    return 0;
}