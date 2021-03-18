# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Examples:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Input: nums1 = [2], nums2 = []
Output: 2.00000
```

Constraints:

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Follow up: The overall run time complexity should be O(log (m+n)).

Solution: https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

Solution1: O(m+n), 将两个有序链表 Merge 在一起， Merge 的过程中计算中位数

参考解答：Recursive Approach，将两个List切分成相等的两部分
