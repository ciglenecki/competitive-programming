from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], i: int, j: int):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return

            grid[i][j] = "+"

            dfs(grid, i, j - 1)  # up
            dfs(grid, i + 1, j)  # right
            dfs(grid, i, j + 1)  # down
            dfs(grid, i - 1, j)  # left

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":

                    dfs(grid, i, j)
                    counter += 1

        return counter
