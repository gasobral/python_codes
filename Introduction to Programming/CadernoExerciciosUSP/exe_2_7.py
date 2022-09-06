#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Dado um número inteiro positivo, determine a sua decomposição em fatores
primos calculando também a multiplicidade de cada fator.
    """

    print(main.__doc__)

    numero = int(input("Digite um número inteiro: "))
    fator = 2

    while numero > 1:
        multiplicidade = 0

        while numero % fator == 0:
            multiplicidade = multiplicidade + 1
            numero = numero / fator

        if multiplicidade != 0 :
            print(f'primo: {fator}\t multiplicidade: {multiplicidade}')

        fator = fator + 1

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
