#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados um número real x e um inteiro não negativo n, calcular uma aproximação
para cos x através dos n primeiros termos da seguinte série:

cos x = 1 - x^2/2! + x^4/4! - x^6/6! + ... + (-1)^k x^{2k}/(2k)! + ...

Compare com os resultados de sua calculadora!
    """

    print(main.__doc__)

    x = float(input("Digite um número real: "))
    n = int(input("Digite um inteiro não negativo: "))

    potencia = float(1)
    fatorial = float(1)
    cosx = float(1)
    sinal = 1
    i = 2
    k = 0

    while i <= n:
        potencia = potencia * x * x
        fatorial = fatorial * (k +1) * (k +2)
        sinal = sinal * (-1)
        cosx = cosx + sinal * (potencia / fatorial)
        k = k + 2
        i = i + 1

    print(f'cos{x}: {cosx}')
    return EX_OK


# Parte Principal do Script - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
