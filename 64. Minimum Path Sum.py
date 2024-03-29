class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0: dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
                elif i == 0 and j == 0:dp[i][j] = grid[i][j]
                elif i == 0: dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0: dp[i][j] = grid[i][j] + dp[i-1][j]
        return dp[-1][-1]
a = Solution()
print(a.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))