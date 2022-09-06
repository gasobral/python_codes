#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Importção de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Uma loja de discos anota diariamente durante o mês de Março a quantidade de
discos vendidos. Determinar em que dia desse mês ocorreu a maior venda e qual
foi a quantidade de discos vendida nesse dia.
    """

    max_dias_marco = 5
    max_quantidade = 0

    for dia in range(1, max_dias_marco +1):
        quantidade = int(input())

        if quantidade > max_quantidade:
            max_quantidade = quantidade
            max_dia = dia

    print("dia: ", max_dia, "\t quantidade: ", max_quantidade)

    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
