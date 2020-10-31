from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        dp = [int(x) for x in matrix[0]]
        n = len(matrix)
        m = len(matrix[0])
        max_square = max(dp)
        for i in range(1,n):
            prev = dp[0]
            dp[0] = int(matrix[i][0])
            max_square = max(dp[0], max_square)
            for j in range(1,m):
                if matrix[i][j] == '1':
                    dp[j], prev = min(dp[j], dp[j-1], prev) + 1, dp[j]
                    if dp[j]>max_square:
                        max_square = dp[j]
                else:
                    dp[j], prev = 0, dp[j]
        return max_square**2