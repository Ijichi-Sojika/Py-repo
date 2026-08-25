class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        rs = []
        indexed = []
        for i in range(200):
            indexed.append(True)
        baseCmp = strs[0]
        length = len(strs)
        for i in range(0, length):
            word = strs[i]
            if word == '':
                rs.clear()
                break
            index = 0
            for j in range(len(baseCmp)):
                if word[j] == baseCmp[index] and indexed[index]:
                    rs.append(word[j])
                    indexed[index] = False
                elif word[j] != baseCmp[index]:
                    rsLength = len(rs)
                    for k in range(j, rsLength):
                        rs.pop()
                    break
                index += 1
        a = ''
        for letter in rs:
            a += letter
        return a

#runtime is bm lol