# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # find the middle point and reverse the half
        mid = head
        fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = mid.next
            mid.next = rev
            rev = mid
            mid = tmp
        if fast:
            mid = mid.next
        # Now rev is the head of first reversed half
        # We need to compare with the second half
        while rev and rev.val == mid.val:
            rev = rev.next
            mid = mid.next
        return not rev
        