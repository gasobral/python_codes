#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementalção de Funções - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Dados o número n de alunos de uma determinada classe e as 3 notas das provas
de cada aluno, calcular a média aritmética das provas de cada aluno, a média
da classe, o número de aprovados e o número de reprovados (critério de
aprovação: média maior ou igual a 5.0).
    """

    print(main.__doc__)

    n = int(input("Digite a quantidade de alunos: "))

    media_classe = float(0)
    qtde_aprovados = 0

    for i in range(n):
        media_aluno = float(0)

        for j in range(3):
            nota = float(input(f'Digite a nota {j +1} do aluno {i +1}: '))
            media_aluno = media_aluno + nota

        media_aluno = media_aluno / 3
        media_classe = media_classe + media_aluno
        print(f'Média do aluno {i +1}: {media_aluno}')

        if media_aluno >= float(5):
            qtde_aprovados = qtde_aprovados +1

    media_classe = media_classe / n
    qtde_reprovados = n - qtde_aprovados

    print(f'Média da classe: {media_classe}')
    print(f'Número de alunos aprovados: {qtde_aprovados}')
    print(f'Número de alunos reprovados: {qtde_reprovados}')

    return EX_OK


# Parte Principal do Script - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
