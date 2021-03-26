# [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1

Input: n = 3, bad = 1
Output: 1
```

Constraints:

- 1 <= bad <= n <= 2^31 - 1


Solution1: Binary Search. But need to pay attention is we find isBadVersion(mid) is True.

Runtime: 32 ms, faster than 50.16% of Python3 online submissions for First Bad Version.


https://leetcode.com/problems/first-bad-version/solution/

If you are setting mid = (left + right) /2,  you have to be very careful. Unless you are using a language that does not overflow such as Python, (left + right) /2 could overflow. One way to fix this is to use left + (right - left)/2 instead.
