class Solution:
    def isPalindrome(self, x: int) -> bool:
        n,j=x,0
        while n>0:
            r=n%10
            j=j*10+r
            n//=10
        return j==x
