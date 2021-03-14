# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

- 1 <= nums.length <= 2 * 104

- -10 <= nums[i] <= 10

Solution1: O(n^2) 186 / 187 test cases passed. Status: Time Limit Exceeded. Use similar idea of dynamic programming.

Solution2: O(n). Refer to https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

问题的难点在于数组的元素可能有负数，因此需要记录到当前位置最大最小乘机，curr_max and curr_min，当 nums[i] 为负数时，curr_max and curr_min 需要进行交换，然后 curr_max = max(nums[i], nums[i] * curr_max), curr_min = min(nums[i], nums[i] * curr_min)


this is very similar to the " max cumulative sum subarray" problem. here you keep 2 values: the max cumulative product UP TO current element starting from SOMEWHERE in the past, and the minimum cumuliative product UP TO current element . it would be easier to see the DP structure if we store these 2 values for each index, like maxProduct[i],minProduct[i] .

at each new element, u could either add the new element to the existing product, or start fresh the product from current index (wipe out previous results), hence the 2 Math.max() lines.

if we see a negative number, the "candidate" for max should instead become the previous min product, because a bigger number multiplied by negative becomes smaller, hence the swap()
