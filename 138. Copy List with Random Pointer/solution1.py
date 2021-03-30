
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
        
        # deal with random pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # resore and return new list
        newhead = head.next
        new = None
        curr = head
        while curr:
            if new:
                new.next = curr.next
            new = curr.next
            curr.next = curr.next.next
            new.next = None
            curr = curr.next
        
        return newhead
            
        