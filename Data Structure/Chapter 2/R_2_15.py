#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Classes - - - - - - - - - - - - - - - - - - - - - #
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d

        elif isinstance(d, list):
            self._coords = []

            for elemento in d:
                self._coords.append(elemento)

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

    def __radd__(self, other):
        return self.__add__(other)

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

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree!')

        result = 0

        for j in range(len(self)):
            result = result + self[j] * other[j]

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
The Vector class of Section 2.3.3 provides a constructor that takes an
integer d, and produces a d-dimensional vector with all coordinates
equal to 0. Another convenient form for creating a new vector would be
to send the constructor a parameter that is some iterable type
representing a sequence of numbers, and to create a vector with
dimensional equal to the length of that sequence and coordinates equal
to the sequence values. For example, Vector([4,7,5]) would produce a
three-dimensional vector with coordinates <4,7,5>. Modify the
constructor so that either of these forms is acceptable; that is, if a
single integer is send, it produces a vector of that dimension with all
zeros, but if a sequence of numbers is provided, it produces a vector
with coordinates based on that sequence.
    """

    print(main.__doc__)

    v = Vector(5)
    v[0] = 1
    v[1] = 2
    v[2] = 3
    v[3] = 4
    v[4] = 5

    u = Vector([0,1,0,1,1])
    print(u)

    print(u * v)

    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
