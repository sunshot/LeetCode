from typing import List
import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = 0
        d_cnt = collections.defaultdict(int)
        formed = 0
        start = 0
        start_k = 0
        
        # start is the starting of the window
        # start_k is the starting point of k distinct integers
        # in the window start_k-start number are repeated
        # so 1+start_k - start number of subarrays are possible
        
        for x in A:
            d_cnt[x] += 1
            if d_cnt[x] == 1:
                formed += 1
            if formed == K+1:
                d_cnt[A[start_k]] -= 1
                if d_cnt[A[start_k]] == 0:
                    formed -= 1
                    start_k += 1
                    start = start_k
            if formed == K:
                while d_cnt[A[start_k]] > 1:
                    d_cnt[A[start_k]] -= 1
                    start_k += 1
                # Until d_cnt[A[start_k]] = 1
                ans += start_k - start + 1
        return ans

if __name__== '__main__':
    solution = Solution()

    A = [1,2,1,3,4]
    K = 3
    result = solution.subarraysWithKDistinct(A, K)
    print(result)