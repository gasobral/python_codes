#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados um inteiro positivo n e n sequências de números inteiros, cada qual
terminada por 0, calcular a soma dos números pares de cada sequência
    """

    print(main.__doc__)

    print("Digite o número de sequências: ", end = '')
    n = int(input())
    soma = 0

    for i in range(n):
        print("Digite um número inteiro: ", end = '')
        numero = int(input())

        while numero != 0:
            if numero % 2 == 0:
                soma = soma + numero

            print("Digite um número inteiro: ", end = '')
            numero = int(input())

    print(f'A soma dos numeros pares é: {soma}')

    return EX_OK


# Script Princial - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
