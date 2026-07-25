from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i in a:
            if i not in b:
                return False
            if a[i] > b[i]:
                return False
        return True
