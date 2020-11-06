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
    j = [sum(i) for i in k if sum(i) <= ma]
    print(max(j))


# weights = [7, 10, 19, 37, 30, 11, 35, 16]
# max_Capacity = 49
weights = [1, 3, 5]
max_Capacity = 7
maxCapacity(weights, max_Capacity)

# time.sleep(1)
end = time.time()
print(f"Runtime of the program is {end - start}")
