class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = []
        list_b = []
        list_res = []
        for digit in a:
            list_a.append(int(digit))
        for digit in b:
            list_b.append(int(digit))
        if len(a) >= len(b):
            main_length = len(a)
        else:
            main_length = len(b)
        carry = False
        for i in range(main_length):
            if i > len(b) - 1 and len(a) != len(b):
                digit_b = 0
            else:
                digit_b = list_b[-(i+1)]
            if i > len(a) - 1 and len(a) != len(b):
                digit_a = 0
            else:
                digit_a = list_a[-(i+1)]

            if not carry:
                sum = digit_a + digit_b
            else:
                sum = digit_a + digit_b + 1
            match sum:
                case 0:
                    if digit_a == 1:
                        carry = True
                    list_res.insert(0, 0)
                case 1:
                    carry = False
                    list_res.insert(0, 1)
                case 2:
                    carry = True
                    list_res.insert(0, 0)
                case 3:
                    carry = True
                    list_res.insert(0, 1)
            if i == main_length - 1 and carry:
                list_res.insert(0, 1)
                break
        res = ""
        for digit in list_res:
            res += str(digit)
        return res