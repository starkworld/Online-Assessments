def reArrangeArr(a):
    b = []
    j = len(a)-1
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[round(i/2)])
        else:
            b.append(a[j])
            j -= 1

    return b

print(reArrangeArr([1,2,3,4,5,6,7,8]))