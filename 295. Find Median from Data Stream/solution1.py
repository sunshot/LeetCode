from typing import List
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # small(max heap) and large(min heap)
        # all elements in small are <= elements in large
        # large's size - small's size <= 1
        # smallest in large >= largest in small
        # once large's size - small's size > 1, we pop one element from large and add it to small. And vice versa when small's size > large's size.
        self.small = []
        self.large = []
        self.k = 0
        

    def addNum(self, num: int) -> None:
        if self.k == 0:
            heapq.heappush(self.large, num)
            self.k += 1
            return
        self.k += 1
        if num >= self.large[0]:
            heapq.heappush(self.large, num)
            if len(self.large) - len(self.small) > 1:
                self.move(self.large, self.small)
        else:
            heapq.heappush(self.small, -num)
            if len(self.large) < len(self.small):
                self.move(self.small, self.large)
        

    def findMedian(self) -> float:
        if self.k == 0:
            return None
        if self.k % 2 != 0:
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2.0
        
    
    def move(self, h1, h2) -> None:
        num = heapq.heappop(h1)
        heapq.heappush(h2, -num)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__== '__main__':
    solution = MedianFinder()

    solution.addNum(1)
    solution.addNum(2)
    print(solution.findMedian())
    solution.addNum(3)
    print(solution.findMedian())
    solution.addNum(2)
    print(solution.findMedian())