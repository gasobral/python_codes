#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Classes - - - - - - - - - - - - - - - - - - - - - #
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):

        if len(self) != len(other):
            raise ValueError('dimensions must agree')

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]

        return result

    def __neg__(self):
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = -self[j]

        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Implement the __neg__ method for the Vector class of Section 2.3.3, so
that the expression -v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
    """

    print(main.__doc__)

    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(-v)
    total = 0

    for entry in v:
        total += entry

    print(f'total: {total}')
    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
