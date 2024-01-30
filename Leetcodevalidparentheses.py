class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                l.append(i)
            else:
                if not l or (i == ')' and l[-1] != '(') or (i == '}' and l[-1] != '{') or (i == ']' and l[-1] != '['):
                    return False
                l.pop()
        if not l:
            return True
        else:
            return False
    def solution_short(self, s):
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True