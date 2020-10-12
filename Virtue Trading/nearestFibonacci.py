"""
Fibonacci number sequence problem, find the nearest Fibonacci number
"""


def fibs():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def nearestFib(n):
    """If n is fibo num return True and n
        Otherwiise return False and nearest Fibo"""

    for fib in fibs():
        if fib == n:
            return True, n
        elif fib < n:
            prev = fib
        else:
            # is n closest to prev or to fib?
            if n - prev < fib - n:
                return False, prev
            else:
                return False, fib


print(nearestFib(1))


