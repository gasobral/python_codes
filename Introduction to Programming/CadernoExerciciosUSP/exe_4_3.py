#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções -------------------------------------------#
def bloco(n):
    """
(a) Escreva uma função bloco que recebe como parâmetro um inteiro n e
    lê n inteiros do teclado, devolvendo um dos seguintes valores:
    0, se os n números lidos forem pares;
    1, se os n números lidos forem ímpares;
    -1, se entre os n números lidos há números com paridades diferentes.
    """

    numero = int(input())
    paridade = numero % 2
    i = 1

    while i < n:
        numero = int(input())
        paridade_corrente = numero % 2

        if paridade != paridade_corrente:
            paridade = -1
        else:
            paridade = paridade_corrente

        i += 1

    return paridade


def verifica_seq_piramidal():
    """
(b) usando a função do item anteriro, escreva um programa que, dados um
    inteiro n (n >= 1) e uma sequência de n números inteiros, verifica
    se ela é piramidal m-alternante. O programa deve imprimir o valor
    de m ou dar a resposta não.
    """

    n = int(input("Digite um natural: "))
    paridade_anterior = bloco(1)
    i = 1
    tam_segmento = 2

    while i + tam_segmento <= n:
        paridade_corrente = bloco(tam_segmento)

        if paridade_corrente == paridade_anterior:
            return -1
        else:
            paridade_anterior = paridade_corrente

        i = i + tam_segmento
        tam_segmento += 1

    if i != n:
        return -1

    return tam_segmento -1


def main(args):
    """
Uma sequência de n números inteiros não nulos é dita piramidal
m-alternante é constituída por m segmentos: o primeiro com um elemento,
o segundo com dois elementos e assim por diante até o m-ésinmo, com m
elementos. Além disso, os elementos de um mesmo segmento devem ser
todos pares ou todos ímpares e para cada segmento, se seus elementos
forem todos pares (ímpares), os elementos do segmento seguinte devem
ser todos ímpares (pares).

(a) Escreva uma função bloco que recebe como parâmetro um inteiro n e
    lê n inteiros do teclado, devolvendo um dos seguintes valores:
    0, se os n números lidos forem pares;
    1, se os n números lidos forem ímpares;
    -1, se entre os n números lidos há números com paridades diferentes.

(b) usando a função do item anteriro, escreva um programa que, dados um
    inteiro n (n >= 1) e uma sequência de n números inteiros, verifica
    se ela é piramidal m-alternante. O programa deve imprimir o valor
    de m ou dar a resposta não.
    """

    print(main.__doc__)
    m = verifica_seq_piramidal()

    if m > 0:
        print(f'A sequência é piramidal {m}-alternante!')
    else:
        print("não!")

    return EX_OK


if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
