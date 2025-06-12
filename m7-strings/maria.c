#include <stdio.h>

int main() {
    printf("Olá! Eu sou Maria!");

    printf("Digite um número inteiro: ");
    int numero;
    scanf("%d", &numero);

    char soma = numero + " ";

    printf("A soma de %d com espaco é %c", numero, soma);

    return 0;
}