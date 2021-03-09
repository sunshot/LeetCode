from typing import List
import collections
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.formed = 0
    
    def add(self, x: int) -> None:
        self.count[x] += 1
        if self.count[x] == 1:
            self.formed += 1
    
    def remove(self, x: int) -> None:
        self.count[x] -= 1
        if self.count[x] == 0:
            self.formed -= 1
            
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if not A or not K or len(A) < K or len(set(A)) < K:
            return 0
        ans = 0
        window1 = Window()
        window2 = Window()
        ans = 0
        left1 = 0
        left2 = 0
        # use [left1..right] to track > K
        # use [left2..right] to track >= K
        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)
            
            while window1.formed > K:
                window1.remove(A[left1])
                left1 += 1
            
            while window2.formed >= K:
                window2.remove(A[left2])
                left2 += 1
            
            ans += left2 - left1
            
        return ans

if __name__== '__main__':
    solution = Solution()

    A = [1,2,1,3,4]
    K = 3
    result = solution.subarraysWithKDistinct(A, K)
    print(result)