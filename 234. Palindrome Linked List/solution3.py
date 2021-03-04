from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # find the middle point and reverse the half
        fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = head.next
            head.next = rev
            rev = head
            head = tmp
        tail = head
        if fast:
            tail = head.next
        # Now rev is the head of first reversed half
        # We need to compare with the second half
        # And we need to restore the reversed first half
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            tmp = rev.next
            rev.next = head
            head = rev
            rev = tmp
            tail = tail.next
        return isPali
        
def convert2ListNode(nums: List[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for x in nums:
        node = ListNode(x)
        curr.next = node
        curr = curr.next
    return dummy.next

def convertFromListNode(head: ListNode) -> List[int]:
    if not head:
        return []
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,2,1]
    head = convert2ListNode(nums)
    result = solution.isPalindrome(head)
    print(result)