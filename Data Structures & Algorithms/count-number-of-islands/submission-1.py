class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, r, c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)
            return
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        return count


        