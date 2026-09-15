class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            if s[0].isalpha():
                return 1
            else:
                return 0
        count = 0
        foundStart = False
        for i in range(len(s)):
            if not s[-(i+1)].isalpha() and not foundStart:
                continue
            elif not s[-(i+1)].isalpha() and foundStart:
                break
            elif s[-(i+1)].isalpha() and not foundStart:
                foundStart = True
                count += 1
            else:
                count += 1
        return count