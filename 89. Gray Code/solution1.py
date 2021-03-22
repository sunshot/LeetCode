from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        '''
        from up to down, then left to right
    
        0   1   11  110
                10  111
                    101
                    100

        start:      [0]
        i = 0:      [0, 1]
        i = 1:      [0, 1, 3, 2]
        i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
        '''
        
        ans = [0]
        for i in range(n):
            ans += [x | (1 << i) for x in reversed(ans)]
        
        return ans

if __name__== '__main__':
    solution = Solution()

    n = 3
    ans = solution.grayCode(n)
    print(ans)