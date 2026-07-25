from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = Counter(s)
        b = Counter(t)
        for i in t:
            if i not in s:
                return i
            if a[i] != b[i]:
                return i
