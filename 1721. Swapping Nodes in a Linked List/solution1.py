from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        if not a or k > len(a):
            return head
        # Let swap a[k-1] and a[-k]
        a[k-1], a[-k] = a[-k], a[k-1]
        
        # convert list to ListNode
        dummy = ListNode(0)
        curr = dummy
        for x in a:
            node = ListNode(x)
            curr.next = node
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

    nums = [7,9,6,6,7,8,3,0,9,5]
    k = 5

    head = convert2ListNode(nums)
    ans = solution.swapNodes(head, k)

    print(convertFromListNode(ans))
