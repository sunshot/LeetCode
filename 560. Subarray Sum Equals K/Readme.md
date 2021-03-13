# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

```
Input: nums = [1,1,1], k = 2
Output: 2
```

We can borrow some ideas from [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

Solution1: Time Limit Exceeded, 72 / 89 test cases passed. O(n^2)

Solution2: 根据提示：What about storing sum frequencies in a hash table? Will it be useful? 进行优化，sumDict[i]表示从 nums[0..i] 的元素的和（包括i），再用一个hash表记录对应 sumDict[i] 值的个数，这样在遍历 i 时，只需要看 k + sumDict[i-1] 这个值在hash表中右多少个，则从i起始的 subarray 就有多少个，为了遍历 i+1 时，不考虑 0..i 的 sumDict 在hash表中的个数，需要从删除 sumDict[i]，最终算法复杂度 O(n)

Solution3: 根据参考解答：https://leetcode.com/problems/subarray-sum-equals-k/solution/ 实质时在 Solution2 的基础上进行优化，与 Hash 解法的 2Sum 类似，每次看 i 位置时，以 i 位置作为结束的 subarray，判断 i 前面有没有可能存在的起点？起点 j 需要满足： sumDict[i] - sumDict[j-1] = k ，考虑到单个元素也可以，需要实现把 sumHash[0] = 1 放进去，然后对每个位置 i，判断已有的 sumHash 中有无 currSum - k

