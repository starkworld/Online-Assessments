def transform(word):
    count = 1
    length = ""
    if len(word) > 1:
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                count+=1
            else :
                length += word[i-1]+str(count)
                count=1
        length += (word[i]+str(count))
    else:
        i=0
        length += (word[i]+str(count))
    return length


print(transform('AAABBCCCAABDCC'))