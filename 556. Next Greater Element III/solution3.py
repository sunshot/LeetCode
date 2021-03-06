class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        
        # Start from the right most digit and find the first 
        # digit that is smaller than the digit next to it
        i = len(num)-1
        while i-1 >= 0 and num[i] <= num[i-1]:
            i -= 1
        if i == 0:
            return -1
        
        # Now we know num[i-1] < num[i]
        # We will find the smallest num but > num[i-1]
        smallest = i
        while smallest + 1 < len(num) and num[smallest+1] > num[i-1]:
            smallest += 1
        
        # Let's swap i-1 and smallest
        num[i-1], num[smallest] = num[smallest], num[i-1]
        num[i:] = num[i:][::-1]
        ans = int(''.join(num))
        return ans if ans < 1<<31 else -1

if __name__== '__main__':
    solution = Solution()

    # n = 21
    # n = 101
    n = 12222333
    result = solution.nextGreaterElement(n)
    print(result)
