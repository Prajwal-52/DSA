class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        ans=k
        while ans in num:
            ans +=k
        return ans