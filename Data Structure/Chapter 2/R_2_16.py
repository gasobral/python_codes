#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Our Range class, from Section 2.3.5, relies on the formula
# max(0, (stop - start + step -1) // step)
# to compute the number of elements in the range. It is not immediately
# evident why this formula provides the correct calculation, even if
# assuming a postive step size. Justify this formula, in you own words.

# início do intervalo: start
# fim do intervalo:    stop + step -1, pois o extremo do intervalo não
#                                      é incluído
# número de elementos no invervalo:
# (stop + step -1 - start) // step
# quantidade de start * step elementos dentro do intervalo
# stop + step -1 - start
