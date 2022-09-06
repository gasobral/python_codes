#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


def conta_digitos(n):
    """
Conta a quantidade de dígitos de um inteiro n.

Parâmetros
----------
n: int
   um inteiro

Retorno
-------
int
A quantidade de dígitos de n.
    """

    qtde_digitos = 1
    quociente = n // 10

    while quociente != 0:
        qtde_digitos = qtde_digitos + 1
        quociente = quociente // 10

    return qtde_digitos


def encaixa(a, b):
    """
Escreva uma função encaixa que, recebendo dois números inteiros a e b
como parâmetros, verifica se b corresponde aos últimos dígitos de a.

Ex:
567890 890  => encaixa
1243   1243 => encaixa
2457   245  => não encaixa
457    2457 => não encaixa
    """

    if conta_digitos(b) > conta_digitos(a):
        return False

    ## obter a parte inferior
    parte_inferior = 0
    n = conta_digitos(b)
    i = 0
    pot_10 = 1
    num = a

    while i < n:
        parte_inferior = parte_inferior + (num % 10) * pot_10
        num = num // 10
        pot_10 = pot_10 * 10
        i = i +1

    if parte_inferior - b == 0:
        return True

    return False


def verifica_segmento(a, b):
    """
    """

    num_a = a
    qtde_digitos_a = conta_digitos(num_a)
    qtde_digitos_b = conta_digitos(b)
    e_segmento = encaixa(a, b)

    while qtde_digitos_b < qtde_digitos_a and e_segmento != True:
        num_a = num_a // 10
        qtde_digitos_a = conta_digitos(num_a)
        e_segmento = encaixa(num_a, b)

    return e_segmento


def main(args):
    """
    """

    numero_a = int(input("Digite um inteiro: "))
    qtde_digitos_a = conta_digitos(numero_a)

    numero_b = int(input("Digite um inteiro: "))
    qtde_digitos_b = conta_digitos(numero_b)

    if qtde_digitos_a < qtde_digitos_b:
        print(verifica_segmento(numero_b, numero_a))

    else:
        print(verifica_segmento(numero_a, numero_b))

    return EX_OK


if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
