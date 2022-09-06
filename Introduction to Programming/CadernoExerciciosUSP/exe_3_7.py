#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados números reais x e \epsilon, com \epsilon > 0, calcular uma
aproximação para senx através da seguinte série infinita

senx = x/1! - x^3/3! + x^5/5! - ... + (-1)^k x^{2k +1}/(2k +1) + ...

incluindo todos os termos até que |x^{2k +1}/(2k +1)| < \epsilon. Compare
com os resultados de sua calculadora.
    """

    print(main.__doc__)

    x = float(input("Digite um número real: "))
    epsilon = float(input("Digite um número real: "))

    fatorial = float(1)
    potencia_x = x
    sinal = 1
    k = 1
    termo = potencia_x / fatorial
    senx = termo

    while abs(termo) > epsilon:
        potencia_x = potencia_x * x * x;
        fatorial = fatorial * (k +1) * (k + 2)
        k = k + 2
        sinal = sinal * (-1)
        termo = sinal * (potencia_x / fatorial)
        senx = senx + termo

    print(f'sen({x}): {senx} \t sen({x}): {sin(x)}')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from math import sin
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
