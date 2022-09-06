#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def testa_numero_perfeito(n):
    """
Recebe um inteiro n e retorna True se n for um número perfeito e False caso
contrário
    """

    soma_divisores = 1
    i = 2

    while (i < n):
        if (n % i) == 0:
            soma_divisores = soma_divisores + i

        i = i + 1

    if (n == soma_divisores):
        return True

    return False


def main(args):
    """
Dado um número natural n, verifica se n é um número perfeito, isto é, se n é\
\nigual a soma dos seus divisores diferentes de n.
    """

    print(main.__doc__)

    n = int(input())
    flag_numero_perfeito = testa_numero_perfeito(n)

    print(f"{n} é um número perfeito? {flag_numero_perfeito}")

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
