# [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Input: head = [1,2,3,4], node = 3
Output: [1,2,4]

Input: head = [0,1], node = 0
Output: [1]

Input: head = [-3,5,-99], node = -3
Output: [5,-99]

```

Constraints:

- The number of the nodes in the given list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node

Solution1: 没有思路，看了答案才恍然大悟，把 node 下一个节点的 value 拷贝到 node 处，然后删除 node 的下一个节点。

https://leetcode.com/problems/delete-node-in-a-linked-list/solution/

