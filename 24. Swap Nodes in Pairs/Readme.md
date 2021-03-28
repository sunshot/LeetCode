# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

Given a linked list, swap every two adjacent nodes and return its head.

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

```

Constraints:

- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)

Solution1: Use a dummy node to point the head of list, and let curr = dummy, then we will always swap curr.next and curr.next.next. 

Runtime: 24 ms, faster than 95.54% of Python3 online submissions for Swap Nodes in Pairs.

