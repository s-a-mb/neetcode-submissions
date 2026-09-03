class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # instrinct is big window to small window

        # sort array

        # when to reset prod

        # when prod gets read for while condition



        prod = 1
        res = set()
        counter = l = 0
        


        for r in range(len(nums)):
            prod *= nums[r]
            
            
        
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1
            
            counter += (r - l + 1)

        return counter

        

        # l r

        # step through nums, with a window of r - l + 1 each time, until r len nums

