#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados um inteiro x e um inteiro não negativo n, calcular x^n.
    """

    x = int(input())
    n = int(input())

    if n < 0:
        return -1

    potencia = 1
    for i in range(n):
        potencia = potencia * x

    print("x^n: ", potencia)
    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
