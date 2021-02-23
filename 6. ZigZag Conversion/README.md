
## ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

类似于之字形，先向下走一竖列，然后往右上走一个斜角线。如果是 numRows 则一个小循环中，第一竖列是 numRows 个字符，接下来是 ``numRows-2`` 个竖列，每个竖列一个字符

## Solution1

笨办法，straightforward 方法，先构造一个二维数组，然后按照 ZigZag 的规律填充这个二维数组。首先计算出最多需要多少个循环 ``n//(numRows*2-2)+1`` 假设 n 为字符串的长度，然后每个循环有 ``numRows - 1`` 列，来确定最大需要的二维数组的列数。然后对每个循环进行填充，最后考虑边界条件。二维数组填充完后，对二维数组进行遍历，得到最后结果

## Solution2

参考答案第二个方法。每一个循环需要填充 ``2 * numRows - 2`` 个字符，因此，对第0行，出现的字符位置分别是：`` k * (2 * numRows - 2)``，对最后一行，出现的字符位置分别是: ``k * (2 * numRows - 2) + (numRows -1)``，对于中间行 i，出现的字符包括循环的第一列： ``k * (2 * numRows - 2) + i`` 和另一个字符: ``(k+1) * (2 * numRows - 2) - i``

设 ``cycleLen = 2*numRows-2`` 可以使用循环的方式求出每一行出现的字符

## Solution3

非常巧妙：https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
维护一个 numRows 的 List，每个元素表示对应行出现的字符，遍历整个字符串时，就将此List填充了
