from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = collections.defaultdict(set)
        L = len(beginWord)
        wordList = set(wordList)
        for word in wordList:
            matches = {word[:i]+'*'+word[i+1:] for i in range(L)}
            graph[word] = matches
            for match in matches:
                graph[match].add(word)
        
        # print(graph)
        # Use BFS
        # word, level
        queue = collections.deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        
        while queue:
            word, level = queue.popleft()
            matches = graph[word]
            for match in matches:
                if endWord in graph[match]:
                    return level + 1
                for neigh in graph[match]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, level + 1))
        
        return 0

if __name__== '__main__':
    solution = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    ans = solution.ladderLength(beginWord, endWord, wordList)

    print(ans == 5)