#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys, os


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def verifica_primo(n):
    """
Recebe um natural n e retorna True se n for primo e False caso contrário.
    """

    if (n % 2) == 0:
        return False

    primo = True
    i = 3

    while i < n:
        if (n % i) == 0:
            primo = False

        i = i + 1

    return primo


def main(args):
    """
Dado inteiro positivo p, verificar se p é primo.
    """

    print(main.__doc__)
    n = int(input())

    if verifica_primo(n) == True:
        print("O número ", n , " é primo.")

    else:
        print("O número ", n, " não é primo.")

    return os.EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = os.EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
