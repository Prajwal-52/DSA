class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i=0
        current_count=0
        max_count=0
        for j in range(len(nums)):
            if nums[j]==1:
                continue
            else:
                current_count=j-i
                i=j+1
                max_count=max(max_count,current_count)
        current_count=j-i+1
        max_count=max(max_count,current_count)
        return max_count