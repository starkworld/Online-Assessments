
words = ['illuminated', 'animosity', 'deoxyribonucleic', 'container', 'lit', 'amity', 'encourage', 'lighted']
wordsToSynonyms = ['encourage:urge,boost,inspire', 'container:tin,can,bag,bottle', 'lighted:lit',
                   'illuminated:lit']
wordsToAntonyms = ['encourage:discourage', 'animosity:amity,like', 'lighted:dark']


def kangaroo(words, wordsToSynonyms, wordsToAntonyms):
    lst = []
    l = []
    count = 0
    for i in wordsToSynonyms:
        lst.append(i.split(':'))
    for j in wordsToAntonyms:
        l.append(j.split(':'))

    for i in range(len(lst)):
        for j in range(1, len(lst[0])):
            lst[i][j] = lst[i][j].split(',')
    for i in range(len(l)):
        for j in range(1, len(l[0])):
            l[i][j] = l[i][j].split(',')

    res_dct = {lst[i][j]: lst[i][j + 1] for i in range(0, len(lst), 1) for j in range(len(lst[0]) - 1)}

    for x in res_dct.keys():
        for y in res_dct[x]:
            c = 0
            j = 0
            if x in words:
                for i in range(len(x)):
                    if j < len(y):
                        if x[i] == y[j]:
                            c += 1
                            j += 1
                if c == len(y):
                    count += 1

    return count


print(kangaroo(words, wordsToSynonyms, wordsToAntonyms))
