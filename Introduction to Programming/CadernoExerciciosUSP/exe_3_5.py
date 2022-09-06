#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados números reais a, b e c calcular as raízes de uma equação do segundo
grau da forma ax^2 + bx + c = 0. Imprimir a solução em uma das seguintes
formas:

a. Dupla    b. Reais distintas    c. Complexas
raiz        raiz1                 parte real
raiz2                 parte imaginária
    """

    print(main.__doc__)

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b ** 2 -4 * a * c

    if delta == 0:
        x = -b / (2*a)
        print(f'Dupla\n{x}')

    elif delta > 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz)/(2*a)
        print(f'Reais distintas\n{x1}\n{x2}')

    else:
        delta = -delta
        raiz = math.sqrt(delta)
        x_real = -b/(2*a)
        x_img = raiz/(2*a)
        print(f'Complexas\n{x_real}\n{x_img}i')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    import math

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
