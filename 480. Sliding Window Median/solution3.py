from typing import List
import heapq
class Solution:
    def move(self, h1, h2) -> None:
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))
    
    def getMedian(self, small, large, k: int):
        if k % 2 != 0:
            return large[0][0]
        else:
            return (large[0][0] - small[0][0]) / 2.0
        
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small(max heap) and large(min heap)
        # all elements in small are <= elements in large
        # large's size - small's size <= 1
        # smallest in large >= largest in small
        # once large's size - small's size > 1, we pop one element from large and add it to small. And vice versa when small's size > large's size.
        
        small = []
        large = []
        ans = []
        for i, x in enumerate(nums[:k]): 
            heapq.heappush(small, (-x,i))
        for _ in range(k - k//2):
            self.move(small, large)
        ans.append(self.getMedian(small, large, k))
        for i, x in enumerate(nums[k:]):
            # consider i+1 .. i+k windows
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]:
                    self.move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    self.move(small, large)
            while small and small[0][1] <= i: 
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            ans.append(self.getMedian(small, large, k))
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.medianSlidingWindow(nums, k)
    # expected = [1, -1, -1, 3, 5, 6]
    print(result)
