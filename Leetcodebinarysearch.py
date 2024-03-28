class Solution(object):
    def mySqrt_myself(self, x):
        a, b = 0, x
        while a <= b:
            mid = a + (b - a)//2
            if mid * mid <= x < (mid + 1)*(mid + 1):
                return mid
            elif x < mid * mid:
                b = mid - 1
            else:
                a = mid + 1
    def solution_float(self, x):
        a = float(10**((len(str(x)) + 1) // 2))
        while int(a * a) > x:
            a = (a + x / a) / 2
        return int(a)