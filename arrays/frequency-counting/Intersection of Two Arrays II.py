from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        a = Counter(nums1)
        b = Counter(nums2)
        for i in a:
            if i in b:
                x = min(a[i],b[i])
                while x > 0:
                    ans.append(i)
                    x -= 1
        return ans
