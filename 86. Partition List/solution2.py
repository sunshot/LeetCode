class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

    nums = [1,4,3,2,5,2]
    x = 3
    head = convert2ListNode(nums)
    head = solution.partition(head, x)
    result = convertFromListNode(head)
    print(result)