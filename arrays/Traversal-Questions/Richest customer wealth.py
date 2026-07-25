class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = 0
        for i in accounts:
            w = sum(i)
            max_w = max(max_w,w)
        return max_w
