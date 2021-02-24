# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # find the middle point
        mid = head
        fast = head.next
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        p = mid.next
        mid.next = None
        curr = None
        while p:
            tmp = p.next
            p.next = curr
            curr = p
            p = tmp
        #Now curr is the head of next half
        while head and curr:
            if head.val != curr.val:
                return False
            head = head.next
            curr = curr.next
        return True
        