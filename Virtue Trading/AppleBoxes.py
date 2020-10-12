def solution(A):
    # write your code in Python 3.6
    a = A[0]
    c = 0
    for i in sorted(A[1:]):
        a = a + i
        if a <= 5000:
            c += 1
    return c


print(solution([4250, 100, 30, 30, 100, 50, 100]))
