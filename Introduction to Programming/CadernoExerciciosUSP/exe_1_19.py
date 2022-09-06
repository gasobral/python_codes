#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def imprimir_ordem_crescente(L):
    """
Recebe três número a, b, c e os imprime em ordem crescente.
    """

    l = len(L)

    for i in range(0, l):
        min = i

        for j in range(i, l):
            if L[j] < L[min]:
                min = j

        troca = L[i]
        L[i] = L[min]
        L[min] = troca

    print(L)


def main(args):
    """
Dados três números, imprimi-los em ordem crescente.
    """

    lista = list()

    lista.append(int(input()))
    lista.append(int(input()))
    lista.append(int(input()))

    imprimir_ordem_crescente(lista)
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
