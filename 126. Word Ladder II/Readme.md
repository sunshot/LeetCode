# [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

- The first word in the sequence is beginWord.
- The last word in the sequence is endWord.
- Only one letter is different between each adjacent pair of words in the sequence.
- Every word in the sequence is in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
```

Constraints:

- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the strings in wordList are unique.

This is followup of [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

Solution1: https://leetcode.com/problems/word-ladder-ii/discuss/933951/Python3-Word-Ladder-II%3A-Simple-BFS

Solution2: https://leetcode.com/problems/word-ladder-ii/discuss/490116/three-python-solution-only-bfs-bfsdfs-bibfs-dfs Similar to the solution in 127. But we need to make sure we traverse all the paths.

See discussion: It's used to guarantee words in one level can visit some common words in the next level. For example, in the 4th level, the words are [dog, log], the last level is [cog]. In the first iteration, 'dog' goes to 'cog', localvisited will go from [] to [cog], but visited remains []. In the second iteration, 'log' goes to 'cog', localvisited will go from [] to [cog]. Only after finishing these two iterations, visited will be updated to [cog]. So in a word, with localvisited, we can visit the next level several times and get several paths, without it, we can only get one path.

