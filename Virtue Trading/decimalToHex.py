def toHex(dec):
    x = int((dec % 16))
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]


numbers = [0, 11, 16, 32, 33, 41, 45, 678, 574893]

print([toHex(x) for x in numbers])
print([hex(x) for x in numbers])

decimal = 257
hexadecimal = hex(decimal).lstrip("0x")
print(hexadecimal)
a = str(hexadecimal)
b = ''
for i in a:
    if i == '1':
        b += i
    elif i == '0':
        b += i
        print(a)

print(a)






