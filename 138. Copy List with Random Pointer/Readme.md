# [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.

```

Constraints:

- 0 <= n <= 1000
- -10000 <= Node.val <= 10000
- Node.random is null or is pointing to some node in the linked list.

Hints:

- Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node.
- You may want to use extra space to keep old node ---> new node mapping to prevent creating multiples copies of same node.
- We can avoid using extra space for old node ---> new node mapping, by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For e.g.
Old List: A --> B --> C --> D
InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
- The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

Solution1: Follow the hints, using interweaving. O(n). Runtime: 28 ms, faster than 96.34% of Python3 online submissions for Copy List with Random Pointer.

The algorithm is composed of the follow three steps which are also 3 iteration rounds.

- Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
- Iterate the new list and assign the random pointer for each duplicated node.
- Restore the original list and extract the duplicated nodes.

https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)

