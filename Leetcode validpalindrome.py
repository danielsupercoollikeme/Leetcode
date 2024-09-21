class Solution(object):
    def solution_myself(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = len(s) - 1
        while a < b:
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True
    def solution_operator(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s) //2))