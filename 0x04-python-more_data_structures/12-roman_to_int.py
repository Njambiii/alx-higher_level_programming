#!/usr/bin/python3


def roman_to_int(roman_string):
    units = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
             'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
             'CM': 900, 'M': 1000}

    n = 0
    skip = False
    if (roman_string is not None) and isinstance(roman_string, str):
        str_len = len(roman_string)
        for i in range(str_len):
            base = 0
            key = roman_string[i]
            if (i + 1) < str_len:
                key += roman_string[i+1]
                base = units.get(key)

            if not skip:
                if base:
                    n += base
                    skip = True
                    continue
                else:
                    key = roman_string[i]
                    base = units.get(key)
                    n += base
            skip = False
    return n
