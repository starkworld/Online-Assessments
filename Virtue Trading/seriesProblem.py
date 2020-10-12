"""Sum of given series"""


def sumOfSeries(num):
    res = 0
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        res = res + (i / fact)
    return res


n = 100
print("Sum: ", sumOfSeries(n))
