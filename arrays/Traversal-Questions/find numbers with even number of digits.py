class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            dig_count = 0
            while i > 0:
                dig_count += 1
                i = i//10
            if dig_count % 2 == 0:
                count += 1
        return count
