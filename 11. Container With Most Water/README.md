## Solution

https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

最直接的方法是 O(n^2) 对每一个List中的元素，计算它与其他元素可以装的水，进而判断出最大值，但 List 上了规模时间复杂度太高

讨论区参考解答：

https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation

Idea / Proof:

- The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
- All other containers are less wide and thus would need a higher water level in order to hold more water.
- The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

做法就是先计算出头尾（左右指针）一共能装多少水，然后选取头尾中较小的值，舍弃这个小值（左或右指针），将左指针加1（或右指针减一），直到遍历到左大于等于右


类似的问题：

https://leetcode.com/problems/trapping-rain-water/
