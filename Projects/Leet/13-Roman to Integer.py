class Solution:
    def romanToInt(self, s: str) -> int:
        ls = []
        for char in s:
            match char:
                case "I":
                    ls.append(1)
                case "V":
                    ls.append(5)
                case "X":
                    ls.append(10)
                case "L":
                    ls.append(50)
                case "C":
                    ls.append(100)
                case "D":
                    ls.append(500)
                case "M":
                    ls.append(1000)
        
        sum = 0
        length = len(ls)
        iBTP = False
        for i in range(length):
            if iBTP:
                iBTP = False
                continue

            if i == length - 1:
                sum += ls[i]
                break

            if ls[i] < ls[i+1]:
                iBTP = True
                sum += ls[i+1] - ls[i]
            else:
                iBTP = False
                sum += ls[i]
        
        return sum