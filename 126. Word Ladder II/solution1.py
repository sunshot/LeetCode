import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(set)
        l = len(wordList[0])

        wordList = set(wordList)
        if endWord not in wordList:
            return []

        wordList.add(beginWord)

        def get_matches(word):
            return {word[:i]+'*'+word[i+1:] for i in range(l)}

        for word in wordList:
            matches = get_matches(word)
            for match in matches:
                graph[match].add(word)
            graph[word] = matches

        ans = []
        min_path = None
        seen = set()

        q = collections.deque([(beginWord, 1, [beginWord])])

        while q:
            word, length, seq = q.popleft()

            for w in graph[word]:
                if w == endWord and (not min_path or min_path == length+1):
                    min_path = length+1
                    seq.extend([w])
                    ans.append(seq)
                    seen.add(w)
            
                if w not in seen:   
                    if w in wordList:
                        q.append((w, length, seq+[w]))
                    else:
                        q.append((w, length+1, seq))
            seen.add(word)

        return ans
        
if __name__== '__main__':
    solution = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    ans = solution.findLadders(beginWord, endWord, wordList)
    print(ans)