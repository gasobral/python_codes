#! /usr/bin/env/python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado um inteiro positivo n, calcular e imprimir o valor da seguinte soma:

1/n + 2/(n -1) + 3/(n -2) + ... + n/1
    """

    print(main.__doc__)
    n = int(input("Digite um inteiro postivo: "))
    soma = float(0)

    for i in range(1, n +1):
        soma = soma + float(i / (n -i +1))

    print(f'Soma: {soma}')


# Parte Principal do Script - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
