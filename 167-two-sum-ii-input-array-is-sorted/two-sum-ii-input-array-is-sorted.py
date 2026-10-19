class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [i+1,j+1]
            if s < target:
                i += 1
            else:
                j -= 1
        return []
