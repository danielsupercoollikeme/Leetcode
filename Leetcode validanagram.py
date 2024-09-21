class Solution(object):
    def solution_myself(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        for i in set(t):
            if s.count(i) != t.count(i):
                return False
        return True
    def solution_extend(self, s, t):
        s1 = []
        t1 = []
        s1.extend(s)
        t1.extend(t)
        s1.sort()
        t1.sort()
        if s1 == t1:
            return True
        else:
            return False