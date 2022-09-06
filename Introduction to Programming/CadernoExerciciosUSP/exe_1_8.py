#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys, os


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado um inteiro não negativo n, determina n!.
    """

    print(main.__doc__)
    n = int(input())

    if n < 0 :
        print("O valor de n deve ser não negativo!", file = sys.stderr)
        return os.EX_USAGE

    fatorial = 1

    for i in range(1, n +1, 1):
        fatorial = fatorial * i

    print(f"{n}! : {fatorial}")
    return os.EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = os.EX_OK

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
