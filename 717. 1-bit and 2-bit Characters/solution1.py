from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n:
            if bits[i] == 0:
                if i == n-1:
                    return True
                i += 1
            else:
                if i+1 < n:
                    i += 2
                else:
                    return False
        return False

if __name__== '__main__':
    solution = Solution()

    bits = [1, 1, 1, 0]
    print(solution.isOneBitCharacter(bits))