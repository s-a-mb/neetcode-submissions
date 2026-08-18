class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        l = 0
        minDif = float('inf')

        for r in range(k - 1, len(nums)):
            cur = nums[r] - nums[l]

            minDif = min(cur, minDif)

            l += 1
        
        return minDif
            
