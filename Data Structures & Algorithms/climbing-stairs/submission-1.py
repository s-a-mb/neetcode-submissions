class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = [-1] * (n + 1)

        def count(n, dp):

            if n == 0 or n == 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = count(n - 1, dp) + count(n - 2, dp)

            return dp[n]

        return count(n, mem)

        