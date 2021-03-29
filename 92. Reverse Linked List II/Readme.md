# [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
```

Constraints:

- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

Follow up: Could you do it in one pass?

Solution1: This is followup of [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) and simple version of [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/). We can do the reverse when we find the left and right node.

Runtime: 20 ms, faster than 99.25% of Python3 online submissions for Reverse Linked List II.

