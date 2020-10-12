def solution(string):
    lst = []

    for length in range(1, len(string) + 1):
        # print('length:', length)
        for x in range(0, len(string) - length + 1):
            substring = string[x:x + length]
            # print(substring, len(set(substring)))
            if len(set(substring)) == 1:
                lst.append(substring)

    return len(lst)


print(solution('zzzyz'))
