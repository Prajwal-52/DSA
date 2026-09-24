class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            digit_sum = 0
            x = nums[i]
            while x > 0:
                digit_sum += x%10
                x //= 10
            if digit_sum == i:
                return i
        return -1