# [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

```
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```

Note:

- -30000 <= A[i] <= 30000
- 1 <= A.length <= 30000

Similar to 
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)
- [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) This seems to minimum erasure value but elements maybe negative.


Solution1: We compute max and min sum of subarray, and also sum(A), then we can get the possible max sum for circular array. Runtime: 512 ms, faster than 76.84% of Python3 online submissions for Maximum Sum Circular Subarray.

[Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem) for Maximum subarray problem.

```python
def max_subarray(numbers):
    """Find the largest sum of any non-empty contiguous subarray."""
    best_sum = float('-inf')  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

See multiple solutions: https://leetcode.com/problems/maximum-sum-circular-subarray/solution/

My solution is similar to https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass


