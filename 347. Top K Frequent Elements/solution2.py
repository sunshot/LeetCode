from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = collections.Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key = count.get)

if __name__== '__main__':
    solution = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    ans = solution.topKFrequent(nums, k)
    print(ans)