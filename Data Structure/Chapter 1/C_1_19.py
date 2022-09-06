#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Demonstrate how to use Python's list comprehension syntax to produce
# the list ['a', 'b', 'c', ..., 'z'], but without having to type all 26
# such characteres literally

print([chr(i) for i in range(ord('a'), ord('z')+1)])
