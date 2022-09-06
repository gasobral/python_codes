#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Importação de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys, os


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def testa_multiplo(x, y):
    """
Dados dois números inteiros verifica se x é multiplo de y. Se for retorna\
verdadeiro, caso contrário retorna falso.
    """

    if (x % y) == 0:
        return True

    return False


def main(args):
    """
Dado n e dois números inteiros positivos i e j, imprimir em ordem crescente os\
n primeiros naturais que são múltiplos de i ou de j e ou ambos.

Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
    """

    print(main.__doc__)
    print("Digite o valor de n: ", end = '')
    n = int(input())
    print("Digite o valor de i: ", end = '')
    i = int(input())
    print("Digite o valor de j: ", end = '')
    j = int(input())

    qtd_multiplo = 0
    numero = 0

    while qtd_multiplo < n:
        if testa_multiplo(numero, i)  or testa_multiplo(numero, j):
            qtd_multiplo = qtd_multiplo + 1

            if qtd_multiplo < n:
                print(f"{numero}, ", end = '')

            else:
                print(f"{numero}.")

        numero = numero + 1

    return os.EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = os.EX_OK

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
