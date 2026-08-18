class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # dfs
        # find the first island tile to determine position as you traverse graph
        # from that tile, find the next island tile. You then add that tile to a running total, 
        # which then compares another value which the maxIsland 
        # I will need another array containing areas visited to make sure I don't get in a loop
        # 

        visited = set()

        xMax = len(grid)

        yMax = len(grid[0])




        def dfs(pos_x, pos_y):

            if  pos_x < 0 or pos_x == xMax or pos_y < 0 or pos_y == yMax or grid[pos_x][pos_y] == 0:
                return 0

            if (pos_x, pos_y) in visited:
                return 0
            else:
                visited.add((pos_x, pos_y))
            
            return 1 + dfs(pos_x, pos_y - 1) + dfs(pos_x, pos_y + 1) + dfs(pos_x + 1, pos_y) + dfs(pos_x - 1, pos_y)

        maxIsland = 0


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                maxIsland = max(maxIsland, dfs(x, y))

        return maxIsland
