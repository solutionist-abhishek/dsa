class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pat = {}
        st = {}
        if len(words) != len(pattern):
            return False
        for c1,c2 in zip(pattern,words):
            if c1 in pat and pat[c1] != c2:
                return False
            if c2 in st and st[c2] != c1:
                return False
            pat[c1] = c2
            st[c2] = c1
        return True
