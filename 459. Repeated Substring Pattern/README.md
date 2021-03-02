# 459. Repeated Substring Pattern

https://leetcode.com/problems/repeated-substring-pattern/

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

思路：判断第一个字符从字符串结尾开始搜索所处的位置，以该位置到结尾作为substring，看看是否满足条件，遍历完所有可能的位置

讨论中的参考解答：

https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination

1.First char of input string is first char of repeated substring
1.Last char of input string is last char of repeated substring
1.Let S1 = S + S (where S in input string)
1.Remove 1 and last char of S1. Let this be S2
1.If S exists in S2 then return true else false
1.Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
