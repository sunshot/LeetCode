class Solution:
    def convertToWords(self, num: int) -> str:
        # convert less than 1000 to words
        digi_words = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }
        houdred_digi = num // 100
        num = num % 100
        ans = ''
        if houdred_digi > 0:
            ans += digi_words[houdred_digi] + ' Hundred'
            if num == 0:
                return ans
        if num in digi_words:
            if len(ans) > 0:
                ans += ' '
            ans += digi_words[num]
        else:
            ten_digi = num - num % 10
            if len(ans) > 0:
                ans += ' '
            ans += digi_words[ten_digi] + ' ' + digi_words[num % 10]
        return ans
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.convertToWords(num)
        units = ['', 'Thousand', 'Million', 'Billion']
        s = str(num)
        seg = len(s) // 3
        first = len(s) % 3
        start = 0
        res = ''
        for i in range(seg, -1, -1):
            if first == 0:
                first = 3
                continue
            sub = int(s[start:start+first])
            start += first
            first = 3
            if sub == 0:
                continue
            ans = self.convertToWords(sub)
            if len(res)!=0:
                res += ' '
            res += ans
            if i > 0:
                res += ' ' + units[i]
        return res
        
if __name__ == '__main__':
    solution = Solution()

    num = 1234567891
    ans = solution.numberToWords(num)
    print(ans)