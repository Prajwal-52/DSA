class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in nums:
            if i in seen and seen[i]>=1:
                return True
            seen[i]=seen.get(i,0)+1
        return False