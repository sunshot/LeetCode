# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

![image](https://user-images.githubusercontent.com/13043834/109388114-1ad58200-7940-11eb-84e8-c46d7fcd27cb.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

中文题目参考：直方图的水量
https://leetcode-cn.com/problems/volume-of-histogram-lcci/

中文解答参考：
https://leetcode-cn.com/problems/volume-of-histogram-lcci/solution/shuang-zhi-zhen-zhi-fang-tu-de-shui-liang-by-realz/

很多方法可解，对于List中某个位置i，如果能知道i左边最高的 leftmax，和右边最高的 rightmax，设 minH = min(leftmax, rightmax) 如果 minH 大于 height[i] 则i处能装的雨水是： minH - height[i]

可以提前计算出 leftmax 和 rightmax，总体时间复杂度 O(n)

参考解答还给出了利用栈来解决，参考：

https://leetcode.com/problems/trapping-rain-water/solution/

We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to \text{ans}ans.

