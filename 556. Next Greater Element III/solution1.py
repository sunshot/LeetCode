class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = []
        while n >= 10:
            num.append(n % 10)
            n = n // 10
        num.append(n)
        num.reverse()
        
        # start from right most to find the next greater element
        stack = []
        isFind = False
        for i in range(len(num)-1, -1, -1):
            while stack and num[stack[-1]] <= num[i]:
                stack.pop()
            if stack and num[stack[-1]] > num[i]:
                # We find a result
                isFind = True
                break
            stack.append(i)
        if not isFind:
            return -1
        
        # We find i index has next greater element, let find the min next greater element
        min_index = stack.pop()
        j = i + 1
        while j < len(num):
            if num[j] > num[i] and num[j] < num[min_index]:
                min_index = j
            j += 1
        # Let's swap i and min_index
        num[i], num[min_index] = num[min_index], num[i]
        ans = num[0:i+1] + sorted(num[i+1:])
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