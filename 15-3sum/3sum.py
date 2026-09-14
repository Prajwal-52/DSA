class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i=0
        res=[]
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            if nums[i]==nums[i-1] and i>0:
                i+=1
                continue
            while j<k:
                t=nums[i]+nums[j]+nums[k]
                if t==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif t<0:
                    j+=1
                else:
                    k-=1
            i+=1
        return res