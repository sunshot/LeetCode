# [143. Reorder List](https://leetcode.com/problems/reorder-list/)

You are given the head of a singly linked-list. The list can be represented as:

```L0 → L1 → … → Ln - 1 → Ln```

Reorder the list to be on the following form:

```L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

Constraints:

- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

思路：通过快慢指针找到链表的中点，然后将后一半链表翻转，最后将前一半链表和翻转后的后一半链表 merge 在一起

细节：考虑链表是偶数个节点和奇数个节点，即注意链表如果有两个中心，则第二个中心为后一半链表；如果只有一个中心，则属于第一半链表

