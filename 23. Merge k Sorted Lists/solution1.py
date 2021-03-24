from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = queue.PriorityQueue()
        for idx, node in enumerate(lists):
            if node:
                q.put((node.val, idx, node))
        while not q.empty():
            val, idx, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, idx, node))
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

    nums = [[1,4,5],[1,3,4],[2,6]]
    lists = []
    for num in nums:
        node = convert2ListNode(num)
        lists.append(node)
    
    ans = solution.mergeKLists(lists)
    print(convertFromListNode(ans))