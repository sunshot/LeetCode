# 61. Rotate List

https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

## Test case

```python
[1,2,3,4,5]
2
[0,1,2]
4
[0,1,2]
100
[1,2,3,4,5]
5
[1,2]
1
[1,2,3,4,5]
10
```

## Solution

用两个指针的方式，因为我们需要知道队尾，队尾最后要指到队首，用 fast 和 slow 两个指针，初始 slow 指向head，fast.next 指向 head index + k + 1，即 fast 指向 head index + k。考虑到 k 可能比队列长度要长，因此第一次遍历需要顺便求出队列的长度

```python
        fast = head
        i = 1
        while i < k and fast and fast.next:
            fast = fast.next
            i += 1
```

这个循环结束后，fast 指向第 k 个位置，或者 fast 指向队尾，此时可以求出队列的长度即为 i，然后 ``k = k % i``，再次同样的循环，此时 k 小于 队列长度，fast指向第 k 个位置，将 fast 后移一位，就能满足 slow = head， fast 指向 head index + k

```python
        fast = fast.next
        slow = head
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # fast is tail, slow point to the node before the new head
```

最后 fast 已经指向队尾， slow 下一个节点是新的队首，很好处理了
