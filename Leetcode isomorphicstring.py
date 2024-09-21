class Solution(object):
    def solution_myself(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        b = []
        for i in s:
            a.append(s.index(i))
        for j in t:
            b.append(t.index(j))
        if a == b:
            return True
        else:
            return False
    def solution_oneline(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))