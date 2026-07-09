class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitstr = ""
        digitsout = []

        for digit in digits:
            digitstr += str(digit)
        digitstr = int(digitstr) + 1

        for digit in str(digitstr):
            digitsout.append(int(digit))

        return digitsout
        