def mutate(num, arr):
    b = []
    for i in range(0, num):
        if i == 0:
            b.append(0 + arr[i] + arr[i + 1])
        elif i == num - 1:
            b.append(arr[i - 1] + arr[i] + 0)
        else:
            b.append(arr[i - 1] + arr[i] + arr[i + 1])
    return b


print(mutate(5, [4, 0, 1, -2, 3]))
