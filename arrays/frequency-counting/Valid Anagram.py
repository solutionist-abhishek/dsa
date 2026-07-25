from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        if len(s) != len(t):
            return False
        for i in a:
            if i not in b:
                return False
            if a[i] > b[i]:
                return False
        return True 
