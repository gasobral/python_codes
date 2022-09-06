#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dizemos que um número natural n com pelo menos dois algarismos é palíndrome
se

O primeiro algarismo de n é igual ao seu último algarismo,
O segundo algarismo de n é igual ao seu penúltimo algarismo

e assim sucessivamente.
Exemplos:
567765 e 32423 são palíndromes
567675 não é palíndrome

Dado um inteiro n, n >= 10, verificar se é palíndrome.
    """

    print("Digite um número: ", end = '')
    numero = int(input())

    if numero < 10:
        return EX_OK

    aux = numero
    reverso = 0

    while aux != 0:
        reverso = reverso * 10 + aux % 10
        aux = aux // 10
        
    if reverso == numero:
        print(f'{numero} é palíndromo!')
    else:
        print(f'{numero} não é palíndromo!')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
