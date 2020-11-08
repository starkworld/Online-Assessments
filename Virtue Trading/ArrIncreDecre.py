def solution(A):
    # write your code in Python 3.6
    # if len(A) == 4:
    #     return A
    # k = 0
    if A == sorted(A, reverse=True):
        return A
    else:
        while A != sorted(A):
            for i in range(1, len(A) - 1):
                if A[i - 1] > A[i] < A[i + 1]:
                    A[i] = A[i] + 1
                elif A[i - 1] < A[i] > A[i + 1]:
                    A[i] = A[i] - 1
        return A


print(solution([1, 6, 3, 4, 3, 5]))
