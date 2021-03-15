# [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

Constraints:

- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length


Similar to:
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) and see it in [github](https://github.com/sunshot/LeetCode/tree/main/239.%20Sliding%20Window%20Maximum). We can image this problem as Sliding Window Minmum, but easier.

Solution1: Runtime: 412 ms, faster than 76.52% of Python3 online submissions for Maximum Points You Can Obtain from Cards.

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray

