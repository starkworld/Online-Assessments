import functools
import operator
from typing import List


class Solution:
    def diffWaysToCompute(self, inp) -> List[int]:
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}

        tokens = self.tokenize(inp)
        nums = tokens[::2]
        operators = tokens[1::2]

        @functools.lru_cache(None)
        def evaluate(start, end):
            if start == end:
                return (nums[start],)

            results = []

            for mid in range(start, end):
                operation = operations[operators[mid]]
                for num1 in evaluate(start, mid):
                    for num2 in evaluate(mid + 1, end):
                        results.append(operation(num1, num2))

            return tuple(results)

        return evaluate(0, len(nums) - 1)

    @staticmethod
    def tokenize(text):
        tokens = [0]

        for char in text:
            if char.isdigit():
                tokens[-1] = tokens[-1] * 10 + int(char)
            else:
                tokens.append(char)
                tokens.append(0)

        return tokens


class Solutions:
    def diffWaysToCompute(self, input: str, memo={}) -> List[int]:
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]

        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])

                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n

s = Solutions()
print(s.diffWaysToCompute("2*3-4*5"))