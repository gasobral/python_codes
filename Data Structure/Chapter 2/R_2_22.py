#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Classes - - - - - - - - - - - - - - - - - - - - - #
class Sequence(metaclass = ABCMeta):
    """
Our own version of collections.Sequence abstract base class.
    """
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element af index j of the sequence"""

    def __contains__(self, val):
        """Returns True if val found in the sequence; False otherwise."""

        for j in range(len(self)):
            if self[j] == val:
                return True

        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise
           ValueError) """

        for j in range(len(self)):
            if self[j] == val:
                return True

        raise ValueError('value not in sequence')

    def count(self, val):
        """Return the number of elementos equal to given value."""
        k = 0

        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):

        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self[i] != other[i]:
                return False

        return True

    def __let__(self, other):
        for i in range(self):
            if self[i] >= other[i]:
                return False

        return True


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
In similar spirit to the previous problem, augment the Sequence class
with method __lt__, to support lexicographics comparison seq1 < seq2.
    """

    print(main.__doc__)
    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    from abc import ABCMeta, abstractmethod

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
