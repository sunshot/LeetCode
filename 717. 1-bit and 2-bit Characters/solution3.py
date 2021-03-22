from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0
        
if __name__== '__main__':
    solution = Solution()

    bits = [1, 1, 1, 0]
    print(solution.isOneBitCharacter(bits))