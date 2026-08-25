class Solution:
    def rob(self, nums: List[int]) -> int:

        # rob this one and skip to i + 2, or skip this one
        # return max at each path

        dp = [-1] * len(nums)
        
        def rec(i):
            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(rec(i + 1), nums[i] + rec(i + 2))

            return dp[i]

        return rec(0)