## 2020/10/17
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        dp = [[float('inf')] * (N+1) for _ in range(M+1)]
        dp[M][N-1] = 1
        dp[M-1][N] = 1
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]

if __name__ == "__main__":
    print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))