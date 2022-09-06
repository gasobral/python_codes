#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def remove_pontuacao2(s):
    """
    """

    return s.translate(str.maketrans('', '', string.punctuation))


def remove_pontuacao(s):
    """
    """

    for pontuacao in string.punctuation:
        s = s.replace(pontuacao, '')

    return s


def main(args):
    """
Write a short Python function that takes a string s, representing a
sentence, and returns a copy of the string with all punctuation
removed. For example, if given the string "Let's try, Mike", this
function would return "Lets try Mike".
    """

    print(main.__doc__)
    s = input()
    print(remove_pontuacao2(s))
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    import string
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
