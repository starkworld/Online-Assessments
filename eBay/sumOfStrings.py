from itertools import zip_longest


def sm(s1, s2):
    a, b = [], []
    a.extend(s1)
    b.extend(s2)
    res = [int(x) + int(y) for x, y in zip_longest(a, b, fillvalue=0)]
    s = ''
    for i in res[::-1]:
        s += str(i)
    return s


print(sm('99', '99'))
