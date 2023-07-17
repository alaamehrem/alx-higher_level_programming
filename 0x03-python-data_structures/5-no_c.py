#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for _char in my_string:
        if (_char == 'c') or (_char == 'C'):
            _char = ""
        new_string += _char
    return new_string
