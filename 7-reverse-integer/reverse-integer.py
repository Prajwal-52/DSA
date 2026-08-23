class Solution:
    def reverse(self, x: int) -> int:
        is_negative=False
        if x<0:
            is_negative=True
        num=abs(x)
        ans=0
        while num>0:
            last_digit=num%10
            ans=(ans*10)+last_digit
            num //=10
        if ans<(-2**31) or ans>(2**31-1):
            return 0
        if is_negative:
            return -ans
        else:
            return ans