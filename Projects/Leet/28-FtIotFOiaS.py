# find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        for i in range(len(haystack)):
            if i > len(haystack) - len(needle):
                return -1
            check = True
            dex = 0
            for need in needle:
                if haystack[i+dex] != need:
                    check = False
                    break
                else:
                    dex += 1
            if check:
                return i
        return -1