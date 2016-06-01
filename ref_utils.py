#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Description - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Code written by gasobral@gmail.com                                          #
# This program loads bibtex files and make annotations to it.                 #

# Module Import - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys

# Data Structures - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# { function_name = key : function_pointer = value } #
know_cmd = {}

# Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def read_cmd():
    """Reads a command from command from stdin.\n\
If it's a valid command then return the respective function.\n\
Otherwise returns None.
"""
    pass


def main(args) :
    """This program loads bibtex files, create notes to it and remove unused\n\
references."""

    print(main.__doc__)
    exit_status = False # variable that show if the program ends or not #

    # main loop, read files, make notes, etc #
    while exit_status = False :
        user_cmd = input()

    return 0


# Main Script - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
return_code = 0

if __name__ == "__main__" :
    return_code = main(sys.argv)

sys.exit(return_code)
