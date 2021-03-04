# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        # always insert after this pointer
        p = dummy
        # always detect whether curr.next need to move
        curr = dummy
        
        while curr.next:
            if curr.next.val < x:
                # move curr.next after p
                if p.next != curr.next:
                    tmp = curr.next
                    if curr.next.next:
                        curr.next = curr.next.next
                    else:
                        curr.next = None
                    tmp.next = p.next
                    p.next = tmp
                    p = p.next
                else:
                    p = p.next
                    curr = curr.next
            else:
                curr = curr.next
        return dummy.next