# 76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

采用两个 pointers，滑动窗口的方式来判断和修改窗口大小

- 如何判断 s[left:right+1] 包含了所有 t 的字符？
- 初始找到一个窗口后，先缩减窗口长度(left--)，直到不满足条件，然后开始增加窗口长度(right++)，直到满足条件，最终找到后还需要再缩减一下

Solution1 直接比较两个hash，比较慢

参考解答：

https://leetcode.com/problems/minimum-window-substring/solution/

记录 t 中不同字符的个数，然后判断窗口中如果某一个字符在 t 中，并且出现的次数与 t 中出现次数一样，则不同字符个数加 1， 用这个条件来判断，速度大增

另一个优化是先将 s 过滤，只保留在 t 中的字符，然后遍历过滤后的字符