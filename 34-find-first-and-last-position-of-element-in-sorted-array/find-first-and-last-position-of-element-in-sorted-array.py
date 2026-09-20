class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def first_found(nums,target):
            l , r = 0 , len(nums)-1
            result = -1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    result=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return result
        def last_found(nums,target):
            l , r = 0 , len(nums)-1
            result = -1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    result=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return result
        return [first_found(nums,target),last_found(nums,target)]