from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i in a:
            if a[i] >= len(nums)/2:
                return i
        
