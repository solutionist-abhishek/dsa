class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans :bool = []
        for i in candies:
            temp  = i + extraCandies
            if temp >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
