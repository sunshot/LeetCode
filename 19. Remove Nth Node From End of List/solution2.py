from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        # Now slow point to n-1 th node
        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return dummy.next
        
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

    nums = [1,2,3,4,5]
    n = 2
    head = convert2ListNode(nums)
    head = solution.removeNthFromEnd(head, n)
    result = convertFromListNode(head)
    print(result)