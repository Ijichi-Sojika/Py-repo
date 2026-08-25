class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if s.count("(") != s.count(")") or s.count("{") != s.count("}") or s.count("[") != s.count("]"):
            return False
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        if s[-1] == "(" or s[-1] == "{" or s[-1] == "[":
            return False
        cmp = []
        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                cmp.append(letter)
            else:
                match letter:
                    case ")":
                        if cmp[-1] == "(":
                            cmp.pop()
                        else:
                            return False
                    case "}":
                        if cmp[-1] == "{":
                            cmp.pop()
                        else:
                            return False
                    case "]":
                        if cmp[-1] == "[":
                            cmp.pop()
                        else:
                            return False
        if len(cmp) != 0:
            return False
        return True