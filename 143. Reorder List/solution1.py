from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = head
        tail = head.next
        while mid and tail and tail.next:
            mid = mid.next
            tail = tail.next.next
        
        # print(mid.val)
        # mid is the middle of link
        nexthalf = mid.next
        mid.next = None
        
        # reverse nexthalf
        lasthalf = None
        while nexthalf:
            tmp = nexthalf.next
            nexthalf.next = lasthalf
            lasthalf = nexthalf
            nexthalf = tmp
        tail = lasthalf
        
        curr = head
        while tail:
            tmp = tail.next
            tail.next = curr.next
            curr.next = tail
            curr = curr.next.next
            tail = tmp
            
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
    head = convert2ListNode(nums)
    solution.reorderList(head)
    print(convertFromListNode(head))