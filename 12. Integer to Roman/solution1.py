class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 0 or num > 4000:
            return None
        ans = []
        if num // 1000 > 0:
            m = num // 1000
            num = num % 1000
            ans.extend(['M'] * m)
        if num >= 900:
            num = num - 900
            ans.append('CM')
        if num >= 500:
            num = num - 500
            ans.append('D')
        if num >= 400:
            num = num - 400
            ans.append('CD')
        if num // 100 > 0:
            c = num // 100
            num = num % 100
            ans.extend(['C'] * c)
        if num >= 90:
            num = num - 90
            ans.append('XC')
        if num >= 50:
            num = num - 50
            ans.append('L')
        if num >= 40:
            num = num - 40
            ans.append('XL')
        if num // 10 > 0:
            x = num // 10
            num = num % 10
            ans.extend(['X'] * x)
        if num >= 9:
            num = num - 9
            ans.append('IX')
        if num >= 5:
            num = num - 5
            ans.append('V')
        if num >= 4:
            num = num - 4
            ans.append('IV')
        if num > 0:
            ans.extend(['I'] * num)
        return ''.join(ans)

if __name__== '__main__':
    solution = Solution()

    num = 3999
    ans = solution.intToRoman(num)
    print(ans)