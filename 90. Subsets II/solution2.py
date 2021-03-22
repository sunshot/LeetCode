from typing import List
import collections
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        counter = collections.Counter(nums)
        # convert the counter dicts to a list of (num, count) tuples
        counter = [(num, counter[num]) for num in counter]
        
        # backtrack
        def backtrack(path: List[int], index: int) -> None:
            if len(path) > len(nums):
                return
            if index > len(counter):
                return
            ans.append(path)
            
            for i in range(index, len(counter)):
                num, freq = counter[i]
                if freq <= 0:
                    continue
                
                # backtrack for i
                counter[i] = (num, freq - 1)
                backtrack(path + [num], i)
                
                # restore
                counter[i] = (num, freq)
        
        backtrack([], 0)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,2,2]
    ans = solution.subsetsWithDup(nums)
    print(ans)