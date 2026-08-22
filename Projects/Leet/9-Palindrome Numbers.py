class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            y = str(x)
            length = last_index = len(y)
            for i in range(length):
                last_index -= 1
                if y[i] != y[last_index]:
                    return False
        
        return True