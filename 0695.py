## 2020/06/21
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        M = len(grid)
        N = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        self.islands = 0
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1:
                    self.dfs(x, y, grid, M, N, directions)
                    res = max(res, self.islands)
                    self.islands = 0
        return res
        
    def dfs(self, x0, y0, grid, M, N, directions):
        self.islands += 1
        grid[y0][x0] = 0
        for dx, dy in directions:
            x = x0 + dx
            y = y0 + dy
            if 0 <= x < N and 0 <= y < M and grid[y][x] == 1:
                self.dfs(x, y, grid, M, N, directions)

if __name__ == "__main__":
    Solve = Solution()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(Solve.maxAreaOfIsland(grid))