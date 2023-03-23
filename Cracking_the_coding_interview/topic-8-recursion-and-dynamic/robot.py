class Solution:

    def uniquePathsWithObstacles(self, grid):
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid
        self.memo = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        return self.findNumberOfPaths(0,0)

    def findNumberOfPaths(self, cr, cc):
        if (cr >= self.rows or cc >= self.columns or self.grid[cr][cc] == 1):
            return 0
        if (cr == self.rows - 1 and cc == self.columns - 1):
            return 1
        if (self.memo[cr][cc] != 0):
            return self.memo[cr][cc]
        self.memo[cr][cc] = self.findNumberOfPaths(cr + 1, cc) + self.findNumberOfPaths(cr, cc + 1)
        return self.memo[cr][cc]
    
if __name__ == "__main__":
    test_grid = [
    [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0],
    [1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1],
    [0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
    [0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
    [0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0]]
    
    sol = Solution().uniquePathsWithObstacles(test_grid)
    print(sol)