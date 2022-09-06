#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys
from os import EX_OK


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def binario_para_decimal(n):
    """
Converte um número binário para decimal.
    """

    valor = 0
    i = len(n) -1
    potencia_2 = 1

    while (i >= 0):
        valor = valor + int(n[i]) * potencia_2
        potencia_2 = potencia_2 * 2
        i = i -1

    return valor


def main(args):
    """
Dado um número natural na base binária, transformá-lo para a base decimal.
    """

    print(main.__doc__)

    numero_binario = input()
    numero_decimal = binario_para_decimal(list(numero_binario))

    print(f"binário {numero_binario} \t decimal {numero_decimal}")

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
codigo_retorno = EX_OK

if __name__ == "__main__":
    codigo_retorno = main(sys.argv)

sys.exit(codigo_retorno)
