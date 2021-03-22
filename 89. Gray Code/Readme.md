# [89. Gray Code](https://leetcode.com/problems/gray-code/)

The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

```
Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1

Input: n = 1
Output: [0,1]
```

Constraints:

- 1 <= n <= 16

Solution1: see https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments) 没有想到解法，参考讨论区答案

https://leetcode.com/problems/gray-code/discuss/29891/Share-my-solution

My idea is to generate the sequence iteratively. For example, when n=3, we can get the result based on n=2.
00,01,11,10 -> (000,001,011,010 ) (110,111,101,100). The middle two numbers only differ at their highest bit, while the rest numbers of part two are exactly symmetric of part one. It is easy to see its correctness.

```java
public List<Integer> grayCode(int n) {
    List<Integer> rs=new ArrayList<Integer>();
    rs.add(0);
    for(int i=0;i<n;i++){
        int size=rs.size();
        for(int k=size-1;k>=0;k--)
            rs.add(rs.get(k) | 1<<i);
    }
    return rs;
}
```

Say the example input is 3.

0 000
1 001
3 011
2 010

6 110
7 111
5 101
4 100

For the pair of (2, 6), (3, 7), (1, 5) and (0, 4), the last 2 bits are the same. The only difference is 6,7,5 and 4 set the first bit on. Hope this helps.

