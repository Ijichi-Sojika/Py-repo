class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            if digits[0] != 9:
                digits[0] += 1
            else:
                digits[0] = 0
                digits.insert(0, 1)
            return digits
        carry = False
        for i in range(len(digits)):
            if i == 0:
                if digits[-(i+1)] != 9:
                    digits[-(i+1)] += 1
                else:
                    digits[-(i+1)] = 0
                    carry = True
            else:
                if not carry:
                    continue
                else:
                    if i != len(digits) - 1:
                        if digits[-(i+1)] != 9:
                            digits[-(i+1)] += 1
                            carry = False
                        else:
                            digits[-(i+1)] = 0
                            carry = True
                    else:
                        if digits[-(i+1)] != 9:
                            digits[-(i+1)] += 1
                        else:
                            digits[-(i+1)] = 0
                            digits.insert(0, 1)
        return digits