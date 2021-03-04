# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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