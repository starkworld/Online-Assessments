from itertools import combinations

import time

start = time.time()


# sleeping for 1 sec to get 10 sec runtime


# program body ends

# end time


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c + [a[0]]]
    return cs


def maxCapacity(sequence, ma):
    k = combs(sequence)
    return max([sum(i) for i in k if sum(i) <= ma])


def weightCapcity(weights, maxSize):
    # Creating all sublists and appending into subs
    subs = []
    for i in range(0, len(weights) + 1):
        # Creating sublist using combinations, which is built in function in python
        temp = [list(x) for x in combinations(weights, i)]
        if len(temp) > 0:
            subs.extend(temp)
    # Intializing maximum with zero value
    maximum = 0
    # For each list calculating a value
    for i in subs:
        count = 0
        for j in i:
            count = count + j
        # Finding maximum using condition
        if count > maximum and count <= maxSize:
            maximum = count
    # Returning maximum
    return maximum


weights = [7, 10, 19, 37, 30, 11, 35, 16]
max_Capacity = 49
# weights = [1, 3, 5]
# max_Capacity = 7
print(maxCapacity(weights, max_Capacity))
print(weightCapcity(weights, max_Capacity))

# time.sleep(1)
end = time.time()
print(f"Runtime of the program is {end - start}")
