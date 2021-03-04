# 86. Partition List

https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

## Solution

题目的意思只需要将小于 x 的 node 移到它的前面，要保证以前的顺序，不需要排序或其他操作，straightforward 的方法就是两个指针的方式，p 指向当前小于 x 的最后的node，新的小于 x 的 node 都要插到 p 的后面，curr 指向当前遍历的节点的前一个节点，每次都是对 curr.next 进行判断操作。为了方便起见，设置一个 dummy 节点作为新的 head 节点。

如果 curr.next 小于 x，则需要将它移动到 p 的后面，同时 p 后移一位，curr不动

否则，p不动，curr后移一位。直到 curr 指到队尾。

参考解答的方法：

https://leetcode.com/problems/partition-list/solution/

直接构造两个linkedlist，before 链接小于 x 的node，after 链接大于等于 x 的node
