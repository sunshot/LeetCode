# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

This is followup question of [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

暴力解法：对每个字符串，计算出 Counter hash 值，然后与其他字符串的 Counter 进行比较

参考解答：

https://leetcode.com/problems/group-anagrams/solution/

Categorize by Sorted String

Maintain a map ans : {String -> List} where each key \text{K}K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to \text{K}K.

In Java, we will store the key as a string, eg. code. In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

- Time Complexity: O(NK \log K)O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs

- Space Complexity: O(NK)O(NK), the total information content stored in ans

Categorize by Count

Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.