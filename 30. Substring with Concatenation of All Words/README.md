# 30. Substring with Concatenation of All Words

https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

## Test case

```python
"barfoothefoobarman"
["foo","bar"]
"wordgoodgoodgoodbestword"
["word","good","best","word"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
"aaaaaaaaaaaaaa"
["aa","aa"]
```

## Solution

注意到坑：words 里面的单词可能会重复，单词本身可能也会有overlap

```python
step = len(words[0])
words_len = step * len(words)
```

难点有： 如何从 s 中找到起始点 i，判断 i:i+words_len 的字符串是 words 中的单词拼接成的，考虑到上述坑的存在，最保险的办法是从 s 的 0 开始遍历。判断是否为拼接，solution1 用了比较两个有序的 list 的方法，另外，遍历的时候即使成功了，也需要从下一个位置开始重新遍历，因为有类似这样的测试例：

```python
"aaaaaaaaaaaaaa"
["aa","aa"]
```
