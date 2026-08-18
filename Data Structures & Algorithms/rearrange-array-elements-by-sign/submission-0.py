class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # begins with a positive
        # negatives remain in the original order, as do positives
        # negatives and positives must alternate

        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
                pos.append(num)
            else:
                neg.append(num)
                neg.append(num)

        for i in range(len(nums)):

            if i % 2 == 0:
                nums[i] = pos[i]
            else:
                nums[i] = neg[i]
        
        return nums

        

        
            