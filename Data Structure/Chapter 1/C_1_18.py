#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Demonstrate how to use Python's list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

print([i * (i+1) for i in range(0, 10)])
