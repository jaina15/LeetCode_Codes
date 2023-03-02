class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans=0
        j=0
        c=0
        while n>0:
            j=j*10+(n%10)
            n//=10
        while j>0:
            if c%2==0:
                ans+=(j%10)
            else:
                ans-=(j%10)
            c+=1
            j//=10
        return ans
