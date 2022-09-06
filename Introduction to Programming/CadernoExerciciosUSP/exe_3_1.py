#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Função - - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Uma pessoa aplicou um capital de x reais a juros mensais de z durante 1 ano.
Determinar o montante de cada mês durante este período.
    """

    print(main.__doc__)
    capital_inicial = float(input("Digite o capital inicial: "))
    juros_mensal = float(input("Digite o juros (0-100): "))
    montante_mensal = capital_inicial

    for i in range(12):
        montante_mensal = montante_mensal + (montante_mensal * juros_mensal)/100
        print(f'Mês {i+1}\t Montante Mensal: {montante_mensal:.2f}')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
