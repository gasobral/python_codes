#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


lista = []

try:
    lista[1] = "teste"

except IndexError:
    print("Don't try buffer overflow attacks in Python")
