#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados um inteiro positivo n e n triplas compostas por um símbolo de operação
(+, -, * ou /) e dois números reais, calcule o resultados ao efetuar a
operação indicada para os dois números (Sugestão: use switch).
    """

    print(main.__doc__)
    n = int(input("Digite um inteiro positivo: "))

    for i in range(n):
        tripla = input("Digite uma tripla: ")
        operador = tripla[0]
        operando1 = float(tripla[1])
        operando2 = float(tripla[2])

        if operador == '+':
            print(f'Resultado: {operando1 + operando2}')

        elif operador == '-':
            print(f'Resultado: {operando1 - operando2}')

        elif operador == '*':
            print(f'Resultado: {operando1 * operando2}')

        elif operador == '/':
            print(f'Resultado: {operando1 / operando2}')

    return EX_OK


# Seção Principal do Script - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
