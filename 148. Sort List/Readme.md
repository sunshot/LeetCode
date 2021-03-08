# 148. Sort List

https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

[MergeSort](https://en.wikipedia.org/wiki/Merge_sort) is the solution for this problem. We need sub problems: [Find Middle Of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) and [Merge two sorted linked lists](https://leetcode.com/problems/merge-two-sorted-lists/).

See the corresponding solutions in https://github.com/sunshot/LeetCode/tree/main/876.%20Middle%20of%20the%20Linked%20List and https://github.com/sunshot/LeetCode/tree/main/21.%20Merge%20Two%20Sorted%20Lists

MergeSort 分为 Top down 及 Bottom up，前者比较简单，先把 List 分为两部分，然后递归的对两部分分别 sort，最后将两个有序的 List merge到一起，不过因为递归，空间复杂度不满足题目要求，是 O(logn) 

Bottom up 则去除了递归，核心思想是 size = 1, 2, 4, ... 对 List 进行切分和归并，令 dummyHead.next = head, 首先需要求得 List 长度。

对每一个 size，从 dummyHead.next 开始，进行切分和归并，直到队尾。切分时，先找到 start 开头长为 size 的 List，再找到接下来的长度为 size 的 List，记其头为 mid，队尾为 end，end.next 为 nextsublist，先将 start 和 mid 进行归并，用 tail 来链接归并后的 List，然后将 start 指向 nextsublist，循环进行

切分时，给定 start 和 size，相当于需要找到 start 开头的 List 的结束，mid 开头的 List 的开始和结束，可以使用快慢指针的方式，不过需要注意边界条件

总体而言，Bottom up 自己写还是比较有挑战
