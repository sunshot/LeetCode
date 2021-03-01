## 19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

这个题最直接的方式就是两遍遍历 List，第一遍找到 List的长度 L，然后相当于删除 L-n+1 的节点（从头开始数，head节点是第一个）

技巧是设置一个 dummy node，指向 head，这样能避免过多的边缘条件检测

更巧妙的方法是维护两个指针，两个指针之间间隔 n+1 ，即第一个指针的序号是 i，第二个指针的序号是 i+n+1，这样当第二个指针指向None时，第一个指针正好指向倒数 n+1 个节点，删除它的下一个节点即可

Solution1 没有设置 dummy 节点，需要多种判断

Solution2 设置了 dummy 节点，代码更优雅