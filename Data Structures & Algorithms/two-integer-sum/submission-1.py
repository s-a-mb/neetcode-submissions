class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s_nums = []

        for i, num in enumerate(nums):
            s_nums.append([num, i])

        s_nums.sort()

        small, big = 0, len(nums) - 1

        while s_nums[small][0] + s_nums[big][0] != target:
            if s_nums[small][0] + s_nums[big][0] > target:
                big -= 1
            else:
                small += 1
        
        return [min(s_nums[small][1], s_nums[big][1]), max(s_nums[small][1], s_nums[big][1])]
        
        





        