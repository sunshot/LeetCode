## Test case

````
"babad"
"cbbd"
"a"
"ac"
"xabax"
"xabay"
"cdxabaxyy"
"cdxabaxdc"
"xabbbax"
"axabbbaxabc"
"abbcccbbbcaaccbababcbcabca"
"abcda"
"bananas"
"ababababababa"
````

## Solution

首先要清楚 Palindromic 的含义，相当于这个 String 是对称的，如 ``aba``, ``abba``，或者把这个 String reverse，跟自身相等

Solution1 就是很直接的方法，扫描整个字符串，如果已存在 Palindromic 字符串，判断当前扫描位置的字符串是否能归到已有的 Palindromic 上，构成更长的 Palindromic 字符串，如果不能，则判断当前 Palindromic 字符串是否最长。最早这里犯了一个错误，仅仅又从当前字符串重新判断，其实应该判断当前 Palindromic 字符串去掉一些起始字符串后，加上当前位置的字符串，是否还能构成 Palindromic 字符串。方法复杂度应该是 O(n^3)，不过实际测试更快：

Runtime: 56 ms, faster than 99.82% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 63.02% of Python3 online submissions for Longest Palindromic Substring.

Solution2 参考推荐的方法， O(n^2)：https://leetcode.com/problems/longest-palindromic-substring/solution/  对每一个字符，往其左右扩展，看看是否构成回文字符串，考虑到 ``aba``, ``abba`` 的情况，需要每个字符判断两次

Solution3 也是参考推荐的方法，动态规划

后两个方法的实际测试时间更长


类似问题：https://www.geeksforgeeks.org/longest-common-substring-dp-29/
