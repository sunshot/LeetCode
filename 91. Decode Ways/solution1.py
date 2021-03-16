class Solution:
    def decode(self, s: str, i: int, j: int) -> int:
        # i: begin index
        # j: end index
        n = j - i
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6):
                return 2
            else:
                return 1
        m1 = self.decode(s, i+1, j)
        if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6):
            return m1 + self.decode(s, i+2, j)
        else:
            return m1
        
    
    def numDecodings(self, s: str) -> int:
        if '0' in s:
            s = s.replace('20', '10')
            strs = s.split('10')
            s = s.replace('10', '')
            if '0' in s:
                return 0
            # Now we can assume no zero in s, only 1-9
            ans = 1
            for a in strs:
                ans *= self.decode(a, 0, len(a))
            return ans
        else:
            return self.decode(s, 0, len(s))
        
        
        
        
if __name__ == '__main__':
    solution = Solution()

    # s = "226"
    # s = "11106"
    s = "111111111111111111111111111111111111111111111"
    ans = solution.numDecodings(s)
    print(ans == 1836311903)