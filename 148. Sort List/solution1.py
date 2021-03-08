from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # tail used to keep track of the tail of merged list
    # and use to link the new merged list
    tail = None
    # nexSubList always points to the next sub list to deal with
    nextSubList = None
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        start = head
        n = self.getCount(head)
        size = 1
        while size < n:
            self.tail = dummyHead
            while start:
                if not start.next:
                    self.tail.next = start
                    break
                mid = self.split(start, size)
                self.merge(start, mid)
                start = self.nextSubList
            start = dummyHead.next
            size = size * 2
        head = dummyHead.next
        return head
        
    def split(self, start: ListNode, size: int) -> ListNode:
        # will split the list from start, to make sure
        # start will point to the first size nodes
        # return mid will point to next size nodes
        # self.nextSubList will point to mid list's end's next
        midPrev = start
        end = start.next
        index = 1
        while index < size and (midPrev.next or end.next):
            if end.next:
                if end.next.next:
                    end = end.next.next
                else:
                    end = end.next
            if midPrev.next:
                midPrev = midPrev.next
            index += 1
        mid = midPrev.next
        midPrev.next = None
        self.nextSubList = end.next
        end.next = None
        # We split start list and mid list
        # also point to the next sub list
        return mid
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        while tail and tail.next:
            tail = tail.next
        # link the old tail with the head of merged list
        self.tail.next = dummy.next
        # update the old tail to the new tail of merged list
        self.tail = tail
        return dummy.next
    def getCount(self, head: ListNode) -> int:
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        return cnt

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

    nums = [-1,5,3,4,0]
    ans = solution.sortList(convert2ListNode(nums))
    print(convertFromListNode(ans))