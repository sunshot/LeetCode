# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        fast = head
        i = 1
        while i < k and fast and fast.next:
            fast = fast.next
            i += 1
        if not fast.next:
            # i is list length
            k = k % i
            if k == 0:
                return head
            fast = head
            i = 1
            while i < k and fast and fast.next:
                fast = fast.next
                i += 1
        fast = fast.next
        slow = head
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # fast is tail, slow point to the node before the new head
        newhead = slow.next
        slow.next = None
        fast.next = head
        head = newhead
        return head