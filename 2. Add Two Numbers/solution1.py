from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        curr1 = l1
        curr2 = l2
        carry = 0
        curr = dummy
        while curr1 or curr2:
            value = carry
            if curr1:
                value += curr1.val
                curr1 = curr1.next
            if curr2:
                value += curr2.val
                curr2 = curr2.next

            carry = value // 10
            value = value % 10

            curr.next = ListNode(value)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)
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
    
if __name__ == '__main__':
    solution = Solution()

    # nums1 = [2,4,3]
    # nums2 = [5,6,4]

    nums1 = [9,9,9,9,9,9,9]
    nums2 = [9,9,9,9]

    ans = solution.addTwoNumbers(convert2ListNode(nums1), convert2ListNode(nums2))
    print(convertFromListNode(ans))