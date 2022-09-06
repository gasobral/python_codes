#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def verifica_primo(m):
    """
(a) Escreva uma função que recebe um inteiro positivo m e devolve 1 se
    m é primo, 0 em caso contrário.
    """

    if m == 2:
        return 1

    if m % 2 == 0:
        return 0

    i = 3

    while i <= m/2:
        if m % i == 0:
            return 0

        i = i +1

    return 1


def soma_primos(n):
    """
(b) Escreva um programa que leia um inteiro não-negativo n e imprima a
    soma dos n primeiros números primos.
    """

    soma = 0
    i = 0
    numero = 1

    while i < n:
        if verifica_primo(numero) == 1:
            soma = soma + numero
            i = i +1

        numero = numero +1

    return soma


def main(args):
    """
(a) Escreva uma função que recebe um inteiro positivo m e devolve 1 se
    m é primo, 0 em caso contrário.

(b) Escreva um programa que leia um inteiro não-negativo n e imprima a
    soma dos n primeiros números primos.
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro não-negativo: "))
    print(f'Soma dos {n} primeiros primos: {soma_primos(n)}')

    return EX_OK


# Teste o Script - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
