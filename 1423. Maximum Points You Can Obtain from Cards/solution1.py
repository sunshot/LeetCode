from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        k = len(cardPoints) - k
        if k == 0:
            return total
        # Now we transfer the problem to k sliding window, return the min sum
        ans = sum(cardPoints[0:k])
        curr_sum = ans
        left = 0
        for right in range(k, len(cardPoints)):
            curr_sum = curr_sum + cardPoints[right] - cardPoints[left]
            ans = min(ans, curr_sum)
            left += 1
        return total - ans
            
if __name__== '__main__':
    solution = Solution()

    cardPoints = [100,40,17,9,73,75]
    k = 3
    ans = solution.maxScore(cardPoints, k)
    print(ans == 248)
        