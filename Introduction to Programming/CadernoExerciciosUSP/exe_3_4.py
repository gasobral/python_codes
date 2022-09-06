#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Estrutura de Dados - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
class coordenada_real:
    """
Uma classe que implementa uma coordenada real no espaço
    """

    def __init__(self, x = 0, y = 0):

        self.x = float(x)
        self.y = float(y)


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Considere o conjunto H = H_1 cup H_2 de pontos reais, onde

H_1 = {(x, y) | x <=0, y <=0, y + x^2 + 2x -3 <= 0} e
H_2 = {(x, y) | x >=0, y + x^2 -2x -3 <= 0}

Faça um programa que lê um inteiro positivo n e uma sequência de n pontos
reais (x, y) e verifica se cada ponto pertence ou não ao conjunto H. O
programa deve também contar o número de pontos da sequência que pertencem
a H.
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro positivo: "))
    qtde_pontos_H = 0
    ponto =  coordenada_real()

    for i in range(n):
        ponto.x = float(input("Digite a componente x: "))
        ponto.y = float(input("Digite a componente y: "))

        if ponto.x <= 0 and ponto.y < 0:
            if ponto.y + ponto.x * ponto.x + 2*ponto.x -3 <= 0:
                qtde_pontos_H = qtde_pontos_H + 1

        if ponto.x >= 0:
            if ponto.y + ponto.x * ponto.x -2 * ponto.x -3 <= 0:
                qtde_pontos_H = qtde_pontos_H + 1

    print(f'Quantidade de pontos em H: {qtde_pontos_H}')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
