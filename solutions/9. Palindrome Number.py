class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        j=0
        while n>0:
            j=j*10+(n%10)
            n//=10
        return j==x
