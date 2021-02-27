class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_rev = x_str[::-1]
        return x_str == x_rev

if __name__== '__main__':
    solution = Solution()

    result = solution.isPalindrome(12321)
    print(result == True)