#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Sabe-se que um número da forma n^3 é igual a soma de n ímpares consecutivos.
Exemplo:
1^3 = 1 +
2^3 = 3 + 5
3^3 = 7 + 9 + 11
4^3 = 13 + 15 + 17 + 19
Dado m, determine os ímpares consecutvios cuja soma é igual a n^3 para n
assumindo valores de 1 a m.
    """

    print(main.__doc__)

    m = int(input("Digite um inteiro postivo: "))
    numero_impar = 1

    for i in range(1, m +1):
        soma = 0
        j = 0

        while j < i:
            soma = soma + numero_impar
            numero_impar = numero_impar + 2
            j = j + 1

        print(f'{i}^3 = {soma}')

    return EX_OK

# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
