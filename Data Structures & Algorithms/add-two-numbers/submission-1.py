# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 
        # add node 1 and 2 and carry
        # find carry if existing
        # pass into next node
        
        def rec(node1, node2, c):

            if not node1 and not node2 and c == 0:
                return None

            
            
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            
            v_new = (v1 + v2 + c) % 10

            carry = (v1 + v2 + c) // 10

            new = rec(node1.next if node1 else 0, node2.next if node2 else 0, carry)

            return ListNode(v_new, new)
        
        return rec(l1, l2, 0)
        
    