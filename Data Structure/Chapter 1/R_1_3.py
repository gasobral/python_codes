#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def minmax(data):
    """
Função que retorna os elementos mínimo e máximo de uma sequência de
um ou mais elementos.

Parâmetros
----------
    data (list): uma sequencia de um ou mais inteiros

Retorno
-------
    tuple: contém o mínimo e o máximo de tuple
    """

    minimo = maximo = data[0]

    for elemento in data:
        if elemento > maximo:
            maximo = elemento

        if elemento < minimo:
            minimo = elemento

    return (minimo, maximo)


def main(args):
    """
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largets numbers, in
the form of tuple of length two. Do not use built-in functions min or
max in implementing your solution.
    """

    n = int(input("Digite o número de elementos: "))
    sequencia = []

    for i in range(n):
        elemento = int(input("Digite um inteiro: "))
        sequencia.append(elemento)

    minimo, maximo = minmax(sequencia)
    print(f'Máximo: {maximo}\n'
          f'Mínimo: {minimo}')
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
