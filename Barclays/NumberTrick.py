def checksum(number):
    a = str(number)
    lst = []
    summ = 0
    for i in a:
        if int(i) % 2 != 0:
            s = (str(2 * int(i)))
            if len(s) >= 2:
                for j in s:
                    summ = summ + int(j)
            else:
                lst.append((2 * int(i)))
            lst.append(int(summ))
            summ = 0
        else:
            lst.append(int(i))

    return sum(lst)


print(checksum(5678))
