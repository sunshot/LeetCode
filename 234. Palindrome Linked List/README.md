## Solution

找到 LinkedList 的中间节点，然后比较前后两部分

https://leetcode.com/problems/palindrome-linked-list/

与：

https://leetcode.com/problems/reverse-linked-list/

https://leetcode.com/problems/linked-list-cycle

https://leetcode.com/problems/linked-list-cycle-ii

https://leetcode.com/problems/reorder-list/

都是相同的思路和套路

用两个 pointer 找到中间节点

https://leetcode.com/problems/middle-of-the-linked-list

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## Solution1
所谓的 straightforward，找到中间节点，然后把结尾的一般先 reverse，然后再比较

## Solution2 and Solution3

讨论中的思路：https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

寻找中间节点的时候就可以把前半段 reverse，然后比较，很聪明

比较的过程中可以把前半段再恢复，更聪明
