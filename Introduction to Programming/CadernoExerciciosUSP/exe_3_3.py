#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Estruturas de Dados - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class ponto:
    def __init__(self, x = 0, y = 0):
        self.x = float(x);
        self.i = float(y);


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Os pontos (x, y) que pertecem à figura H (abaixo) são tais que x >=0, y >= 0
e x^2 + y^2 <= 1. Dados um inteiro positivo n e n pontos reais (x, y),
verifique se cada ponto pertence ou não a H.
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro positivo: "))
    p = ponto()

    for i in range(n):
        p.x = float(input("Digite a componente x: "))
        p.y = float(input("Digite a componente y: "))

        if p.x ** 2 + p.y ** 2 <= 1:
            print(f'O ponto ({p.x}, {p.y}) pertence a H')
        else:
            print(f'O ponto ({p.x}, {p.y}) NÃO pertence a H')

    del p
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
