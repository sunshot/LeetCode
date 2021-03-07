def longsubstring(s: str) -> str:
    if not s:
        return ''
    result = ''
    i = 0
    lastsequence = ''
    lastsequenceDict = {}
    lastdupIndex = -1
    while i < len(s):
        if s[i] in lastsequenceDict and lastsequenceDict[s[i]] > lastdupIndex:
            #find duplicate
            #detect whether this lastsequence is better
            if len(lastsequence) > len(result):
                result = lastsequence
            index = lastsequenceDict[s[i]]
            lastsequence = s[index+1:i+1]
            lastsequenceDict[s[i]] = i
            lastdupIndex = index
            i += 1
        else:
            lastsequence += s[i]
            lastsequenceDict[s[i]] = i
            i += 1
            
    if len(lastsequence) > len(result):
        result = lastsequence
    i += 1
    return result
    

result = longsubstring('abcad')
print(result)

result = longsubstring('abccccdef')
print(result)

result = longsubstring('')
print(result)

result = longsubstring('ababcd')
print(result)

result = longsubstring('ababcde')
print(result)
                