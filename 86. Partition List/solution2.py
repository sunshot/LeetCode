# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        before = before_dummy = ListNode(0)
        after = after_dummy = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_dummy.next
        head = before_dummy.next
        return head