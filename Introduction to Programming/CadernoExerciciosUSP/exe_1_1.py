#! /usr/bin/env pyhthon3
# -*- coding: utf-8 -*-

# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dada uma coleção de números inteiros positivos terminada por 0, imprimir seus
quadrados.
    """


    numero = int(input())

    while numero != 0:
        print(numero * numero)
        numero = int(input())

    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
