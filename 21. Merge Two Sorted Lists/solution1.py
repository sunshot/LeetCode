from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                # select l1
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return head.next

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

    num1 = [1,2,4]
    num2 = [1,3,4]
    ans = solution.mergeTwoLists(convert2ListNode(num1), convert2ListNode(num2))
    print(convertFromListNode(ans))