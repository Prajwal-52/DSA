class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] == nums[i-1] :
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                while nums[j] == nums[j-1] and j>i+1:
                    j+=1
                while k<len(nums)-1 and nums[k] == nums[k+1]:
                    k-=1
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
                elif s<0:
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                else:
                    k-=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1
        return ans                
