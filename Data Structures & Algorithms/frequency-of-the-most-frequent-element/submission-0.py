class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # find the max possible frequency of an element'
        # i return only an amount
        nums.sort()
        max_freq = 0
        l = 0

        real = 0

        for r in range(len(nums)): # right side of the window
            
            real += nums[r]

            while nums[r] * (r - l + 1) > real + k:
                real -= nums[l]
                l += 1

        
            max_freq = max(max_freq, r - l + 1)

        
        return max_freq
