def diceThrow(a, b, c):
    if a == b == c:
        return 1000 * a
    elif a == b or a == c:
        return 500 * a
    elif b == a or b == c:
        return 500 * b
    elif c == a or c == b:
        return 500 * c
    else:
        return 100 * min(a, b, c)


print(diceThrow(3, 8, 9))
