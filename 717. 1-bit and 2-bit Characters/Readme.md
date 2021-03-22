# [717. 1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/)

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

```
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
```

Note:

- 1 <= len(bits) <= 1000.
- bits[i] is always 0 or 1.

Solution1: Just loop from the start. Runtime: 52 ms, faster than 62.89% of Python3 online submissions for 1-bit and 2-bit Characters.


Solution3: https://leetcode.com/problems/1-bit-and-2-bit-characters/solution/ The second-last 0 must be the end of a character (or, the beginning of the array if it doesn't exist). Looking from that position forward, the array bits takes the form [1, 1, ..., 1, 0] where there are zero or more 1's present in total. It is easy to show that the answer is true if and only if there are an even number of ones present.
