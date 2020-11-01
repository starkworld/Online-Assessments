def roman_number(number):
    roman_char = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV', 1: 'I'}
    out = ''
    for val, c in roman_char.items():
        if number < val:
            continue
        repeat, number = divmod(number, val)
        out += repeat * c
    return out
