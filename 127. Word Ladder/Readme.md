# [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

- The first word in the sequence is beginWord.
- The last word in the sequence is endWord.
- Only one letter is different between each adjacent pair of words in the sequence.
- Every word in the sequence is in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
```

Constraints:

- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the strings in wordList are unique.

Solution: https://blog.csdn.net/qq_46595591/article/details/108021281

Analysis Process
1.Preprocess the given wordList to find all the universal states and record the universal states in the dictionary, the key is the universal state, and the value is all the words with the universal state
universal state:Replace a letter in a word with *
2.Put tuples that have beginWord and 1 in the queue,1 represents the hierarchy of nodes and we need to return the hierarchy of endWord which is the shortest distance from beginWord
3.To prevent rings, access array records are used
4.When there are elements in the queue, the first element is fetched and recorded as Current Word
5.Find all common states of Current Word, and check whether these common states have mappings for other words, which is done by checking all Combo dict
6.All the words obtained in All Combo dict have a common state with Current Word, so they are connected to Current Word, so they are added to the queue
7.For all newly acquired words, add elements to the queue (word, level + 1) where level is the hierarchy of Current Word
8.Finally, when you reach the desired word, the corresponding level is the length of the shortest transformation sequence



https://leetcode.com/problems/word-ladder/discuss/40710/Share-my-two-Python-solutions%3A-a-very-concise-one-(12-lines-~160ms)-and-an-optimized-solution(~100ms)

https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95

