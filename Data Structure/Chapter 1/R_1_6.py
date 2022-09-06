#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def soma_quadrado_impares(n):
    """
Função que retorna o valor da soma dos quadrados dos inteiros ímpares
menores do que n.

Parâmetros
----------
    n (int): um inteiro positivo.

Retorno
-------
    int: o valor da soma dos quadrados dos inteiros ímpares menores do
         que n.
    """

    soma = 0
    i = 1

    while i < n:
        soma = soma + i ** 2
        i = i +2

    return soma


def main(args):
    """
Write a short Python function that takes a postive integer n and returns
the sum of all the odd positive integers smaller than n.
    """

    print(main.__doc__)
    n = int(input("Digite um inteiro: "))
    soma = soma_quadrado_impares(n)
    print(f'Soma: {soma}')
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
