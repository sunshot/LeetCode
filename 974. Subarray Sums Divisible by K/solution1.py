from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        #sum:num of the sum
        d = {0:1}
        currSum = 0
        for num in A:
            currSum += num
            mod = currSum % K
            if mod in d:
                ans += d[mod]
                d[mod] += 1
            else:
                d[mod] = 1
        return ans

if __name__== '__main__':
    solution = Solution()

    A = [4,5,0,-2,-3,1]
    K = 5
    ans = solution.subarraysDivByK(A, K)
    print(ans == 7)

