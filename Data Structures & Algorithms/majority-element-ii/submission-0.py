class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_val = len(nums)//3

        res = []
        cnt = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if cnt > min_val:
                    res.append(nums[i-1])
                cnt = 1
            else:
                cnt +=1
        
        if cnt > min_val:
            res.append(nums[len(nums)-1])
        
        return res
            
            
