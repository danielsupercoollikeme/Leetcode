class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        for i in range(rowIndex + 1):
            if i == 0:
                a = [1]
                l.append(a)
            else:
                b = [1]
                j = 1
                while j < i:
                    b.append(a[j - 1] + a[j])
                    j += 1 
                b.append(1)
                l.append(b)
                a = b
        return l[rowIndex]
    def solution_down(self, r):
        ans = [1] * (r + 1)
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = ans[i - 1] * up/down
            up = up - 1
            down = down + 1
        return ans