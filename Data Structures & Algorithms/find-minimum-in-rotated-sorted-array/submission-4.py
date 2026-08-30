class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        left = 0
        right = len(nums) - 1


        while left < right:
            if right - left == 1:
                return min(nums[left], nums[right])
            
            mid = int((right + left) / 2)
            print(nums[mid], mid)
            
            # what does left, right and mid look like depending on certain rotations?
            # 1-5, 2 rotations = 34512 -> 3 5 2
            #if mid > left and greater than mid
            # left = mid
            # 

            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid
                print(nums[left])
            else:
                right = mid

        return nums[mid]
                
