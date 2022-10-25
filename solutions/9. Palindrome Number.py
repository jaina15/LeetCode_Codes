class Solution:
    def isPalindrome(self, x: int) -> bool:
        n,j,r=x,0,0
        while n>0:
            r=n%10
            j=j*10+r
            n=n//10
        return True if x==j else False
