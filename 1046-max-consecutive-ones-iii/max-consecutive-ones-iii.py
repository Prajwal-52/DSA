class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        zeroCount = 0
        max_count = 0
        for r in range(0,len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            max_count = max(max_count,r-l+1)
        return max_count