# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        # goal is to get the current node replaced by temp, which is the next node. next node is prev node

        # concurrent node is saved to temp
        # concurrent node is replaced by prev
        # prev is replaced by current
        # current is replaced by temp

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev
        
            
            