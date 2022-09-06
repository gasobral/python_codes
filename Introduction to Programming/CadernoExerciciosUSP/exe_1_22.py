#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados um inteiro positivo n e uma sequência de n números inteiros,
determinar o comprimento de um segmento crescente de comprimento máximo.
    """

    print("Digite o tamanho da sequência: ", end = '')
    n = int(input())

    if n == 0:
        return EX_OK

    print("Digite um número: ", end = '')
    numero = int(input())
    anterior = numero
    segmento_corrente = 1
    max_segmento = segmento_corrente

    for i in range(1, n):
        print("Digite um número: ", end = '')
        numero = int(input())

        if anterior < numero:
            segmento_corrente = segmento_corrente + 1

        elif segmento_corrente >  max_segmento:
            max_segmento = segmento_corrente

        anterior = numero

    print(f'Comprimento do segmento crescente máximo: {max_segmento}')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
