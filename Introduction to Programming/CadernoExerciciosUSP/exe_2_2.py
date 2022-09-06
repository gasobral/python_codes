#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado um inteiro positivo n, determinar todos os inteiros entre 1 e n que
são comprimento de hipotenusa de um triângulo retângulo com catetos inteiros
    """

    print(main.__doc__)
    print("Digite um inteiro positivo: ", end = '')
    n = int(input())

    for i in range(1, n+1):
        j = 1
        while j <= i:
            h = 1

            while h <= i:
                if i * i == j * j + h * h:
                    print(f'{i} {j} {h} formam um triânulo retângulo.')

                h = h + 1

            j = j + 1

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
