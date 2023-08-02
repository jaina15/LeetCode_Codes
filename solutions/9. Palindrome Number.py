class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        j=0
        while n>0:
            r = n%10
            j = j*10 + r
            n//=10
        print(j)
        return True if j==x else False
