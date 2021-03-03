class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        if not a:
            return -1
        for x in b:
            if x not in a:
                return -1
        if b in a:
            return 1
        aa = a + a[0]
        for i in range(len(b)):
            if b[i:i+2] not in aa:
                return -1
        q = (len(b) - 1) // len(a) + 1
        for i in range(2):
            if b in a * (q+i):
                return q+i
        return -1

if __name__== '__main__':
    solution = Solution()

    a = 'abc'
    b = 'cabcabca'
    result = solution.repeatedStringMatch(a, b)
    print(result == 4)