from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            # Let's swap curr.next and curr.next.next
            tmp = curr.next
            curr.next = curr.next.next
            tmp.next = curr.next.next
            curr.next.next = tmp
            curr = curr.next.next
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

    nums = [1,2,3,4,5,6]
    head = convert2ListNode(nums)
    head = solution.swapPairs(head)
    print(convertFromListNode(head))