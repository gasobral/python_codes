#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def converte(n):
    """
Recebe um número n na base decimal e o converte para base binária.
    """

    binario = list()
    quociente = n

    while quociente >= 2:
        resto = quociente % 2
        quociente = int(quociente/2)
        binario.append(resto)

    resto = quociente % 2
    binario.append(resto)
    binario.reverse()

    return binario


def lista_para_string(L):
    """
Recebe uma lista L e retorna uma string com os elementos de L.
    """

    Lstr = ""

    for l in L:
        Lstr += str(l)

    return Lstr


def main(args):
    """
Dado um número natural na base decimal, transformá-lo para a base binária.
    """

    print(main.__doc__)
    numero_decimal = int(input())

    numero_binario = converte(numero_decimal)
    print(lista_para_string(numero_binario))
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
