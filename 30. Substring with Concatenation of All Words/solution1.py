from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        for x in words:
            if x not in s:
                return []
        step = len(words[0])
        words_len = step * len(words)
        result = []
        words.sort()
        for i in range(len(s)-words_len+1):
            if s[i:i+step] in words:
                # Let's detect whether s[i:i+words_len] is concatenation
                concate = []
                for j in range(i, i+words_len, step):
                    concate.append(s[j:j+step])
                concate.sort()
                #compare words and concate
                isEqual = True
                for a, b in zip(words, concate):
                    if a!=b:
                        isEqual = False
                        break
                if isEqual:
                    result.append(i)
        return result

if __name__== '__main__':
    solution = Solution()

    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    result = solution.findSubstring(s, words)
    print(result == [6,9,12])

