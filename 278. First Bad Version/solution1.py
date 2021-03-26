# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    
    def __init__(self, bad: int):
        self.bad = bad
    
    def isBadVersion(self, version):
        self.counter += 1
        if version >= self.bad:
            return True
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.counter = 0

        def binarySearch(start, end) -> int:
            if start == end:
                return start
            mid = start + (end - start) // 2
            if self.isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
            return binarySearch(start, end)
        
        return binarySearch(1, n)

if __name__== '__main__':
    n = 3
    bad = 1
    solution = Solution(bad)

    ans = solution.firstBadVersion(n)
    print(ans == bad)
    print(f'Call isBadVersion: {solution.counter}')