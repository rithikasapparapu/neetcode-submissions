class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.area = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            self.area += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            return self.area

        for i in range(ROWS):
            for j in range(COLS):
                self.area = 0
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area



        