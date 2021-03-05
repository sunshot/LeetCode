# 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

https://leetcode.com/problems/min-stack/

本题的关键是：Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

stack里面每一个元素都带有额外的熟悉 currMin，即从队首到它为止最小的元素

类似问题：

https://leetcode.com/problems/max-stack/
