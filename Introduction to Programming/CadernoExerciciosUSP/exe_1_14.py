#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implemenetação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - #
def fibonacci(n):
    """
Implementa a função que computa o n-ésimo termo da sequência de Fibonacci.
    """

    if n <= 2:
        return 1

    a = 1
    b = 1
    i = 3

    while (i <= n):
        n_termo = a + b
        a = b
        b = n_termo
        i = i + 1

    return n_termo


def main(args):
    """
Computa o n-ésimo termo da sequência de Fibonacci.
    """

    print(main.__doc__)

    n = int(input())
    valor = fibonacci(n)
    print(f"O valor do {n}-ésimo termo da sequência de Fibonacci é {valor}.")

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
