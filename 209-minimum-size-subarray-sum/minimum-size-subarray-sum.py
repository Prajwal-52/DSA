class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        count=float('inf')
        currentCount=0
        sum=0
        l=0
        n=len(nums)
        for r in range(n):
            sum+=nums[r]
            while sum>=target:
                currentCount=r-l+1
                count=min(currentCount,count)
                sum-=nums[l]
                l+=1
        return 0 if count==float('inf') else count