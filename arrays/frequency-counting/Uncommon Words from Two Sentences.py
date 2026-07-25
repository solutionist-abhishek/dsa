from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_ls = s1.split()
        s2_ls = s2.split()
        ans = []
        a = Counter(s1_ls)
        b = Counter(s2_ls)
        for i in a:
            if a[i]==1 and i not in b:
                ans.append(i)
        for i in b:
            if b[i]==1 and i not in a:
                ans.append(i)
        return ans
