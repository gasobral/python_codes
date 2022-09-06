#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys, os


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def e_par(numero):
    """
Dado um numero verificar se ele é par ou não.
    """

    if (numero % 2) == 0:
        return True

    return False


def main(args):
    """
Dados n e uma sequência de n números inteiros, determinar a soma dos números\
pares.
    """

    print("Digite um valor de n: ", end = '')
    n = int(input())
    soma = 0

    for i in range(n):
        numero = int(input())

        if e_par(numero) == True:
            soma = soma + numero

    print("Soma dos números pares: ", soma)
    return os.EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = os.EX_OK

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
