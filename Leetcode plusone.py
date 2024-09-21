class Solution(object):
    def plusOne_myself(self, digits):
        s = ""
        for i in digits:
            s += str(i)

        ans = str(int(s) +1)

        return [int(ans[j]) for j in range(len(ans))]
    def solution_insert(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0,1) 
        return digits  