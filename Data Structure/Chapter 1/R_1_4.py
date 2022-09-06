#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def soma_quadrado(n):
    """
Função que retona a soma de 1^2 + 2^2 + ... (n-1)^2.

Parâmetro
---------
    n (int): um inteiro positivo.

Retorno
-------
    int: o valor da soma de 1^2 + 2^2 + ... (n-1)^2.
    """

    soma = 0

    for i in range(n):
        soma = soma + i * i

    return soma


def main(args):
    """
Write a short Python function that takes a postive integer n and returns
the sum of the squares of all postiive integers smaller than n.
    """

    print(main.__doc__)
    n = int(input("Digite um inteiro: "))
    soma = soma_quadrado(n)
    print(f'Soma: {soma}')
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
