#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dado um inteiro positivo n, determine o número harmônico H_n definido por:

H_n = \sum_{k = 1}^n \frac{1}{k}
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro positivo: "))
    numero_harmonico = float(0)

    for k in range(1, n +1):
        numero_harmonico = numero_harmonico + float(1/k)

    print(f'Número Harmônico: {numero_harmonico:.2f}')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
