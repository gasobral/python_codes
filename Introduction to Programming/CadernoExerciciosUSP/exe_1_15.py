#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def imprime_congruentes(n, j, m):
    """
Imprime os n primeiros naturais que são congruentes a j módulo m.
    """

    for i in range(1, n +1):
        if (i % m) == (j % m):
            print(i, end = ' ')
    
    return


def main(args):
    """
Dados inteiros positivos n, j e m, imprimir os n primeiros naturais congruentes\
\n a j módulo m.
    """

    print(main.__doc__)

    n = int(input())
    j = int(input())
    m = int(input())

    imprime_congruentes(n, j, m)

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
