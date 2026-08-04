class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        m = 0
        while i < j:
            a = min(height[i],height[j])* (j-i)
            m = max(m,a)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return m
