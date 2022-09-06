#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def contadigitos(n, d):
    """
n: um inteiro
d: um dígito entre 0 e 9
return: a quantidade de vezes que o dígito d aparece no número n
    """

    qtde_ocorrencias = 0
    numero = n

    while numero != 0:
        resto =  numero % 10

        if resto == d:
            qtde_ocorrencias = qtde_ocorrencias + 1

        numero = numero // 10

    return qtde_ocorrencias


def main(args):
    """
Um número a é dito permutação de um número b se o dígitos de a formam
uma permutação dos dígitos de b.

Exemplo:
5412434 é uma permutação de 4321445, mas não é uma permutação de
4312455.

Obs: Considere que o dígito 0 (zero) não aparece nos números.

(a) Faça uma função contadigitos que, recebendo um inteiro n e um
    inteiro d, 0 < d <=9, devolve quantas vezes o dígito d aparece em n.

(b) Usando a função od item anterior, faça um programa que lê dois
    números a e b e responda se a é permutação de b.
    """

    print(main.__doc__)

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    e_permutacao = True
    i = 0

    while i < 10 and e_permutacao == True:
        if contadigitos(numero1, i) != contadigitos(numero2, i):
            e_permutacao = False
        
        i = i +1


    if e_permutacao == True:
        print(f'O número {numero2} é permutação do número {numero1}.')

    else:
        print(f'O número {numero2} é NÃO permutação do número {numero1}.')

    return EX_OK


# Executa o script como módulo principal - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
