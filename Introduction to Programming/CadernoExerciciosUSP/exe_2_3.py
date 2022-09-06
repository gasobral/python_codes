#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados dois inteiros positivos m e n, determinar, entre todos os pares de
números inteiros (x, y) tais que 0 <= x <= m e 0 <= y <= n, um par para o
qual o valor da expressão xy - x^2 +y seja máximo e calcular também esse
máximo.
    """

    print(main.__doc__)

    n = int(input("Digite o valor de um inteiro positivo: "))
    m = int(input("Digite o valor de outro inteiro positivo: "))

    max_valor = 0
    max_x = 0
    max_y = 0

    for x in range(0, m+1):
        for y in range(0, n+1):
            valor = x * y - x * x + y

            if valor > max_valor:
                max_valor = valor
                max_x = x
                max_y = y

    print(f'O valor máximo da expressão xy - x^2 + xy é {max_valor}')
    print(f'Esse valor é atingido no ponto ({max_x}, {max_y})')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
