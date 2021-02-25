## Solution

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

重点是时间复杂度 O(n)，空间复杂度 O(1)

采用两个 pointers 的思路，一个指向当前不重复的位置 unique，另一个用于遍历数组 curr，当发现两者相等时，仅移动 curr；当两者不等时，将 curr 赋值给下一个位置的 unique

最后，unique 指向最后的不重复的元素，把之后的元素 pop 出来即可

类似问题：

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

修改起始条件和判断条件即可

````
        curr = 2
        unique = 1
        for curr in range(2, len(nums)):
            if nums[curr] != nums[unique] or (nums[curr] == nums[unique] and 
                                             nums[curr] != nums[unique-1]):
                unique += 1
                if unique != curr:
                    nums[unique] = nums[curr]
````