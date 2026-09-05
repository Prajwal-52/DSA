class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        mini=float("inf")
        leftmin=[0]*n
        for i in range(n-1,-1,-1):
            mini=min(mini,nums[i])
            leftmin[i]=mini
        maxi=float("-inf")
        for i in range(0,n):
            maxi=max(maxi,nums[i])
            if maxi - leftmin[i] <= k:
                return i
        return -1
        