class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            y = str(x)
            for i in range(len(y)):
                if y[i] != y[-(i+1)]:
                    return False
        
        return True