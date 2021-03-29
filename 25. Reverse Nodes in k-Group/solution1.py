from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        begin = dummy
        end = dummy
        
        # begin always points to the node before the head of k nodes
        # end points to the end of k nodes
        while end and end.next:
            
            # move end to the end
            for _ in range(k):
                if not end or not end.next:
                    return dummy.next
                end = end.next
                
            # Now reverse [begin.next, end]
            curr = end.next
            next_begin = begin.next
            p = begin.next
            end.next = None
            while p:
                tmp = p.next
                p.next = curr
                curr = p
                p = tmp
            begin.next = curr
            begin = next_begin
            end = next_begin
        
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
    k = 3

    head = convert2ListNode(nums)

    ans = solution.reverseKGroup(head, k)

    print(convertFromListNode(ans))