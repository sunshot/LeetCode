from typing import List
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = 0
        d_cnt = {}
        start = 0
        start_k = 0
        
        # start is the starting of the window
        # start_k is the starting point of k distinct integers
        # in the window start_k-start number are repeated
        # so 1+start_k - start number of subarrays are possible
        
        for x in A:
            d_cnt[x] = d_cnt.get(x, 0) + 1
            
            if len(d_cnt) == K+1:
                del d_cnt[A[start_k]]
                start_k += 1
                start = start_k
                
            if len(d_cnt) == K:
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