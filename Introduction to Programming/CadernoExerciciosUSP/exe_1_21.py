#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados n e uma sequência de n números inteiros, determinar quantos segmentos
de números iguais consecutivos compõem essa sequência.

Exemplo:
A sequência 5, 2, 2, 3, 4, 4, 4, 4, 1, 1 é formada por 5 segmentos de
números iguais.
    """

    print("Digite o valor de n: ", end = '')
    n = int(input())

    print("Digite um número: ", end = '')
    anterior = int(input())
    qtde_segmentos = 0
    
    for i in range(1, n):
        print("Digite um número: ", end = '')
        numero = int(input())

        if anterior == numero:
            qtde_segmentos = qtde_segmentos + 1

        anterior = numero

    print(f'Número de segmentos: {qtde_segmentos}')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
