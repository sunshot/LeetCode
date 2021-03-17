from typing import List
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or endWord not in wordList or beginWord == endWord:
            return []
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
        # word, path
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        visited = set()
        visited.add(beginWord)
        ans = []
        
        while queue and not ans:
            level = len(queue)
            localVisited = set()
            for _ in range(level):
                word, path = queue.popleft()
                matches = graph[word]
                for match in matches:
                    for neigh in graph[match]:
                        if neigh == endWord:
                            ans.append(path + [neigh])
                        if neigh not in visited:
                            localVisited.add(neigh)
                            queue.append((neigh, path + [neigh]))
            visited.update(localVisited)
        
        return ans
        
if __name__== '__main__':
    solution = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    ans = solution.findLadders(beginWord, endWord, wordList)
    print(ans)