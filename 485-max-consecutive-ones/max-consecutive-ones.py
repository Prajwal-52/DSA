class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count=0
        max_count=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                current_count+=1
            else:
                max_count=max(max_count,current_count)
                current_count=0
        return max(max_count,current_count)