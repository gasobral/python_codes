#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado n, calcular a soma dos n primeiros númneros inteiros positivos.
    """

    n = int(input())
    soma = 0

    for i in range(1, n + 1):
        soma = soma + i

    print("Soma:", soma)
    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
