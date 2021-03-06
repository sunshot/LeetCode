class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = []
        while n >= 10:
            num.append(n % 10)
            n = n // 10
        num.append(n)
        num.reverse()
        
        # Start from the right most digit and find the first 
        # digit that is smaller than the digit next to it
        i = len(num)-1
        while i > 1:
            if num[i] > num[i-1]:
                break
            i -= 1
        if (i == 1 and num[i] <= num[i-1]) or i == 0:
            return -1
        
        # Now we know num[i-1] < num[i]
        # We will find the smallest num but > num[i-1]
        smallest = i
        for j in range(i+1, len(num)):
            if num[j] > num[i-1] and num[j] < num[smallest]:
                smallest = j
        
        # Let's swap i-1 and smallest
        num[i-1], num[smallest] = num[smallest], num[i-1]
        ans = num[0:i] + sorted(num[i:])
        result = 0
        for x in ans:
            result = result * 10 + x
        if result > 2 ** 31 - 1:
            return -1
        return result

if __name__== '__main__':
    solution = Solution()

    # n = 21
    n = 101
    result = solution.nextGreaterElement(n)
    print(result)