class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[j] = nums[j], nums[i]
                j += 1
                count += 1
        return count
