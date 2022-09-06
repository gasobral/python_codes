#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Importção de Módulos - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
import sys


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados o número n de alunos de uma turma de Introdução aos Autômatos a Pilha
e suas notas da primeira prova, determinar a maior e a menor nota obtidas
por essa turma (nota máxima = 100 e nota mínima = 0).
    """

    nota_max = float(0)
    nota_min = float(100)
    n = int(input())

    for i in range(n):
        nota = float(input())

        if nota > nota_max:
            nota_max = nota

        if nota < nota_min:
            nota_min = nota

    print("Nota máxima", nota_max)
    print("Nota mínima", nota_min)
    return 0


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
return_code = 0

if __name__ == "__main__":
    return_code = main(sys.argv)

sys.exit(return_code)
