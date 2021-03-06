# 496. Next Greater Element I

https://leetcode.com/problems/next-greater-element-i/

You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

Follow up: Could you find an O(nums1.length + nums2.length) solution?

## Solution

最直接的方式是 O(n^2)，即对 nums2 的每一个元素，找到它的 next greater element，并将结果存到 hash 中，有没有更好的方法呢？

使用栈，每次去判断当前遍历元素 x 是不是 栈顶元素的 next greater，如果是，则将栈 pop，并记录结果到 hash 中，最后，栈里面只有 next greater 为 -1 的那些元素

https://leetcode.com/problems/next-greater-element-i/discuss/97604/Python-Solution-with-O(n)

https://leetcode.com/problems/next-greater-element-i/discuss/97595/Java-10-lines-linear-time-complexity-O(n)-with-explanation


