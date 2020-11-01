def concatArr(a):
    b = a.copy()
    ls = []
    for i in a:
        for j in b:
            ls.append(str(i) + str(j))
    s = 0
    for i in ls:
        s += int(i)
    return s


print(concatArr([8]))
print(concatArr([2, 5, 15, 17]))
