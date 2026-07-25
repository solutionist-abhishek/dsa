class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        if nums[0] < nums[len(nums)-1]:
            drops += 1
        for i in range(len(nums)):
            if drops > 1:
                return False
            if i+1 < len(nums) and nums[i] > nums[i+1]:
                drops += 1
        return True
