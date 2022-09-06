#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Qualquer número natural de quatro algarismos pode ser dividido em duas
dezenas formadas pelos seus dois primeiros e dois últimos dígitos.

Exemplos:
1297: 12 e 97
5314: 53 e 14

Escreva um programa que imprime todos os milhares (4 algarismos) cuja raiz
quadrada seja a soma das dezenas formadas pela divisão acima.

Exemplo: raiz de 9801 = 99 = 98 + 01
Portanto 9801 é um dos números a ser impresso.
    """

    print(main.__doc__)

    for i in range(1000, 10000):
        dezena_1 = i % 100
        dezena_2 = i // 100

        if math.isqrt(i) == dezena_1 + dezena_2:
            print(f'numero: {i}\t dezena 1: {dezena_1}\t dezena 2: {dezena_2}')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    import math
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
