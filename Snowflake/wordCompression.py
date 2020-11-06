def compressWord(word, k):
    lst = []
    for char in word:
        if lst and lst[-1][0] == char:
            lst[-1][1] += 1
            if lst[-1][1] == k:
                lst.pop()
        else:
                lst.append([char, 1])
    r = ''
    for ch, count in lst:
        r += ch * count
    return r