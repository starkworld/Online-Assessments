def coolFeature(a, b, query):
    count = 0
    lst = []
    for i in query:
        if len(i) == 2:
            for k in range(0, len(a)):
                for j in range(0, len(b)):
                    if a[k] + b[j] == i[1]:
                        count += 1
            lst.append(count)
            count = 0
        else:
            b[0] = i[2]

    return lst


print(coolFeature([1, 2, 3], [3, 4], [[1, 5], [0, 0, 1], [1, 5]]))
print(coolFeature([1, 2, 2], [2, 3], [[1, 4], [0, 0, 3], [1, 5]]))
