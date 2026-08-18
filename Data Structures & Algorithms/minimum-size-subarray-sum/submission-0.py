class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # return the value of the shortest subarray that is greater or equal to target
        # sliding window of some sort would help
        # shrink the window until smallest possible 

        l = 0

        minL = float('inf')
        cum = 0

        for r in range(len(nums)):
            cum += nums[r]
            while cum >= target:
                minL = min(minL, r - l + 1)
                cum -= nums[l]
                l += 1

        if minL == float('inf'):
            return 0

        return minL

