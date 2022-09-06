#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Dados um inteiro postivo n e n inteiros positivos, determinar o máximo
divisor comum a todos eles.
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro positivo: "))
    numero = int(input("Digite um número da sequência: "))
    mdc = numero
    i = 1

    while i < n:
        numero = int(input("Digite um número da sequência: "))
        divisor = 1

        while divisor <= mdc and divisor <= numero:
            if mdc % divisor == 0 and numero % divisor == 0:
                novo_mdc = divisor

            divisor = divisor + 1

        mdc = novo_mdc
        i = i + 1

    print(f'MDC: {mdc}')
    return EX_OK


# Script Princpial - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
