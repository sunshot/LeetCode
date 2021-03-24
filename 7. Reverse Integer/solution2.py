class Solution:
    def reverse(self, x: int) -> int:
        minus = ''
        if x < 0:
            minus = '-'
            x = x * (-1)
        xstr = str(x)
        result = ''
        addFirst = False
        for i in range(1, len(xstr)+1):
            a = xstr[-i]
            if not addFirst and a == '0':
                continue
            else:
                addFirst = True
                result = result + a 
        result = minus + result
        if result == '':
            result = '0'
        y = int(result)
        if y<(-1)*(2**31) or y>2**31-1:
            return 0
        return y

if __name__== '__main__':
    solution = Solution()

    x = 123
    ans = solution.reverse(x)
    print(ans)