def trades(lis):
    lst1 = []
    for i in lis:
        j = i.split('|')
        lst1.append(int(j[0]) * int(j[1]))
    lst1.sort()
    largest_trades = sum(lst1[-3:])
    smallest_trades = sum(lst1[:2])
    return str(largest_trades) + '|' + str(smallest_trades)


print(trades(['25100|1107', '24593|1916', '24560|7369', '24974|2120', '24832|3239']))
