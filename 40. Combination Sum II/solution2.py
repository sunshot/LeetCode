from typing import List
import collections
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        if not candidates or len(candidates) == 0:
            return ans
        if len(candidates) == 1:
            if target == candidates[0]:
                result = [candidates[0]]
                ans.append(result)
            return ans
        if sum(candidates) < target:
            return ans
        
        counter = collections.Counter(candidates)
        # convert the counter dicts to a list of (num, count) tuples
        counter = [(num, counter[num]) for num in counter]
        
        # backtrack
        def backtrack(path: List[int], index: int, target: int) -> None:
            if target == 0:
                ans.append(path)
                return
            elif target < 0:
                return
            if index >= len(counter):
                return
            for i in range(index, len(counter)):
                num, freq = counter[i]
                if freq <= 0:
                    continue
                
                # backtrack for i
                counter[i] = (num, freq - 1)
                backtrack(path + [num], i, target - num)
                
                # restore
                counter[i] = (num, freq)
                
        backtrack([], 0, target)
        return ans



if __name__== '__main__':
    solution = Solution()

    candidates = [10,1,2,7,6,1,5]
    target = 8

    ans = solution.combinationSum2(candidates, target)
    print(ans)

    