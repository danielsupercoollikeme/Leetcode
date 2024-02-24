class Solution(object):
    def solution_myself(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k = haystack.find(needle)
        return k
    def solution_slow(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        