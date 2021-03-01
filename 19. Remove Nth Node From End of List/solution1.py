# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        slow = head
        fast = head
        i = 0
        while fast and i < n+1:
            fast = fast.next
            i += 1
        if i == n+1:
            while fast:
                fast = fast.next
                slow = slow.next
            # Now slow point to n-1 th node
            if slow.next:
                slow.next = slow.next.next
            else:
                slow.next = None
            return head
        else:
            # delete the head
            if i == n:
                return head.next
            else:
                print('wrong parameters')
                return None
      