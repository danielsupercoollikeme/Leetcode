class Solution(object):
    def longestCommonPrefix_myself(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        n = min(len(x) for x in strs)
        prefix = ""
        for i in range(n):
            a = strs[0][i]
            for j in strs:
                if j[i] != a:
                    return prefix
            prefix += a
        return prefix
    def solution_slice(self, strs):
        prefix = strs[0]
        for i in strs[1:]:
            while i.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix