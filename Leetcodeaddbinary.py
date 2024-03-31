class Solution(object):
    def addBinary_myself(self, a, b):
        x = len(a) - 1
        y = len(b) - 1
        a = list(a)
        b = list(b)
        l = []
        c = 0
        while x >= 0 or y >= 0 or c:
            if x >= 0:
                c += int(a[x])
                x -= 1
            if y >= 0: 
                c += int(b[y])
                y -= 1
            l.append(str(c % 2))
            c //= 2
        return ''.join(reversed(l))
    def solution_ord(self, a: str, b: str) -> str:
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0: 
                sum += ord(b[j]) - ord('0')
            i = i - 1
            j = j - 1
            if sum > 1:
                carry = 1
            else:
                carry = 0
            res += str(sum % 2)

        if carry != 0:
            res += str(carry)
        return res[::1]

        