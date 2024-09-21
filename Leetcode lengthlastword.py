class Solution(object):
    def lengthOfLastWord_myself(self, s):
        a = s.strip()
        b = a.split(" ")
        c = b[-1]
        return len(c)   
    def slower_myself(self, s):
        a = 0
        b = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ' and ( i == 0 or s[i-1] == ' '):
                a = i
                break
        for j in range(len(s)-1,-1,-1):
            if s[j] != ' ':
                b = j
                break
        return b - a + 1