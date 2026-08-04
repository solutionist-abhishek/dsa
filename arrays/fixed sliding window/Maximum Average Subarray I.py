class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win = nums[:k]
        win_sum = sum(nums[:k])
        win_avg = win_sum / k
        best = win_avg
        for i in range(k,len(nums)):
            win_sum += nums[i]
            win_sum -= nums[i-k]
            win_avg = win_sum / k
            best = max(best,win_avg)
        return best
