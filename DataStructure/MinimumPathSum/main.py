class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        
        n = len(grid[0])
        print(m)
        print(n)
        dp = [[x for x in range(n)] for y in range(m)]   
        print(dp)
        for x in range(m):
            for y in range(n):
                dp[x][y] = grid[x][y]                
                if y > 0 and x > 0:
                    if(dp[x][y-1] < dp[x-1][y]):
                        dp[x][y] += dp[x][y-1]
                    else:
                        dp[x][y] += dp[x-1][y]
                elif x > 0:
                    dp[x][y] += dp[x-1][y]
                elif y > 0:
                    dp[x][y] += dp[x][y-1]        
        return dp[x][y]