# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = slow.next
        prev = None

        slow.next = None

        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp

        one = head
        two = prev

        
        while two:
            temp1 = one.next
            temp2 = two.next
            one.next = two
            two.next = temp1
            one = temp1
            two = temp2

