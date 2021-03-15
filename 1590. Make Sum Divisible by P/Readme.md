# [1590. Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/)

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

```
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
```

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

Solution1: This problem is similar to [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/). We can get ``target = sum(nums) % p``, then the problem is to find the minimum length subarrays to make sure its sum % p = target. We can use dict to store the cumulative sum mod p and also its latest index. Runtime: 504 ms, faster than 95.69% of Python3 online submissions for Make Sum Divisible by P.

