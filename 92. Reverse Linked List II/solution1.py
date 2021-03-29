from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left-1):
            if not pre or not pre.next:
                return dummy.next
            pre = pre.next
        
        # pre.next is the node of left
        if not pre.next:
            return dummy.next
        end = pre.next
        for _ in range(right - left):
            if not end or not end.next:
                return dummy.next
            end = end.next
        
        # end point to right node
        curr = end.next
        end.next = None
        p = pre.next
        while p:
            tmp = p.next
            p.next = curr
            curr = p
            p = tmp
        pre.next = curr
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
    left = 2
    right = 4
    head = convert2ListNode(nums)
    ans = solution.reverseBetween(head, left, right)
    print(convertFromListNode(ans))