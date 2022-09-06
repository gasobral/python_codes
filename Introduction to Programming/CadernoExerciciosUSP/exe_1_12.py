#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def mdc(a, b):
    """
Recebe dois naturais a, b e computa o MDC(a, b) iterativamente pelo algoritmo
de Euclides
    """

    while(b != 0):
        resto = a % b
        a = b
        b = resto

    return a


def main(args):
    """
Recebe dois naturais a, b e determina o MDC(a, b) pelo algoritmo de Euclides.
    """

    print(main.__doc__)

    a = int(input())
    b = int(input())

    valor_mdc = mdc(a, b)
    print(f"mdc({a}, {b}): {valor_mdc}")

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
