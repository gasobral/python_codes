#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementações de Funções - - - - - - - - - - - - - - - - - - - - - - - - - #
def soma1():
    
    soma = float(0)
    sinal = -1

    for i in range(10000, 0, -1):
        soma = soma + float(1/i) * sinal
        sinal = sinal * (-1)

    return soma

def soma2():

    soma = 0
    sinal = 1

    for i in range(1, 10001, 1):
        soma = soma + float(1/i) * sinal
        sinal = sinal * (-1)

    return soma

def soma3():

    soma = 0

    for i in range(1, 10001, 2):
        soma = soma + float(1/i)

    for i in range(2, 10001, 2):
        soma = soma -float(1/i)

    return soma


def soma4():

    soma = 0

    for i in range(10000, 0, -2):
        soma = soma -float(1/i)

    for i in range(9999, 0, -2):
        soma = soma +float(1/i)

    return soma


def main(args):
    """
Faça um programa que calcula a soma

1 -1/2 +1/3 -1/4 + ... + 1/9999 -1/10000

pelas seguintes maneiras:

* adição dos termos da direita para a esquerda;
* adição dos termos da esquerda para a direita;
* adição separada dos termos positivos e dos termos negativos da esquerda
  para a direita;
* adição separada dos termos positivos e dos termos negativos da direita
  para a esquerda.

Compare e discuta os resultados obtidos no computador.
    """

    print(main.__doc__)

    print(soma1())
    print(soma2())
    print(soma3())
    print(soma4())

    return EX_OK


# Executa o script como sendo o módulo principal dele - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
