#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys, os


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dizemos que um número natural é triangular se ele é produto de três números\
naturais consecutivos.

Exemplo: 120 é triangular, pois 4.5.6 = 120

Dado um inteiro não negativo n, verificar se n é triangular.
    """

    print(main.__doc__)
    print("Digite o valor de n: ", end = '')
    n = int(input())
    i = 1

    while (i * (i+1) * (i+2) ) < n:
        i = i + 1

    if (i * (i+1) * (i+2) ) == n:
        print(f"{n} é triangular, pois {i}.{i+1}.{i+2} = {n}")

    else:
        print(f"{n} não é triangular")

    return os.EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = os.EX_OK

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
