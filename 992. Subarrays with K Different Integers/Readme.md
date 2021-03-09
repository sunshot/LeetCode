# [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)


Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

```
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```

Similar problems:

https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

后两个需要会员才能看

直接的思路时 solution1，O(n^2)，Time Limit Exceeded，从 start = 0 开始遍历，对每一个 start，判断哪些符合条件的 subarray，利用 dict 来记录 subarray 里面出现的元素

参考解答：https://leetcode.com/problems/subarrays-with-k-different-integers/solution/
solution2，采用两个滑动窗口，[left1..right] 是 = k 的子数组（对 right 而言，第一次达到 k 的最小 left），[left2..right] 是 < K 的子数字 （对 right 而言，第一次从 K 变成 小于 K 的 left），left2 - left1 为当前right符合条件的子数组数量

参考解答似乎效率一般

从 submission 里面随机找的解答 solution3 和 solution4

start is the starting of the window, start_k is the starting point of k distinct integers,in the window start_k-start number are repeated, so 1+start_k - start number of subarrays are possible

[start_k..right] 正好有 k 个不同的元素，并且 A[start_k] 只出现 1 次，则 start_k - start + 1 都是相对于 right 符合条件的子数组

right 后面的元素，如果还满足正好有 k 个不同的元素，则继续寻找 start_k 让 A[start_k] 只出现 1 次；否则，删除 A[start_k]，start_k+1， start 挪到最新的 start_k 的位置 （因为之前的 start..start_k 和最新的 right 都不满足正好有 k 个不同的元素）

讨论区参考解答：
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!

For [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/):

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1
            while l < r and counter < r - l:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res = max(res, r - l)
        return res
```

For [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/):

```python
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1   
            while l < r and counter > 2:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res = max(res, r - l) 
        return res
```

For [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/):

```python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1   
            while l < r and counter > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res = max(res, r - l) 
        return res
```



https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

