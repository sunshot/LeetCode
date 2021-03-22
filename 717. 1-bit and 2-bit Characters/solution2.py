from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n-1:
            i += bits[i] + 1
        return i == n-1

if __name__== '__main__':
    solution = Solution()

    bits = [1, 1, 1, 0]
    print(solution.isOneBitCharacter(bits))