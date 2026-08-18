# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        dummy = head
        nums = []
        
        while dummy:
            nums.append(dummy.val)
            dummy = dummy.next

        n = len(nums) // 2

        oneHalf = nums[:n]
        twoHalf = nums[n:][::-1]

        res = 0

        for i in range(n):
            res = max(res, oneHalf[i] + twoHalf[i])
        
        return res


