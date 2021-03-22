from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        ans = set()
        
        nth_bit = 1 << n
        for i in range(2**n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            res = list(S)
            for j in range(n):
                if bitmask[j] == '1':
                    res[j] = res[j].swapcase()
            ans.add(''.join(res))
        
        return list(ans)

if __name__== '__main__':
    solution = Solution()

    S = 'a1b2'
    ans = solution.letterCasePermutation(S)
    print(ans)