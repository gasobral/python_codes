#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado n, imprimir os n primeiros inteiros positivos ímpares.
Exemplo: Para n = 4 a saída deverá ser 1, 3, 5, 7
    """

    n = int(input())
    impar = 1

    if n > 0:
        print(impar, end = '')
        i = 1

        while i < n:
            impar = impar + 2
            print(",", impar, end = '')
            i = i + 1

        print()

    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
