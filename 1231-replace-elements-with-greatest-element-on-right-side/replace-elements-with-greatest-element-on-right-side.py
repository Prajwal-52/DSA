class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=len(arr)-1
        while i>=0:
            if i==len(arr)-1:
                currentMax=arr[i]
                arr[i]=-1
                i-=1
                continue
            temp=arr[i]
            arr[i]=currentMax
            if temp>currentMax:
                currentMax=temp
            i-=1
        return arr