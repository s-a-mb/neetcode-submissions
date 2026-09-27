class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def subtract(n):
            if n < 0:
                return 0

            count = res = 0
            l = 0

            for r in range(len(nums)):

                count += nums[r]

                while count > n:
                    count -= nums[l]
                    l += 1
                
                res += (r - l + 1)
            
            return res
        
        return subtract(goal) - subtract(goal - 1)