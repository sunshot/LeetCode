from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        # left_k is the kth node
        left_k = curr
        right_k = dummy
        while curr:
            curr = curr.next
            right_k = right_k.next
        
        # Now we need to swap left_k and right_k
        # tmp = left_k.val
        # left_k.val = right_k.val
        # right_k.val = tmp
        left_k.val, right_k.val = right_k.val, left_k.val
        
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

    nums = [7,9,6,6,7,8,3,0,9,5]
    k = 5

    head = convert2ListNode(nums)
    ans = solution.swapNodes(head, k)

    print(convertFromListNode(ans))