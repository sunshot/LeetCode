# [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

Convert a non-negative integer num to its English words representation.

```
Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

Constraints:

- 0 <= num <= 2^31 - 1

Hints:

- Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
- Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
- There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

Solution1: Direct solution following the hints. But pay attention to a lot of edge cases.

Test cases:

```
123
12345
1234567
1234567891
123000
1000
1000010
0
10
1000000
100
900
```
