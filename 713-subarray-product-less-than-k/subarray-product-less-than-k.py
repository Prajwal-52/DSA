class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l = 0
        product = 1
        ans = 0
        if k <= 1:
            return 0
        for r in range(0,len(nums)):
            product *= nums[r]
            while product >= k and l<len(nums):
                product //= nums[l]
                l += 1
            ans += r-l+1
        return ans