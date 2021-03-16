from typing import List
import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        group = [(k, len(list(grp))) for k, grp in itertools.groupby(nums)]
        group.sort(key = lambda  x:x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(group[i][0])
        return result

if __name__== '__main__':
    solution = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    ans = solution.topKFrequent(nums, k)
    print(ans)