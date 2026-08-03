class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            s = nums[i] * nums[i]
            nums[i] = s
        return sorted(nums)
