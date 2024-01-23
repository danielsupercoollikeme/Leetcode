class Solution(object):
    def romanToInt_myself(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                n -= translations[s[i]]
            elif i + 1 < len(s) and s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                n -= translations[s[i]]
            elif i + 1 < len(s) and s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                n -= translations[s[i]]
            else:
                n += translations[s[i]]
        return n
    def solution_replace(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            n += translations[char]
        return n
    def solution_fast(self, s: str) -> int:
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = 0
        for i in range(len(s) - 1, -1, -1):
            a = translations[s[i]]

            if i < len(s) - 1 and a < translations[s[i + 1]]:
                n -= a
            else:
                n += a

        return n