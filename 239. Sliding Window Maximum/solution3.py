from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return nums
        result = []
        queue = collections.deque()
        # First traversing through K in the nums
        # Only add max num to the queue
        for i in range(k):
            while queue:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
        for i in range(k, len(nums)):
            # Leftmost is the result of last round
            # pop leftmost if not in the range i-k+1..i
            if queue:
                result.append(nums[queue[0]])
                if queue[0] < i - k + 1:
                    queue.popleft()
            # for curr i, we will pop rightmost when nums[i] > nums[rightmost]
            # we will always push i into queue
            while queue:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
        if queue:
            result.append(nums[queue[0]])
        return result


if __name__== '__main__':
    solution = Solution()

    nums = [1, -1]
    k = 1
    result = solution.maxSlidingWindow(nums, k)
    print(result)