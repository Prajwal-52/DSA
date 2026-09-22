class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        max_count = 0
        n = len(nums)
        j=0
        while j < n:
            if nums[j] == 1:
                count += 1
            else:
                max_count = max(max_count , count)
                count = 0
            j += 1
        return max(max_count , count)