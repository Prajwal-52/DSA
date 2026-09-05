class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=float("-inf")
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            if sum>max_sum:
                max_sum=sum
            if sum<0:
                sum=0
        return max_sum