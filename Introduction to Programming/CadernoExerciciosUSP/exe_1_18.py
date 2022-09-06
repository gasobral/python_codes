#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def verifica_triangulo_retangulo(a, b, c):
    """
Dados a, b e c retorna True se for um triangulo retângulo, caso contrário\n\
retorna false.
    """

    if a ** 2 == b ** 2 + c ** 2:
        return True

    return False


def main(args):
    """
Dados três inteiros positivos, verificar se eles formam os lados de um\n\
triângulo retângulo.
    """

    print(main.__doc__)

    a = int(input())
    b = int(input())
    c = int(input())

    print(verifica_triangulo_retangulo(a, b, c))
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
