class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        maxR = len(grid)
        maxC = len(grid[0])
        res = 0

        def dfs(r, c):

            if r >= maxR or c >= maxC or r < 0 or c < 0 or grid[r][c] == '0':
                return 0
            
            

            grid[r][c] = '0'

            dfs(r + 1, c) 
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

            return 1
            
        
        for i in range(maxR):
            for j in range(maxC):
               res += dfs(i, j)

        
        return res